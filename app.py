from src.config_loader import load_config

config = load_config()

from langchain_ollama import OllamaLLM
from langchain_chroma import Chroma
from src.rag_chain import build_rag_chain
from src.prep import get_vector_store

# Initialize LLM
llm = OllamaLLM(model=config['llm']['model'], temperature=config['llm']['temperature'], max_tokens=config['llm']['max_tokens'])

# Load vector DB retriever
vectorStore = get_vector_store()
retriever = vectorStore.as_retriever(
    search_kwargs={
        "k": 5,  # Number of documents to retrieve
    }
)

# Build the chain
qa_chain = build_rag_chain(llm, retriever)

while True:
    try:
        query = input("\n❓ Ask a question (or type 'exit' to quit):\n> ")
        if query.lower() in ["exit", "quit"]:
            print("👋 Goodbye!")
            break

        response = qa_chain.invoke(query)
        # print(response)
        print("\n💬 Answer:\n" + response['result'])

    except KeyboardInterrupt:
        print("\n👋 Exiting...")
        break
    except Exception as e:
        print(f"\n⚠️ Error: {e}")
