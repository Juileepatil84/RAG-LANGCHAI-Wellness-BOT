# WellnessBot

Welcome to WellnessBot! This project is a PDF chatbot designed to help you with health concerns by answering questions based on the content of a PDF.

## Table of Contents
- [Demo](#demo)
- [Features](#features)
- [Tech Stack](#tech-stack)
- [Setup Instructions](#setup-instructions)
- [How it Works](#how-it-works)
- [Future Improvements](#future-improvements)
- [Contributing](#contributing)
- [License](#license)

## Demo

Check out a video demo of WellnessBot on my [YouTube channel](https://youtu.be/SlAbk2DjRB0).

![Demo GIF](link_to_your_demo_gif)

## Features

- Ask health-related questions based on the content of a PDF.
- Provides comprehensive answers including remedies and suggestions.
- Interactive web interface built with Streamlit.

## Tech Stack

- [Streamlit](https://streamlit.io/): For creating the web interface.
- [Pinecone](https://www.pinecone.io/): For storing and retrieving context using vector databases.
- [Google Generative AI](https://cloud.google.com/ai/generative): For generating embeddings and responses.
- [LangChain](https://langchain.com/): For creating conversational chains.

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
   git clone https://github.com/Juileepatil84/RAG-LANGCHAI-Wellness-BOT.git

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

## Future Improvements
- Add support for more file formats.
- Improve the accuracy of responses with advanced NLP techniques.
- Add user authentication for personalized experiences.
