# streamlit_app/pages/visualisations.py
import streamlit as st
import plotly.express as px
from api import get_patients

def show(params):
    st.subheader("Visualisations")
    try:
        data = get_patients(params)
        if data.empty:
            st.info("Aucune donnée à afficher.")
            return

        col1, col2, col3 = st.columns(3)

        with col1:
            st.markdown("### Répartition des âges")
            fig = px.histogram(data, x="age", nbins=30, title="Distribution des âges")
            st.plotly_chart(fig, use_container_width=True)
            st.markdown("La majorité des patients sont dans la tranche 30-60 ans.")

        with col2:
            st.markdown("### Répartition par genre")
            fig2 = px.pie(data, names="gender", title="Genre des patients")
            st.plotly_chart(fig2, use_container_width=True)
            st.markdown("Le genre féminin est légèrement plus représenté.")

        with col3:
            st.markdown("### Répartition AVC par genre")
            stroke_gender = data[data['stroke'] == 1]['gender'].value_counts()
            fig3 = px.pie(
                names=stroke_gender.index,
                values=stroke_gender.values,
                title="Patients ayant eu un AVC par genre"
            )
            st.plotly_chart(fig3, use_container_width=True)

        # Pie chart Fumeurs vs Non-fumeurs
        st.markdown("### Fumeurs vs Non-fumeurs parmi les patients ayant eu un AVC")
        stroke_df = data[data['stroke'] == 1]
        stroke_smoking_counts = stroke_df['smoking_status'].apply(
            lambda x: 'Fumeur' if x != 'never smoked' else 'Non-fumeur'
        ).value_counts()

        fig_smoking = px.pie(
            names=stroke_smoking_counts.index,
            values=stroke_smoking_counts.values,
            title="Fumeurs vs Non-fumeurs (AVC)"
        )
        st.plotly_chart(fig_smoking, use_container_width=True)

    except Exception as e:
        st.error(f"Erreur lors du chargement des visualisations : {e}")
