Implementation made by Ignas Barakauskas CPS2

Required python 3

For running base64Convertion.py you will need folowing library:
	library to install:
		Pillow
* pip install pillow

Class Generation from Json schema requires:
	library to install:
		statham-schema
*pip install statham-schema

To generate Python class from Json schema you need to run this command in cmd

statham --input https://ci.mines-stetienne.fr/i2si/interop/WeatherForecast.json --output ./JsonSchemaToPyClass/WeatherForecastClass.py
		|      Json schema file path or web link to schema						|          output file where class is saved