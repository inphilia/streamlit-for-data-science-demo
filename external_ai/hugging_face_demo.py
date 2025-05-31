import streamlit as st
from transformers import pipeline
from openai import OpenAI

st.title('Hugging Face Transformers Demo')
text = st.text_input('Enter text to analyze:')

@st.cache_resource()
def get_model():
    return pipeline('sentiment-analysis')
model = get_model()

if text:
    result = model(text)
    st.write('Sentiment:', result[0]['label'])
    st.write('Confidence:', result[0]['score'])

st.title('OpenAI Version')
analyze_button = st.button('Analyze Text')
client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])
instructions_default = """You are a helpful sentiment analysis assistant. 
You always respond with the sentiment of the text you are given and 
the confidence of your sentiment analysis with a number between 0 and 1"""
instructions = st.text_area('Enter instructions for OpenAI model:',
                            value=instructions_default)

if analyze_button:
    response = client.responses.create(
        model = 'gpt-3.5-turbo',
        instructions = instructions,
        input = text
    )
    st.write(response.output_text)