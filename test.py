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
    Answer the question as detailed as possible from the provided context. Use markdown for formatting, such as lists and headings, to enhance readability. Include all relevant details.
    If the context provided does not have relevant answer then just say something like the its not relevant to context try asking something relevant \n\n
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

        # Concatenate all contexts
        combined_context = "\n\n".join(contexts)

        if contexts and max(scores) > 0.03:
            # Prepare the document for the chain
            input_document = Document(page_content=combined_context)

            # Generate response using the conversational chain
            chain = get_conversational_chain()
            response = chain.invoke({"input_documents": [input_document], "question": query})

            response_text = response['output_text'] + "\n\nIs there anything else I can help with? I hope you feel better soon."
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

    if response_text:
        st.session_state.chat_history.append({"role": "agent", "text": response_text})
    st.session_state.query = ""

# Function to restart the chat
def restart_chat():
    st.session_state.chat_history = [{"role": "agent", "text": "Hello! I'm WellnessBot, your wellness advisor. How can I assist you today with your health concerns?"}]

# Function to show help message
def show_help():
    st.session_state.chat_history.append({"role": "agent", "text": "You can ask me questions about the PDF content, and I will try my best to provide detailed answers. If you need to start over, click the 'Restart Chat' button."})

# Main function to run the Streamlit app
def main():
    st.set_page_config(page_title="WellnessBot", layout="wide")

    # Custom CSS for styling
    st.markdown(
        """
        <style>
        .stApp {
            background-color: #f5f5f5;
            padding-top: 0;
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
        .header-bar {
            display: flex;
            justify-content: space-between;
            align-items: center;
            background-color: #008080;
            padding: 10px;
            color: white;
            width: 100%;
            position: fixed;
            top: 40px;
            left: 0;
            z-index: 1000;
            font-size: 18px;
        }
        .header-bar .menu {
            display: flex;
            align-items: center;
            cursor: pointer;
        }
        .header-bar .menu-content {
            display: none;
            position: absolute;
            top: 50px;
            left: 10px;
            background-color: #008080;
            color: white;
            padding: 10px;
            border-radius: 5px;
            box-shadow: 0px 8px 16px 0px rgba(0,0,0,0.2);
            z-index: 1001;
        }
        .header-bar .menu-content button {
            background-color: #008080;
            border: none;
            color: white;
            padding: 10px;
            width: 100%;
            text-align: left;
            cursor: pointer;
        }
        .title {
            flex-grow: 1;
            text-align: center;
        }
        .title h1 {
            color: white;
            margin: 0;
            font-size: 24px;
        }
        </style>
        """,
        unsafe_allow_html=True
    )
    
    # Header bar with menu and title
    st.markdown(
        """
        <div class="header-bar">
            <div class="menu" onclick="toggleMenu()">
                ☰
                <div class="menu-content" id="menuContent">
                    <button onclick="showHelp()">Help</button>
                    <div>About this app</div>
                    <div>This app is a PDF chatbot named WellnessBot designed to help you with health concerns by answering your questions based on the content of a PDF.</div>
                    <div>Author</div>
                    <div>Created by Raunak Singh Matharu, a Strategy Analyst with experience in data engineering and building AI-powered solutions.</div>
                </div>
            </div>
            <div class="title">
                <h1>WellnessBot</h1>
            </div>
        </div>
        <script>
        function toggleMenu() {
            var menuContent = document.getElementById('menuContent');
            if (menuContent.style.display === 'none' || menuContent.style.display === '') {
                menuContent.style.display = 'block';
            } else {
                menuContent.style.display = 'none';
            }
        }
        </script>
        """,
        unsafe_allow_html=True
    )

    genai.configure(api_key=GOOGLE_GENAI_API_KEY)

    if 'chat_history' not in st.session_state:
        st.session_state.chat_history = []

    # Chat agent introduction
    if not st.session_state.chat_history:
        st.session_state.chat_history.append({"role": "agent", "text": "Hello! I'm WellnessBot, your wellness advisor. How can I assist you today with your health concerns?"})

    # Display chat history
    st.markdown('<div style="padding-top: 60px;"></div>', unsafe_allow_html=True)
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

    # Restart button below user input
    if st.button("🔄 Restart Chat"):
        restart_chat()

if __name__ == "__main__":
    main()
