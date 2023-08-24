import streamlit as st
from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate

st.header("AI Scout Solutions- NLU Utterance Generator")

openai_api_key = st.sidebar.text_input("OpenAI API Key", type="password")

st.sidebar.subheader('About')
st.sidebar.caption('Created by Tony at AI Scout Solutions.')

def utterance_gen(question, intents, example):
    with st.spinner("Generating utterances..."):
        # Instantiate LLM model
        llm = OpenAI(model_name="gpt-3.5-turbo", openai_api_key=openai_api_key)
        # Prompt
        template = '''I have several intents setup for this question:

                    {question}

                    The intents are: {intents}


                    Generate 50 variations in which a user may respond for each intent. Keep in mind this is a chatbot, so users may not write in full sentences or use correct spelling/grammar at all times. For example, a user may say, "{example}"'''
        prompt_query = template.format(
            question=question,
            intents=intents,
            example=example,
        )
        # Run LLM model
        response = llm(prompt_query)
        # Print results
        return st.info(response)

with st.form("myform"):
    question = st.text_input("Please enter the question:", "")
    intents = st.text_input("Please enter all intents for this question, comma-separated:", "")
    example = st.text_input("Please enter an example utterance for ONE of the intents:", "")
    submitted = st.form_submit_button("Submit")
    if not openai_api_key:
        st.info("Please add your OpenAI API key in the sidebar to continue.")
    elif submitted:
        utterance_gen(question, intents, example)

hide_streamlit_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            </style>
            """
st.markdown(hide_streamlit_style, unsafe_allow_html=True) 
