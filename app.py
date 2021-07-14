import streamlit as st
from footer_utils import image, link, layout, footer

st.set_page_config(layout='wide',
                   initial_sidebar_state='collapsed',
                   page_icon="https://beta.openai.com/favicon.ico",
                   page_title="GPT-3 Streamlit Sandbox ⚒️")

@st.cache(allow_output_mutation=True)
def Pageviews():
    return []

st.title('GPT-3 Streamlit Sandbox 🛠️')
st.info("Low Code setup to quickly check use case feasibility on OpenAI's GPT-3!")

left_column, right_column = st.beta_columns(2)

with left_column:
    st.header("Challenge GPT3")
    prompt = st.text_input('Enter Prompt')

with right_column:
    st.header("Help GPT3")
    example_input = st.text_input('Enter Example Input')
    example_output = st.text_input('Enter Example Ouput')

pageviews=Pageviews()
pageviews.append('dummy')
pg_views = len(pageviews)
footer(pg_views)
