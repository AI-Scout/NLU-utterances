import streamlit as st
from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate

st.header("🏠 AI Scout Solutions - Real Estate Description Generator Demo")

openai_api_key = st.sidebar.text_input("OpenAI API Key", type="password")

st.sidebar.subheader('About')
st.sidebar.caption('Created by Tony at AI Scout Solutions. For demo purposes only- this is not the final product.')

def real_estate_description(location, property_type, bedrooms, bathrooms, special_features, price):
    with st.spinner("Generating real estate description..."):
        # Instantiate LLM model
        llm = OpenAI(model_name="gpt-3.5-turbo", openai_api_key=openai_api_key)
        # Prompt
        template = "Generate a real estate description for a {property_type} located in {location}. It has {bedrooms} bedrooms and {bathrooms} bathrooms. Special features include: {special_features}. The listing price is {price}."
        prompt_query = template.format(
            property_type=property_type,
            location=location,
            bedrooms=bedrooms,
            bathrooms=bathrooms,
            special_features=special_features,
            price=price
        )
        # Run LLM model
        response = llm(prompt_query)
        # Print results
        return st.info(response)

with st.form("myform"):
    location = st.text_input("Enter the property location (e.g., city, neighborhood):", "")
    property_type = st.text_input("Enter the property type (e.g., house, apartment):", "")
    bedrooms = st.text_input("Enter the number of bedrooms:", "")
    bathrooms = st.text_input("Enter the number of bathrooms:", "")
    special_features = st.text_input("Enter any special features or highlights (e.g., pool, modern kitchen, view):", "")
    price = st.text_input("Enter the listing price or rental price:", "")
    submitted = st.form_submit_button("Submit")
    if not openai_api_key:
        st.info("Please add your OpenAI API key in the sidebar to continue.")
    elif submitted:
        real_estate_description(location, property_type, bedrooms, bathrooms, special_features, price)


hide_streamlit_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            </style>
            """
st.markdown(hide_streamlit_style, unsafe_allow_html=True) 
