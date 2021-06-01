import requests

api_key = "67da29cb91129f1a68c1c06c1be92daa"

city_name = "HaNoi"

url = "http://api.openweathermap.org/data/2.5/weather?q="+ city_name +"&appid=" + api_key +"&units=imperial"


request = requests.get(url)
json = request.json()

description = json.get("weather")[0].get("description")
print("Today's forecast is",description)

temp_min = json.get("main").get("temp_min")
temp_max = json.get("main").get("temp_max")

print("The minimun temperature is", temp_min)
print("The maximun temperature is", temp_max)

