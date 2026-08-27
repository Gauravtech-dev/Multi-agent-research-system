from langchain_chroma import Chroma

from rag.embeddings import get_embeddings


def create_vector_store(documents):
    embeddings = get_embeddings()

    vector_store = Chroma.from_documents(
        documents=documents,
        embedding=embeddings,
        collection_name="research_documents"
    )

    return vector_store