from agents import build_reader_agent, writer_chain, critic_chain
from tools import web_search, split_text
from rag.vector_store import create_vector_store
from rag.retriever import get_retriever


def run_research_pipeline(topic: str) -> dict:

    state = {}

    # step 1 - web search
    print("\n" + " =" * 50)
    print("step 1 - web search is working ...")
    print("=" * 50)

    search_result = web_search.invoke({
        "query": topic
    })

    state["search_results"] = search_result

    print("\n search result \n", state["search_results"])

    # step 2 - reader agent
    print("\n" + " =" * 50)
    print("step 2 - Reader agent is scraping top resources ...")
    print("=" * 50)

    reader_agent = build_reader_agent()

    reader_result = reader_agent.invoke({
        "messages": [
            (
                "user",
                f"Based on the following search results about '{topic}', "
                f"pick the most relevant URL and scrape it for deeper content.\n\n"
                f"Search Results:\n{state['search_results'][:3000]}"
            )
        ]
    })

    reader_content = reader_result["messages"][-1].content

    if isinstance(reader_content, list):
        state["scraped_content"] = "\n".join(
            item.get("text", "") if isinstance(item, dict) else str(item)
            for item in reader_content
        )
    else:
        state["scraped_content"] = str(reader_content)

    print("\nscraped content: \n", state["scraped_content"])

    # step 3 - RAG
    print("\n" + " =" * 50)
    print("step 3 - RAG is creating and retrieving relevant context ...")
    print("=" * 50)

    documents = split_text(state["scraped_content"])

    vector_store = create_vector_store(documents)

    retriever = get_retriever(vector_store)

    relevant_docs = retriever.invoke(topic)

    retrieved_content = "\n\n".join(
        doc.page_content for doc in relevant_docs
    )

    state["retrieved_content"] = retrieved_content

    print("\n retrieved content: \n", state["retrieved_content"])

    # step 4 - writer chain
    print("\n" + " =" * 50)
    print("step 4 - Writer is drafting the report ...")
    print("=" * 50)

    research_combined = (
        f"SEARCH RESULTS : \n {state['search_results']} \n\n"
        f"RETRIEVED RESEARCH CONTEXT : \n {state['retrieved_content']}"
    )

    state["report"] = writer_chain.invoke({
        "topic": topic,
        "research": research_combined
    })

    print("\n Final Report\n", state["report"])

    # step 5 - critic report
    print("\n" + " =" * 50)
    print("step 5 - critic is reviewing the report ")
    print("=" * 50)

    state["feedback"] = critic_chain.invoke({
        "report": state["report"]
    })

    print("\n critic report \n", state["feedback"])

    return state


if __name__ == "__main__":
    topic = input("\n Enter a research topic : ")
    run_research_pipeline(topic)