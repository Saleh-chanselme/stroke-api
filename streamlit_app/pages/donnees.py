# streamlit_app/pages/donnees.py
import streamlit as st
from api import get_patients

def show(params):
    st.subheader("Données patients")
    try:
        data = get_patients(params)
        st.write(f"Nombre de patients : {len(data)}")
        st.dataframe(data)
    except Exception as e:
        st.error(f"Erreur lors de l'appel API : {e}")
