import requests

def get_weather_metric(metric: str, latitude: float, longitude: float):
    r = requests.get('https://api.open-meteo.com/v1/forecast?latitude=' + str(latitude) + '&longitude=' + str(longitude) + '&current_weather=true')
    if r.status_code == 200:
        if metric in r.json()["current_weather"]:
            return(r.json()['current_weather'][metric])
        else:
            return("Metric not supported!")
    else:
        return("Open-Meteo is down!")