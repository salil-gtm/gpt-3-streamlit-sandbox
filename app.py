import time
import requests
import streamlit as st
from footer_utils import image, link, layout, footer

st.set_page_config(layout='wide',
                   initial_sidebar_state='collapsed',
                   page_icon="favicon.png",
                   page_title="GPT-3 Streamlit Sandbox ⚒️")

@st.cache(allow_output_mutation=True)
def Pageviews():
    return []

st.title('🔮 GPT-3 Streamlit Sandbox 🛠️')
st.info("Setup to quickly check use case feasibility on OpenAI's GPT-3!")

left_column, right_column = st.beta_columns(2)

with left_column:
    st.header("Challenge GPT3")
    prompt = st.text_input('Enter Prompt')
    if st.button('Send', key='challenge'):
        if prompt is not '':
            with st.spinner("Reaching OpenAI's Servers..."):
                time.sleep(3.5)
                response = requests.post(f"http://127.0.0.1:8000/ask_gpt", json={'prompt':prompt})
                st.success(response.text)
        else:
            st.error("Prompt Incomplete :/")

with right_column:
    st.header("Help GPT3")
    example_input = st.text_input('Enter Example Input')
    example_output = st.text_input('Enter Example Ouput')
    if st.button('Send', key='help'):
        if example_input is not '' and example_output is not '':
            with st.spinner("Reaching OpenAI's Servers..."):
                time.sleep(3.5)
                response = requests.post(f"http://127.0.0.1:8000/add_example", json={'input':example_input, 'output':example_output})
                st.success(response.text)
        else:
            st.error("Example Incomplete :/")

pageviews=Pageviews()
pageviews.append('dummy')
pg_views = len(pageviews)
footer(pg_views)
