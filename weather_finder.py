import requests

BASE_URL = "https://wttr.in/"


def fetch_single_weather(location, params): 
    url = f"{BASE_URL}{location}"

    try:
        response = requests.get(url, params=params)
        response.raise_for_status()
        return response.text
    except requests.exceptions.HTTPError as http_error:
        return f"HTTP ошибка: {http_error}"
    except requests.exceptions.ConnectionError as connection_error:
        return f"Ошибка подключения: {connection_error}"
    except requests.exceptions.Timeout as timeout_error:
        return f"Таймаут: {timeout_error}"
    except requests.exceptions.RequestException as request_error:
        return f"Произошла ошибка: {request_error}"


def print_weather_info(location, result):
    error_names = ["HTTP ошибка", "Ошибка подключения", "Таймаут", "Произошла ошибка"]
    
    if any(result.startswith(error_name) for error_name in error_names):
        print(f"\nОшибка для локации {location}:\n{result}")
    else:
        print(f"Прогноз погоды:\n{result}")


def main():
    locations_to_check = ["london", "Cherepovec", "SVO"]
    request_params = {
        "nTqu": "",
        "lang": "ru",
        "m": "",
        "n": "",
    }
    try:
        for location in locations_to_check:
            weather_data = fetch_single_weather(location, request_params)
            print_weather_info(location, weather_data)
    except Exception as exs:
        print(f"Произошла непредвиденная ошибка: {exs}")


if __name__ == "__main__":
    main()
