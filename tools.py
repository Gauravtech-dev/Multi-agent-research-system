from langchain.tools import tool
import requests
from bs4 import BeautifulSoup
from ddgs import DDGS
from langchain_text_splitters import RecursiveCharacterTextSplitter


@tool
def web_search(query: str) -> str:
    """Search the web for recent and reliable information on a topic.
    Returns Titles, URLs and snippets.
    """

    try:
        results = DDGS().text(
            query,
            max_results=5
        )

        out = []

        for r in results:
            out.append(
                f"Title: {r.get('title', '')}\n"
                f"URL: {r.get('href', '')}\n"
                f"Snippet: {r.get('body', '')[:300]}\n"
            )

        return "\n----\n".join(out)

    except Exception as e:
        return f"Could not search the web: {str(e)}"


@tool
def scrape_url(url: str) -> str:
    """Scrape and return clean text content from a given URL for deeper reading."""

    try:
        resp = requests.get(
            url,
            timeout=8,
            headers={"User-Agent": "Mozilla/5.0"}
        )

        resp.raise_for_status()

        soup = BeautifulSoup(
            resp.text,
            "html.parser"
        )

        for tag in soup(["script", "style", "nav", "footer"]):
            tag.decompose()

        return soup.get_text(
            separator=" ",
            strip=True
        )[:3000]

    except Exception as e:
        return f"Could not scrape URL: {str(e)}"


def split_text(text: str):
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000,
        chunk_overlap=200
    )

    return splitter.create_documents([text])