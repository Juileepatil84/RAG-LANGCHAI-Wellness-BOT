# WellnessBot

Welcome to WellnessBot! This project is a PDF chatbot designed to help you with health concerns by answering questions based on the content of a PDF.

## Table of Contents
- [Demo](#demo)
- [Features](#features)
- [Tech Stack](#tech-stack)
- [Setup Instructions](#setup-instructions)
- [Usage](#usage)
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

## Setup and Installation

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

   Inside your project directory, create a .env file to store your GOOGLE_API_KEY.

6. **Create Requirements File:**

   Create a requirements.txt file to list all necessary Python packages.

7. **Install Required Packages:**
  ```cmd
     pip install -r requirements.txt
```  

8. **Create the Streamlit App File:**
   `
   Ensure app.py is set up and ready by this step as the dependencies are installed. You can also use app.py from cloned repository directly.

9. **Run the Application**
   ```
   streamlit run app.py

