#  FastAPI + LangChain RAG Project

This project is a lightweight **FastAPI** backend integrated with **LangChain** to build a Retrieval-Augmented Generation (RAG) system using vector search with **FAISS**.

It is designed to allow building AI-powered applications such as chatbots that can read and query PDF documents or custom datasets.

---

## 📁 Project Structure
├── main.py
├── requirements.txt
├── Dockerfile
├── .env
└── README.md

---

## ⚙️ Installation

### 1. Clone the repository

```bash
git clone https://github.com/your-username/your-repo-name.git
cd your-repo-name

2. Create virtual environment (optional)
python -m venv venv
source venv/bin/activate  # Linux / Mac
venv\Scripts\activate     # Windows

```
## 3. Install dependencies
pip install -r requirements.txt


## 📄 requirements.txt
fastapi
uvicorn
langchain
langchain-community
langchain-openai
faiss-cpu
pypdf
python-dotenv


## Run the Project
Using Uvicorn
uvicorn main:app --reload

Then open:

http://127.0.0.1:8000

## 🐳 Docker Setup
Dockerfile
FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY main.py .

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]

Build Docker Image
docker build -t fastapi-langchain-rag .


## Run Docker Container
docker run -p 8000:8000 fastapi-langchain-rag


## 🔐 Environment Variables

Create a .env file:

OPENAI_API_KEY=your_api_key_here


## 📡 API Example

Once running, access:

GET http://localhost:8000

## 🧠 Project Idea

This project can be extended to:

AI Chatbot over PDF files
RAG (Retrieval-Augmented Generation) system
Knowledge base question answering
Document search engine using embeddings
✨ Future Improvements
Add authentication (JWT)
Add multiple document upload support
Improve vector database (Pinecone / Weaviate)
Add streaming responses
Deploy to cloud (AWS / Render / Docker Hub)