Multi-Agent Research System

An AI-powered research assistant that automates web research, source reading, RAG-based retrieval, report generation, and report evaluation.

Features

Web search with DuckDuckGo (DDGS)
Reader Agent for deeper source analysis
Web scraping with BeautifulSoup
RAG-based semantic retrieval
Embeddings and vector store
Gemini-powered research report generation
Automated Critic evaluation
Streamlit web interface
Live deployment

Workflow

Research Topic
      ↓
DDGS Web Search
      ↓
Reader Agent
      ↓
Web Scraping
      ↓
Text Chunking
      ↓
Embeddings + Vector Store
      ↓
Relevant Context Retrieval
      ↓
Gemini Writer
      ↓
Research Report
      ↓
Gemini Critic
      ↓
Final Evaluation

Tech Stack

Python • LangChain • Google Gemini • DDGS • BeautifulSoup • Sentence Transformers • ChromaDB • Streamlit

Project Structure

Multi-agent-research-system/
├── agents.py
├── tools.py
├── pipeline.py
├── app.py
├── requirements.txt
├── .env
├── .gitignore
└── rag/
    ├── __init__.py
    ├── embeddings.py
    ├── vector_store.py
    └── retriever.py

Run Locally

pip install -r requirements.txt
streamlit run app.py
Environment Setup

Live Demo

https://multi-agent-research-system-wx6pwujzhfntqh8aa8rpqm.streamlit.app/

Future Improvements

Multi-source retrieval
Stronger source citations
Persistent vector storage
Report export
Improved retrieval and evaluation

