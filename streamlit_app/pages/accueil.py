# streamlit_app/pages/accueil.py
import streamlit as st

def show():
    st.subheader("Bienvenue")
    st.markdown("""
    Cette application permet de visualiser les données liées aux accidents vasculaires cérébraux (AVC).

    **Objectifs :**
    - Visualiser les patients et leurs caractéristiques.
    - Explorer les statistiques liées aux AVC.
    - Fournir un outil d’aide à la décision médicale.
    """)
