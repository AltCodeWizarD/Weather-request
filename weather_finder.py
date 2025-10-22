import requests

locations = ["london", "Cherepovec", "SVO"]
params = {
    "nTqu": "",
    "lang": "en"
}
headers = {
    "Accept": "*/*",
    "User-Agent": "curl"
}


def get_weather():
    for location in locations:
        url = f"https://wttr.in/{locations}?m&n&lang=ru"
        response = requests.get(url, params=params, headers=headers)
        print(response.text)


if __name__ == "__main__":
    get_weather()
