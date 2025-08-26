import requests
import pandas as pd

API_URL = "http://127.0.0.1:8000"

def get_patients(params: dict = None) -> pd.DataFrame:
    """
    Récupère les patients depuis l'API FastAPI.

    Args:
        params (dict, optional): Paramètres de filtrage (ex: {"gender": "Male", "stroke": 1}).

    Returns:
        pd.DataFrame: Tableau des patients.

    Raises:
        requests.exceptions.RequestException: Si l'appel API échoue.
    """
    response = requests.get(f"{API_URL}/patients/", params=params or {})
    response.raise_for_status()
    return pd.DataFrame(response.json())
