from typing import Optional
import pandas as pd

# Chargement des données (une fois)
stroke_data_df = pd.read_parquet("stroke_api/data/healthcare_stroke.parquet")
# Tester l'app avec :

# poetry run fastapi dev stroke_api/main.py

#http://127.0.0.1:8000/docs : utiliser la fonctionnalité Try it out pour tester les routes

# Ajout des fonctions de filtrage des données cf notebook 1
def filter_patient(
    gender: Optional[str] = None,
    stroke: Optional[int] = None,
    max_age: Optional[int] = None
    ):
    
    df = stroke_data_df.copy()

    if gender is not None:
        df = df.loc[df["gender"] == gender]

    if stroke is not None:
        df = df.loc[df["stroke"] == stroke]
    
    if max_age is not None:
        df = df.loc[df["age"] <= max_age]

    #print(f"[DEBUG] Filtrage : gender={gender}, stroke={stroke}, max_age={max_age}")
    #print(f"[DEBUG] Données initiales : {df.shape[0]} lignes")

    #print(f"[DEBUG] Données filtrées : {df_filtered.shape[0]} lignes")    

    return df.to_dict("records")

# Ensuite faire appel à ces fonctions dans le fichier api.py où sont définies les routes.

# Ajouter les fonctions de filtrage pour les autres routes.



