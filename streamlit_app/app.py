import streamlit as st
from Pages import accueil, donnees, visualisations, statistiques
from api import get_patients, get_stats

# Configuration de la page
st.set_page_config(page_title="Dashboard AVC", layout="wide")

# Sidebar pour les filtres globaux
st.sidebar.header("Filtres patients")
gender = st.sidebar.selectbox("Genre", options=["", "Male", "Female", "Other"])
stroke = st.sidebar.selectbox("AVC", options=["", 0, 1])
max_age = st.sidebar.slider("Âge maximal", min_value=0, max_value=100, step=1)

params = {}
if gender: params["gender"] = gender
if stroke != "": params["stroke"] = stroke
if max_age is not None: params["max_age"] = max_age

# Création des onglets
Accueil, Données, Visualisations, Statistiques = st.tabs(
    ["Accueil", "Données", "Visualisations", "Statistiques"]
)

# Affichage de chaque onglet via sa fonction show()
with Accueil: 
    accueil.show() 
with Données:
    donnees.show(params)

with Visualisations:
    visualisations.show(params)

with Statistiques:
    statistiques.show()
