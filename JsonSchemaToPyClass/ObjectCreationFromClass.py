from WeatherForecastClass import WeatherAirConditions
from WeatherForecastClass import WeatherCommons
from WeatherForecastClass import GSMAFIWAREWeatherForecastSchema

weatherAirConditions = WeatherAirConditions(
    {"temperature": 6, "feelLikesTemperature": 4, "relativeHumidity": 0.5})
weatherCommons = WeatherCommons({"temperature": 1, "feelLikesTemperature": 1,
                                "relativeHumidity": 1, "weatherType": "type", "visibility": "moderate", "windDirection": 90, "windSpeed": 1, })
gSMAFIWAREWeatherForecastSchema = GSMAFIWAREWeatherForecastSchema(
    {"location": "Saint-Etienne", "alert": "lowTemperature", "date": "2021-01-01", "current": weatherCommons, "dayMinimum": weatherAirConditions, "dayMaximum": weatherAirConditions})

print("____________________________________________________________________________________________________________________________________________________")
print(weatherAirConditions)
print("____________________________________________________________________________________________________________________________________________________")
print(weatherCommons)
print("____________________________________________________________________________________________________________________________________________________")
print(gSMAFIWAREWeatherForecastSchema)
