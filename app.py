from src.config_loader import load_config

config = load_config()

from langchain_ollama import OllamaLLM
from src.rag_chain import build_rag_chain
from src.prep import get_vector_store
from src.ollama_instance import get_llm
from src.retriever import get_retriever

# Initialize LLM
llm = get_llm()

# Load vector DB retriever
vectorStore = get_vector_store()
retriever = get_retriever()

# Build the chain
qa_chain = build_rag_chain(llm, retriever)

while True:
    try:
        query = input("\n❓ Ask a question (or type 'exit' to quit):\n> ")
        if query.lower() in ["exit", "quit"]:
            print("👋 Goodbye!")
            break

        print("\n💬 Answer:")
        try:
            for chunk in qa_chain.stream(query):
                print(chunk.get("result", ""), end="", flush=True)
            print()
            # response = qa_chain.invoke(query)
            # print(response["result"])
        except Exception as e:
            print(f"\n⚠️ Streaming failed: {e}")
            print("🔁 Trying without streaming...")
            response = qa_chain.invoke(query)
            print(response["result"])



    except KeyboardInterrupt:
        print("\n👋 Exiting...")
        break
    except Exception as e:
        print(f"\n⚠️ Error: {e}")


# from src.config_loader import load_config

# config = load_config()

# from langchain_ollama import OllamaLLM
# from langchain_chroma import Chroma
# from src.rag_chain import build_rag_chain
# from src.prep import get_vector_store

# # Initialize LLM
# llm = OllamaLLM(model=config['llm']['model'], temperature=config['llm']['temperature'], max_tokens=config['llm']['max_tokens'])

# # Load vector DB retriever
# vectorStore = get_vector_store()
# retriever = vectorStore.as_retriever(
#     search_kwargs={
#         "k": 5,  # Number of documents to retrieve
#     }
# )

# # Build the chain
# qa_chain = build_rag_chain(llm, retriever)

# while True:
#     try:
#         query = input("\n❓ Ask a question (or type 'exit' to quit):\n> ")
#         if query.lower() in ["exit", "quit"]:
#             print("👋 Goodbye!")
#             break

#         response = qa_chain.invoke(query)
#         # print(response)
#         print("\n💬 Answer:\n" + response['result'])

#     except KeyboardInterrupt:
#         print("\n👋 Exiting...")
#         break
#     except Exception as e:
#         print(f"\n⚠️ Error: {e}")