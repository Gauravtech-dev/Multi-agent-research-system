import streamlit as st
from pipeline import run_research_pipeline


st.set_page_config(
    page_title="Multi-Agent Research System",
    page_icon="🔎",
    layout="wide"
)

st.markdown("""
<style>
    .main-title {
        font-size: 42px;
        font-weight: 700;
        margin-bottom: 5px;
    }

    .subtitle {
        font-size: 18px;
        opacity: 0.75;
        margin-bottom: 30px;
    }

    .section-title {
        font-size: 25px;
        font-weight: 600;
        margin-top: 25px;
    }

    .info-box {
        padding: 18px;
        border-radius: 12px;
        border: 1px solid rgba(128,128,128,0.25);
        margin-bottom: 20px;
    }
</style>
""", unsafe_allow_html=True)


st.markdown(
    '<div class="main-title">Multi-Agent Research System</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="subtitle">Web Search • Multi-Agent Workflow • RAG • Gemini • Critic</div>',
    unsafe_allow_html=True
)


st.markdown(
    '<div class="info-box">'
    'Enter a research topic and let the agents search, retrieve, '
    'analyze and generate a structured research report.'
    '</div>',
    unsafe_allow_html=True
)


st.markdown(
    '<div class="section-title">Research Topic</div>',
    unsafe_allow_html=True
)

topic = st.text_input(
    "Research Topic",
    placeholder="e.g. Artificial Intelligence in Healthcare",
    label_visibility="collapsed"
)


if st.button("Generate Research Report", use_container_width=True):

    if not topic.strip():
        st.warning("Please enter a research topic.")

    else:

        with st.spinner("Research agents are working..."):

            result = run_research_pipeline(topic)

        st.success("Research completed successfully.")

        st.markdown(
            '<div class="section-title">Research Report</div>',
            unsafe_allow_html=True
        )

        st.markdown(result["report"])

        st.markdown(
            '<div class="section-title">Critic Evaluation</div>',
            unsafe_allow_html=True
        )

        st.markdown(result["feedback"])