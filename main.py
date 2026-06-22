from fastapi import FastAPI, UploadFile, File
from langchain_community.document_loaders import PyPDFLoader
from langchain_openai import OpenAIEmbeddings, ChatOpenAI
from langchain_community.vectorstores import FAISS
from langchain.chains import ConversationalRetrievalChain
import shutil
import os

app = FastAPI()

vector_db = None

@app.post("/upload-pdf")
async def upload_pdf(file: UploadFile = File(...)):
    global vector_db
    file_path = f"data/{file.filename}"
    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)
    
    loader = PyPDFLoader(file_path)
    documents = loader.load()
    
    embeddings = OpenAIEmbeddings()
    vector_db = FAISS.from_documents(documents, embeddings)
    
    return {"message": "PDF processed successfully"}

@app.post("/ask")
async def ask_question(question: str):
    if not vector_db:
        return {"error": "Please upload a PDF first"}
    
    llm = ChatOpenAI(model="gpt-4")
    chain = ConversationalRetrievalChain.from_llm(llm, vector_db.as_retriever())
    
    response = chain.invoke({"question": question, "chat_history": []})
    return {"answer": response["answer"]}