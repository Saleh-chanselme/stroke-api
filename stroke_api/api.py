from http.client import HTTPException
from fastapi import APIRouter
from stroke_api import filters
from stroke_api.filters import get_patient_by_id

router = APIRouter()

@router.get("/")
def read_root():
    return {"message": "Bienvenue sur l'API Stroke Prediction !"}

# TODO décommenter et compléter
@router.get("/patients/")
def get_patients(
    gender: str = None, 
    stroke: int = None, 
    max_age: int = None
    ):
    
    try:
        filtered_df = filters.filter_patient( gender=gender, stroke=stroke, max_age=max_age)
        return filtered_df
    except Exception:
        raise HTTPException(status_code=404, detail="HTTP Error is occurred")

# TODO décommenter et compléter
@router.get("/patients/{patient_id}")
    # Gérer le cas où l'id de patient passé en paramètre n'existe pas
def get_patient_by_id(patient_id: int):
    patient = filters.get_patient_by_id(patient_id)
    if patient:
        return patient
    else:
        raise HTTPException(status_code=404, detail="Patient non trouvé")    

# TODO Ajout de la route stats
@router.get("/stats/")
def get_stats():
    try:
        stats = filters.get_statistics()
        return stats
    except Exception:
        raise HTTPException(status_code=500, detail="Erreur lors du calcul des statistiques")












