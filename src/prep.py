import os

from langchain_community.document_loaders import (CSVLoader)
from langchain_ollama import OllamaEmbeddings
from langchain_chroma import Chroma
from src.config_loader import load_config


config = load_config()


path = "data/cybersecurity.csv"

embedding = OllamaEmbeddings(model=config['llm']['embedding_model'])

def get_vector_store():
    print("Initializing vector store...")
    try:
        vectorStore = Chroma(
            collection_name=config['retriever']['collection_name'],
            embedding_function=embedding,
            persist_directory=config['retriever']['persist_directory']
        )
        print("Vector store initialized successfully.")
        return vectorStore
    except Exception as e:
        print(f"An error occurred while initializing the vector store: {e}")
        return None

def add_data_to_vector_store(chunks):
    print("Adding data to vector store...")
    try:
        vectorStore = get_vector_store()
        vectorStore.add_documents(chunks)
    except Exception as e:
        print(f"An error occurred while adding data to the vector store: {e}")
        return False
    print("Data added to vector store successfully.")
    

def load_and_add_data(path):
    if not os.path.exists(path):
        raise FileNotFoundError("The specified file does not exist.")
    print("Loading data...")
    loader = CSVLoader(path, encoding="utf-8")
    chunks = loader.load_and_split()
    print(f"Loaded {len(chunks)} chunks from the CSV file.")
    print(f"First 2 chunks {chunks[:2]} ")




