import pandas as pd
import numpy as np
import streamlit as st

st.set_page_config(layout="wide")

st.title("Data Analyzer and ML Suggestions App")

data_analyser_page = st.Page("Pages/data_analyser.py",title="Data Analyzer")

ml_suggestion_page = st.Page("Pages/ml_suggestions.py",title="ML Suggestion")

pg = st.navigation(pages=[data_analyser_page,ml_suggestion_page])