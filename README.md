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

## Setup Instructions

### Prerequisites

- Python 3.12.4+
- [Pinecone Account](https://www.pinecone.io/)
- [Google Cloud Account](https://cloud.google.com/)

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/YOUR_GITHUB_USERNAME/WellnessBot.git
   cd WellnessBot
