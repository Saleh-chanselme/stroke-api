"""
Streamlit Dashboard AVC
=======================

Ce module représente le point d'entrée de l'application Streamlit pour la 
visualisation et l'analyse des données liées aux AVC (Accidents Vasculaires Cérébraux).

Il s'appuie sur plusieurs sous-modules :
    - `Pages/accueil.py` : page d'accueil et présentation générale du dashboard
    - `Pages/donnees.py` : affichage des données patients récupérées via l'API
    - `Pages/visualisations.py` : graphiques interactifs et visualisations
    - `Pages/statistiques.py` : statistiques descriptives et indicateurs globaux
    - `api.py` : fonctions pour interagir avec l'API FastAPI (`get_patients`, `get_stats`)

La navigation se fait à travers des onglets (`st.tabs`) qui appellent la fonction 
`show()` de chaque page.

Exemple d'utilisation :
    Lancer l'application avec la commande :

        streamlit run app.py
"""

import streamlit as st
from Pages import accueil, donnees, visualisations, statistiques
from api import get_patients, get_stats

# Configuration de la page
st.set_page_config(page_title="Dashboard AVC", layout="wide")

# Sidebar pour les filtres globaux
st.sidebar.header("Filtres patients")

#: Sélection du genre (Male, Female, Other)
gender = st.sidebar.selectbox("Genre", options=["", "Male", "Female", "Other"])

#: Filtrage selon la présence ou non d'AVC (0 = Non, 1 = Oui)
stroke = st.sidebar.selectbox("AVC", options=["", 0, 1])

#: Sélection de l'âge maximal des patients
max_age = st.sidebar.slider("Âge maximal", min_value=0, max_value=100, step=1)

#: Dictionnaire des paramètres envoyés à l'API
params = {}
if gender:
    params["gender"] = gender
if stroke != "":
    params["stroke"] = stroke
if max_age is not None:
    params["max_age"] = max_age


def main():
    """
    Point d'entrée principal de l'application Streamlit.

    Crée l'interface utilisateur avec 4 onglets :
        - Accueil : introduction et présentation du dashboard
        - Données : affichage des patients filtrés
        - Visualisations : graphiques interactifs
        - Statistiques : indicateurs globaux

    Les filtres définis dans la sidebar sont passés en paramètre aux fonctions 
    `donnees.show()` et `visualisations.show()`.

    Returns:
        None
    """
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


if __name__ == "__main__":
    main()