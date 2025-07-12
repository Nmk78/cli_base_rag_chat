from src.prep import get_vector_store

def get_retriever( k=5):
    """
    Function to get the retriever instance.
    This is used in the web API to handle queries.
    args:
        k (int): Number of documents to retrieve.
    """
    vector_store = get_vector_store()  # Number of documents to retrieve
    return vector_store.as_retriever(
        search_kwargs={
            "k" : k  # Number of documents to retrieve
        }
    )