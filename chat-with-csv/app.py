'''
To run this app, run the below command in your terminal:
* Create virtual environment: python3 -m venv .venv && source .venv/bin/activate
* Install packages from requirements.txt: pip install -r requirements.txt
* Update .streamlit/secrets.toml with your OpenAI API key
* Run streamlit app: streamlit run app.py
* Once finished type Ctrl+C in your terminal to stop the streamlit app and
  deactivate the virtual environment by running: deactivate
'''
import streamlit as st

from utils import get_answer_csv

st.header("Chat with data stored in CSV")
uploaded_file = st.file_uploader("Upload a csv file", type=["csv"])

if uploaded_file is not None:
    query = st.text_area("Ask any question related to the data")
    button = st.button("Submit")
    if button:
        st.write(get_answer_csv(uploaded_file, query))
