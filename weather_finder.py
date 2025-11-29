
import requests

BASE_URL = "https://wttr.in/"

if __name__ == "__main__":
    locations_to_check = ["london", "Cherepovec", "SVO"]
    request_params = {
        "nTqu": "",
        "lang": "ru", 
        "m": "",
        "n": "",
    }
    
    for location in locations_to_check:
        url = f"{BASE_URL}{location}"
        
        try:
            response = requests.get(url, params=request_params)
            response.raise_for_status()
            print(f"Прогноз погоды:\n{response.text}")
            
        except (requests.exceptions.RequestException) as error:
            print(f"\nОшибка для локации {location}:\n{error}")
