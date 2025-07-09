from langchain.chains import RetrievalQA
from langchain_core.language_models import BaseLLM
from langchain_core.retrievers import BaseRetriever

def build_rag_chain(llm: BaseLLM, retriever: BaseRetriever):
    return RetrievalQA.from_chain_type(
        llm=llm,
        retriever=retriever,
    )
