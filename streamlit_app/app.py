# streamlit_app/app.py

import streamlit as st
import pandas as pd
import requests
import plotly.express as px

API_URL = "http://127.0.0.1:8000"  # API FastAPI doit lancée

st.set_page_config(page_title="Dashboard AVC", layout="wide")

st.title("Stroke Prediction Dashboard")

# Création des onglets
Accueil, Données, Visualisations, Statistiques = st.tabs(["Accueil", "Données", "Visualisations", "Statistiques"])

# ------------------ ACCUEIL ------------------
with Accueil:
    st.subheader("Bienvenue")
    st.markdown("""
    Cette application permet de visualiser les données liées aux accidents vasculaires cérébraux (AVC).
    
    **Objectifs :**
    - Visualiser les patients et leurs caractéristiques.
    - Explorer les statistiques liées aux AVC.
    - Fournir un outil d’aide à la décision médicale.
    """)

# ------------------ DONNÉES ------------------
with Données:
    st.subheader("Données patients")
    # Widgets de filtrage
    gender = st.selectbox("Genre", options=["", "Male", "Female", "Other"])
    stroke = st.selectbox("AVC", options=["", 0, 1])
    max_age = st.slider("Âge maximal", min_value=0, max_value=100, step=1)

    # Construction des paramètres
    params = {}
    if gender: params["gender"] = gender
    if stroke != "": params["stroke"] = stroke
    if max_age: params["max_age"] = max_age

    # Appel API
    try:
        response = requests.get(f"{API_URL}/patients/", params=params)
        response.raise_for_status()
        data = pd.DataFrame(response.json())

        st.write(f"Nombre de patients : {len(data)}")
        st.dataframe(data)
    except Exception as e:
        st.error(f"Erreur lors de l'appel API : {e}")

# ------------------ VISUALISATIONS ------------------
with Visualisations:
    st.subheader("Visualisations")

    try:
        response = requests.get(f"{API_URL}/patients/")
        data = pd.DataFrame(response.json())

        col1, col2 = st.columns(2)

        with col1:
            st.markdown("### Répartition des âges")
            fig = px.histogram(data, x="age", nbins=30)
            st.plotly_chart(fig, use_container_width=True)

        with col2:
            st.markdown("### Répartition par genre")
            fig2 = px.pie(data, names="gender", title="Genre des patients")
            st.plotly_chart(fig2, use_container_width=True)
        
    except Exception as e:
        st.error(f"Erreur lors du chargement des visualisations : {e}")
        
# ------------------ STATISTIQUES ------------------
with Statistiques:
    st.subheader("Statistiques")
    try:
        response = requests.get(f"{API_URL}/stats/")
        stats = response.json()
        st.metric("Nombre total de patients", stats.get("total_patients", "N/A"))
        st.metric("Âge moyen", stats.get("mean_age", "N/A"))
        st.metric("Taux d’AVC (%)", stats.get("stroke_rate", "N/A"))
        st.metric("Répartition hommes/femmes", stats.get("gender_ratio", "N/A"))
    except Exception as e:
        st.error(f"Erreur lors de l'appel de la route /stats/ : {e}")
