import requests

NOAA_METAR_URL = "https://aviationweather.gov/api/data/metar"
NOAA_TAF_URL = "https://aviationweather.gov/api/data/taf"

def get_metar(icao):
    response = requests.get(NOAA_METAR_URL, params={
        "ids": icao,
        "format": "raw"
    })
    return response.text.strip()

def get_taf(icao):
    response = requests.get(NOAA_TAF_URL, params={
        "ids": icao,
        "format": "raw"
    })
    return response.text.strip()
def parse_metar(metar_str):
    # Simple parser for demonstration purposes
    parts = metar_str.split()
    data = {
        "station": parts[0],
        "time": parts[1],
        "wind": parts[2],
        "visibility": parts[3],
        "temperature": parts[4].split('/')[0],
        "dew_point": parts[4].split('/')[1],
        "altimeter": parts[5],
    }
    return data