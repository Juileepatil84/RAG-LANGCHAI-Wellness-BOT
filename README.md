# WellnessBot

Welcome to WellnessBot! This project is a PDF chatbot designed to help you with health concerns by answering questions based on the content of a PDF.

## Table of Contents
- [Demo](#demo)
- [Features](#features)
- [Tech Stack](#tech-stack)
- [Setup Instructions](#setup-instructions)
- [How it Works](#how-it-works)
- [Future Improvements](#future-improvements)
- [Conclusion](#conclusion)
## Demo

Check out a video demo of WellnessBot on my [YouTube channel](https://youtu.be/SlAbk2DjRB0).


## Features

- Ask health-related questions based on the content of a PDF.
- Provides comprehensive answers including remedies and suggestions.
- Interactive web interface built with Streamlit.

## Tech Stack

- [Streamlit](https://streamlit.io/): For creating the web interface.
- [Pinecone](https://www.pinecone.io/): For storing and retrieving context using vector databases.
- [Google Generative AI](https://cloud.google.com/ai/generative): For generating embeddings and responses.
- [LangChain](https://langchain.com/): For creating conversational chains.

## Mock Data Generation: prompt used to get the data
```chatGPT
Give me a famous health and wellness book in PDF which has home remedies to cure acute diseases.
Pages should be not more that 25. 

```

## Setup Instructions

### Prerequisites
- Python 3.8 or higher
- Anaconda (recommended for environment management)
- Gemini API Key - [Link to create API Key](https://ai.google.dev/gemini-api/docs/api-key)
- [Pinecone Account](https://www.pinecone.io/)
- [Google Cloud Account](https://cloud.google.com/)

### Installation Steps
1. **Clone the Repository:**
   ```cmd
   git clone https://github.com/Juileepatil84/RAG-LANGCHAIN-Wellness-BOT.git

2. **Open the Cloned Folder in Visual Studio Code**
   
   Navigate to the project directory in VS Code.

4. **Set Up Conda Environment:**
   ```
   conda create -n ven python=3.12.4 -y
   
   conda activate venv

4. **Create a .env File:**

   Inside your project directory, create a .env file to store your GOOGLE_API_KEY and PINECONE_API_KEY.

6. **Create Requirements File:**

   Create a requirements.txt file to list all necessary Python packages.

7. **Install Required Packages:**
  ```cmd
     pip install -r requirements.txt
```  

8. **Create the vector datapase creation and Streamlit App File:**
   `
   Ensure app.py and vdb.py is set up and ready by this step as the dependencies are installed. You can also use app.py and vdb.py from cloned repository directly.
   vdb.py will create index in pinecone vector database if it doesnt exist and upload embedding and chunks from pdf.

   Make sure you run vdb.py to create db and load data before runnig streamlit app. 

10. **Run the Application**
   ```
   ## Create database 
   Python vdb.py
   ## Run the web application
   streamlit run app.py
   ```
##### Open your web browser and go to http://localhost:8501

## How it Works
WellnessBot uses Retrieval-Augmented Generation (RAG) to provide accurate and contextually rich answers to health-related questions based on the content of a PDF. Here’s a brief overview of the process:

- User Input: The user asks a question via the Streamlit web interface.
- Embedding Generation: The question is converted into embeddings using Google Generative AI.
- Context Retrieval: Pinecone searches for relevant context in the PDF based on the embeddings.
- Response Generation: LangChain uses the retrieved context to generate a comprehensive answer.
- Display: The answer is displayed on the web interface.

### Code Explanation
app.py:
Sets up the Streamlit web interface.
Handles user inputs and displays the chat history.
Integrates with Pinecone and Google Generative AI to process queries and generate responses.

vdb.py:
Extracts text from PDF files.
Chunks the extracted text for efficient processing.
Generates embeddings for the text chunks.
Upserts the embeddings into Pinecone for context retrieval.

requirements.txt:
Lists all the dependencies required for the project.

## Report

##### Approach Taken
WellnessBot was developed with the goal of providing accurate and contextually rich answers to health-related questions based on the content of a PDF. The approach involved integrating several powerful technologies and libraries to build a robust PDF chatbot.

##### Challenges Faced
Deciding the Chunk Size and Chunk Overlap:
One of the primary challenges was to determine the optimal chunk size and chunk overlap for processing the PDF content. The goal was to ensure that the extracted text chunks were neither too large nor too small, as both extremes could affect the accuracy of the context retrieval and the quality of the generated responses.

Chunk Size: If the chunks were too large, important details might get buried within large paragraphs, making it difficult for the model to retrieve the most relevant context. On the other hand, if the chunks were too small, the model might miss out on important contextual information that spans multiple chunks.

Chunk Overlap: Overlapping chunks are essential to ensure that the context is preserved across boundaries. However, too much overlap could lead to redundant data processing, while too little overlap might result in the loss of critical information that falls between chunks.

To address this, extensive experimentation was conducted to find the balance. The final configuration involved selecting a chunk size that captured sufficient context without being overwhelmingly large, and an overlap size that ensured continuity of information without excessive redundancy.

##### How They Were Overcome
Experimentation and Testing:
Several iterations of experimentation were carried out with different chunk sizes and overlap values. Each iteration involved testing the system's ability to retrieve relevant context and generate accurate responses.

Evaluation Metrics: Metrics such as retrieval accuracy score, response relevance, and user satisfaction were used to evaluate the effectiveness of different configurations.
User Feedback: Feedback from initial users was invaluable in refining the chunking strategy. Their insights helped identify cases where the system performed well and areas that needed improvement.

Balancing Chunk Size and Overlap: Below are methods to balance Chunk Size and Overlap

Optimal Chunk Size: After multiple rounds of testing, an optimal chunk size was determined that balanced detail and manageability. This size was large enough to provide comprehensive context but small enough to be efficiently processed.

Effective Overlap: The chunk overlap was fine-tuned to ensure that important information spanning chunk boundaries was not lost. The overlap was set to a size that maintained context continuity without introducing significant redundancy.
Leveraging Pinecone and LangChain:

Pinecone: The vector database capabilities of Pinecone were leveraged to store and retrieve context efficiently. The ability to query Pinecone with embeddings allowed for quick and accurate context retrieval.
LangChain: LangChain's capabilities were utilized to create conversational chains that could effectively use the retrieved context to generate coherent and relevant responses.


## Future Improvements
- Add support for more file formats.
- Improve the accuracy of responses with advanced NLP techniques.
- Add user authentication for personalized experiences.

## Conclusion
The development of WellnessBot involved overcoming significant challenges related to text chunking. Through careful experimentation and user feedback, an optimal balance was achieved, resulting in a robust system capable of providing accurate and contextually rich health advice based on PDF content.

