import streamlit as st
from dotenv import load_dotenv
import os
from langchain_google_genai import GoogleGenerativeAIEmbeddings, ChatGoogleGenerativeAI
from langchain.prompts import PromptTemplate
from langchain.chains.question_answering import load_qa_chain
from pinecone import Pinecone
import google.generativeai as genai
from langchain.schema import Document

# Load environment variables from .env file
load_dotenv('C:/Users/juile/OneDrive/Desktop/Personal/Prompt eng/RAG Chatbot/.env')

# Retrieve API keys from environment variables
PINECONE_API_KEY = os.getenv("PINECONE_API_KEY")
GOOGLE_GENAI_API_KEY = os.getenv("GOOGLE_GENAI_API_KEY")

# Initialize Pinecone
pc = Pinecone(api_key=PINECONE_API_KEY)
index_name = "rag-chatbot"

# Check if the index exists, if not create it
index = pc.Index(index_name)

# Generate embeddings
embeddings = GoogleGenerativeAIEmbeddings(model="models/embedding-001")

# Function to create the conversational chain
def get_conversational_chain():
    prompt_template = """
    Answer the question as detailed as possible from the provided context. Make sure to provide all the details.Increase the readability of the output\n\n
    Context:\n{context}\n
    Question: \n{question}\n
    Answer:
    """

    model = ChatGoogleGenerativeAI(model="gemini-pro", temperature=0.3)
    prompt = PromptTemplate(template=prompt_template, input_variables=["context", "question"])
    chain = load_qa_chain(llm=model, chain_type="stuff", prompt=prompt)

    return chain

# Function to handle query and response generation
def handle_query(query):
    try:
        # Embed the query
        query_embedding = embeddings.embed_query(query)
        
        # Search for the relevant context in Pinecone using keyword arguments
        results = index.query(vector=query_embedding, top_k=2, include_metadata=True)
        
        contexts = [result['metadata']['text'] for result in results['matches']]
        scores = [result['score'] for result in results['matches']]

        if contexts and max(scores) > 0.03:
            # Prepare the documents for the chain
            input_documents = [Document(page_content=context) for context in contexts]

            # Generate response using the conversational chain
            chain = get_conversational_chain()
            response = chain.invoke({"input_documents": input_documents, "question": query})

            response_text = response['output_text'] + " Is there anything else I can help with? I hope you feel better soon."
            return contexts, response_text

        else:
            return [], "Answer is not available in the context"
    except Exception as e:
        st.error(f"An error occurred: {e}")
        return [], "An error occurred"

# Function to handle input change
def on_input_change():
    user_input = st.session_state.query
    st.session_state.chat_history.append({"role": "user", "text": user_input})
    contexts, response_text = handle_query(user_input)

    if contexts:
        st.session_state.chat_history.append({"role": "agent", "text": f"Context:\n{''.join(contexts)}"})
    if response_text:
        st.session_state.chat_history.append({"role": "agent", "text": response_text})
    st.session_state.query = ""

# Main function to run the Streamlit app
def main():
    st.set_page_config(page_title="PDF Chatbot", layout="wide")
    
    # Custom CSS for styling
    st.markdown(
        """
        <style>
        .stApp {
            background-color: #f5f5f5;
        }
        .user-bubble {
            background-color: #E0FFFF;
            color: #696969;
            padding: 10px;
            border-radius: 10px;
            max-width: 60%;
            margin: 10px 0;
        }
        .bot-bubble {
            background-color: teal;
            color: white;
            padding: 10px;
            border-radius: 10px;
            max-width: 60%;
            margin: 10px 0;
        }
        .avatar {
            width: 30px;
            height: 30px;
            border-radius: 50%;
            display: inline-block;
            margin-right: 10px;
        }
        .chat-row {
            display: flex;
            align-items: center;
        }
        .chat-row.user {
            justify-content: flex-end;
        }
        .chat-row.bot {
            justify-content: flex-start;
        }
        .teal-title h1 {
            color: teal;
        }
        </style>
        """,
        unsafe_allow_html=True
    )
    
    st.markdown('<div class="teal-title"><h1>PDF Chatbot</h1></div>', unsafe_allow_html=True)

    genai.configure(api_key=GOOGLE_GENAI_API_KEY)

    if 'chat_history' not in st.session_state:
        st.session_state.chat_history = []

    # Chat agent introduction
    if not st.session_state.chat_history:
        st.session_state.chat_history.append({"role": "agent", "text": "Hello! I'm Dr, your home remedy doctor. How can I assist you today with your health concerns?"})

    # Display chat history
    for chat in st.session_state.chat_history:
        if chat['role'] == 'agent':
            st.markdown(f"""
            <div class="chat-row bot">
                <div class="avatar" style="background-color: teal;"></div>
                <div class="bot-bubble">{chat['text']}</div>
            </div>
            """, unsafe_allow_html=True)
        else:
            st.markdown(f"""
            <div class="chat-row user">
                <div class="user-bubble">{chat['text']}</div>
            </div>
            """, unsafe_allow_html=True)

    # User input
    st.text_input("Ask a question about the PDF:", key='query', on_change=on_input_change)

if __name__ == "__main__":
    main()
