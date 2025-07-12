rag_chat_bot/
├── app.py                 # Main entry point for the chatbot application (CLI interface)
├── config.yaml            # Configuration file for model and app settings
├── requirements.txt       # List of required Python packages

├── chroma_store/          # Directory for Chroma vector database storage
│   └── chroma.sqlite3     # Chroma vector DB file

├── data/                  # Directory for data files used for RAG
│   └── cybersecurity.csv  # Example data file (knowledge base)

├── src/                   # Source code for core logic and utilities
│   ├── config_loader.py   # Loads and parses configuration from config.yaml
│   ├── prep.py            # Prepares and loads the vector store
│   ├── rag_chain.py       # Builds the RAG (Retrieval-Augmented Generation) chain
│   └── __pycache__/       # Python bytecode cache (auto-generated)



