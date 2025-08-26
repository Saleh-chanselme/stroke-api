# streamlit_app/pages/statistiques.py
import streamlit as st
from api import get_stats

def show():
    st.subheader("Statistiques globales")
    try:
        stats = get_stats()
        st.metric("Nombre total de patients", stats.get("total_patients", "N/A"))
        st.metric("Âge moyen", stats.get("mean_age", "N/A"))
        st.metric("Taux d’AVC (%)", stats.get("stroke_rate", "N/A"))
        st.metric("Répartition hommes/femmes", stats.get("gender_ratio", "N/A"))
    except Exception as e:
        st.error(f"Erreur lors de l'appel API /stats/ : {e}")
