import requests


def get_weather_desc_temp():
    api_key = "67da29cb91129f1a68c1c06c1be92daa"

    city_name = "HaNoi"

    url = "http://api.openweathermap.org/data/2.5/weather?q="+ city_name +"&appid=" + api_key +"&units=imperial"


    request = requests.get(url)
    json = request.json()

    description = json.get("weather")[0].get("description")
    temp_min = json.get("main").get("temp_min")
    temp_max = json.get("main").get("temp_max")
    return {
        "description" : description,
        "temp_min" : temp_min,
        "temp_max" : temp_max
    }


weather = get_weather_desc_temp()

print("Today's forecast is", weather.get("description"))
print("The minimun temperature is", weather.get("temp_min"))
print("The maximun temperature is", weather.get("temp_max"))


