import requests

BASE_URL = "https://wttr.in/"
LOCATIONS = ["london", "Cherepovec", "SVO"]

PARAMS = {
    "nTqu": "",
    "lang": "en",
    "m": "",
    "n": "",
}


def fetch_single_weather(location):
    """Получает погоду для одной локации"""
    url = f"{BASE_URL}{location}"
    PARAMS["lang"] = "ru"

    try:
        response = requests.get(url, params=PARAMS)
        response.raise_for_status()
        return response.text, response.status_code
    except requests.exceptions.HTTPError as http_error:
        return f"HTTP ошибка: {http_error}", None
    except requests.exceptions.ConnectionError as connection_error:
        return f"Ошибка подключения: {connection_error}", None
    except requests.exceptions.Timeout as timeout_error:
        return f"Таймаут: {timeout_error}", None
    except requests.exceptions.RequestException as request_error:
        return f"Произошла ошибка: {request_error}", None


def print_weather_info(location, weather_data, status_code):
    if status_code:
        print(f"\nПогода в {location}")
        print(f"Статус запроса: {status_code}")
        print(f"Прогноз погоды:\n{weather_data}")
    else:
        print(f"\nОшибка для локации {location}:\n{weather_data}")


def main():
    for location in LOCATIONS:
        weather_data, status_code = fetch_single_weather(location)
        print_weather_info(location, weather_data, status_code)


if __name__ == "__main__":
    main()
