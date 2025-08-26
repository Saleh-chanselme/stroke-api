# streamlit_app/api.py
import requests
import pandas as pd
import streamlit as st

API_URL = "http://127.0.0.1:8000"

@st.cache_data
def get_patients(params=None):
    """Récupère les données des patients depuis l'API."""
    response = requests.get(f"{API_URL}/patients/", params=params)
    response.raise_for_status()
    return pd.DataFrame(response.json())

@st.cache_data
def get_stats():
    """Récupère les statistiques globales depuis l'API."""
    response = requests.get(f"{API_URL}/stats/")
    response.raise_for_status()
    return response.json()
