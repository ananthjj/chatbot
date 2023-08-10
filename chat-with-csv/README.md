# This is a simple streamlit app where you can upload a csv file and ask related questions.

## Setup 
1. You need Python installed. If not installed, install if from this [link](https://www.python.org/downloads/)

2. Create virtual environment:
```
python3 -m venv .venv && source .venv/bin/activate
```

3. Install packages from requirements.txt:
```
pip install -r requirements.txt
```

4. Update .streamlit/secrets.toml with your OpenAI API key

5. Run streamlit app:
```
streamlit run app.py
```
After running the streamlit command, able to access the app at http://localhost:8501/. Upload the CSV file.

6. Once finished type Ctrl+C in your terminal to stop the streamlit app and
   deactivate the virtual environment by running:
```
deactivate
```