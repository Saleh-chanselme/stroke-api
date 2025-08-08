from http.client import HTTPException
from fastapi import APIRouter
from stroke_api import filters

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
#@router.get("/patients/{patient_id}")
    # Gérer le cas où l'id de patient passé en paramètre n'existe pas

#def get_patient_by_id(patient_id: int):



# TODO Ajout de la route stats








