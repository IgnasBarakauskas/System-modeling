import unittest
from WeatherForecastClass import WeatherAirConditions
from WeatherForecastClass import WeatherCommons
from WeatherForecastClass import GSMAFIWAREWeatherForecastSchema


class TestCreation(unittest.TestCase):

    def test_creationWeatherAirConditions(self):
        weatherAirConditions = WeatherAirConditions(
            {"temperature": 6, "feelLikesTemperature": 4, "relativeHumidity": 0.5})
        self.assertEqual(weatherAirConditions.temperature, 6)
        self.assertEqual(weatherAirConditions.feelLikesTemperature, 4)
        self.assertEqual(weatherAirConditions.relativeHumidity, 0.5)
        self.assertIsInstance(weatherAirConditions, WeatherAirConditions)

    @unittest.expectedFailure
    def test_creationWeatherAirConditionsErr(self):
        self.assertIsInstance(WeatherAirConditions(
            {"temperature": 6, "feelLikesTemperature": 4, "relativeHumidity": 1.5}), WeatherAirConditions)

    def test_creationWeatherCommons(self):
        weatherCommons = WeatherCommons({"temperature": 1, "feelLikesTemperature": 1,
                                         "relativeHumidity": 1, "weatherType": "type", "visibility": "moderate", "windDirection": 90, "windSpeed": 1, })
        self.assertEqual(weatherCommons.temperature, 1)
        self.assertEqual(weatherCommons.feelLikesTemperature, 1)
        self.assertEqual(weatherCommons.relativeHumidity, 1)
        self.assertEqual(weatherCommons.weatherType, "type")
        self.assertEqual(weatherCommons.visibility, "moderate")
        self.assertEqual(weatherCommons.windDirection, 90)
        self.assertEqual(weatherCommons.windSpeed, 1)
        self.assertIsInstance(weatherCommons, WeatherCommons)

    @unittest.expectedFailure
    def test_creationWeatherCommonsErr(self):
        self.assertIsInstance(WeatherCommons({"temperature": 1, "feelLikesTemperature": 1,
                                              "relativeHumidity": 1.5, "weatherType": "type", "visibility": "moderate", "windDirection": 90, "windSpeed": 1, }), WeatherCommons)
        self.assertIsInstance(WeatherCommons({"temperature": 1, "feelLikesTemperature": 1,
                                              "relativeHumidity": 1, "weatherType": "type", "visibility": "New", "windDirection": 90, "windSpeed": 1, }), WeatherCommons)
        self.assertIsInstance(WeatherCommons({"temperature": 1, "feelLikesTemperature": 1,
                                              "relativeHumidity": 1, "weatherType": "type", "visibility": "moderate", "windDirection": 370, "windSpeed": 1, }), WeatherCommons)
        self.assertIsInstance(WeatherCommons({"temperature": 1, "feelLikesTemperature": 1,
                                              "relativeHumidity": 1, "weatherType": "type", "visibility": "moderate", "windDirection": 90, "windSpeed": -1, }), WeatherCommons)

    def test_creationGSMAFIWAREWeatherForecastSchema(self):
        weatherAirConditions = WeatherAirConditions(
            {"temperature": 6, "feelLikesTemperature": 4, "relativeHumidity": 0.5})
        weatherCommons = WeatherCommons({"temperature": 1, "feelLikesTemperature": 1,
                                         "relativeHumidity": 1, "weatherType": "type", "visibility": "moderate", "windDirection": 90, "windSpeed": 1, })
        gSMAFIWAREWeatherForecastSchema = GSMAFIWAREWeatherForecastSchema(
            {"location": "Saint-Etienne", "alert": "lowTemperature", "date": "2021-01-01", "current": weatherCommons, "dayMinimum": weatherAirConditions, "dayMaximum": weatherAirConditions})
        self.assertEqual(
            gSMAFIWAREWeatherForecastSchema.location, "Saint-Etienne")
        self.assertEqual(
            gSMAFIWAREWeatherForecastSchema.alert, "lowTemperature")
        self.assertEqual(gSMAFIWAREWeatherForecastSchema.date, "2021-01-01")
        self.assertIsInstance(
            gSMAFIWAREWeatherForecastSchema.current, WeatherCommons)
        self.assertIsInstance(
            gSMAFIWAREWeatherForecastSchema.dayMaximum, WeatherAirConditions)
        self.assertIsInstance(
            gSMAFIWAREWeatherForecastSchema.dayMinimum, WeatherAirConditions)

    @unittest.expectedFailure
    def test_creationGSMAFIWAREWeatherForecastSchemaErr(self):
        weatherAirConditions = WeatherAirConditions(
            {"temperature": 6, "feelLikesTemperature": 4, "relativeHumidity": 0.5})
        weatherCommons = WeatherCommons({"temperature": 1, "feelLikesTemperature": 1,
                                         "relativeHumidity": 1, "weatherType": "type", "visibility": "moderate", "windDirection": 90, "windSpeed": 1, })
        self.assertIsInstance(GSMAFIWAREWeatherForecastSchema(
            {"location": "Saint-Etienne", "alert": "Alert", "date": "2021-01-01", "current": weatherCommons, "dayMinimum": weatherAirConditions, "dayMaximum": weatherAirConditions}), GSMAFIWAREWeatherForecastSchema)
        self.assertIsInstance(GSMAFIWAREWeatherForecastSchema(
            {"location": "Saint-Etienne", "alert": "lowTemperature", "date": "2021-010-01", "current": weatherCommons, "dayMinimum": weatherAirConditions, "dayMaximum": weatherAirConditions}), GSMAFIWAREWeatherForecastSchema)


if __name__ == "__main__":
    unittest.main()
