import requests

UNITS = "m"
OPTIONS = "n"
LANG = "ru"

LOCATIONS = ["london", "Cherepovec", "SVO"]
PARAMS = {
    "nTqu": "",
    "lang": "en"
}
HEADERS = {
    "Accept": "*/*",
    "User-Agent": "curl"
}


def get_weather():
    for location in LOCATIONS:
        url = f"https://wttr.in/{location}?{UNITS}&{OPTIONS}&lang={LANG}"
        response = requests.get(url, params=PARAMS, headers=HEADERS)
        print(response.text)


def main():
    get_weather()


if __name__ == "__main__":
    main()
