from typing import Any, Union

from statham.schema.constants import Maybe
from statham.schema.elements import (
    AnyOf,
    Element,
    Integer,
    Null,
    Number,
    Object,
    String,
)
from statham.schema.property import Property


class WeatherAirConditions(Object):

    temperature: Maybe[Union[float, None]] = Property(AnyOf(Number(), Null()))

    feelLikesTemperature: Maybe[Union[float, None]] = Property(AnyOf(Number(), Null()))

    relativeHumidity: Maybe[Union[float, None]] = Property(AnyOf(Number(minimum=0, maximum=1), Null()))


class WeatherCommons(Object):

    temperature: Maybe[Union[float, None]] = Property(AnyOf(Number(), Null()))

    feelLikesTemperature: Maybe[Union[float, None]] = Property(AnyOf(Number(), Null()))

    relativeHumidity: Maybe[Union[float, None]] = Property(AnyOf(Number(minimum=0, maximum=1), Null()))

    weatherType: Maybe[str] = Property(String())

    visibility: Maybe[str] = Property(String(enum=['veryPoor', 'poor', 'moderate', 'good', 'veryGood', 'excellent']))

    windDirection: Maybe[Union[int, None]] = Property(AnyOf(Integer(minimum=0, maximum=360), Null()))

    windSpeed: Maybe[Union[float, None]] = Property(AnyOf(Number(minimum=0), Null()))

    refPointOfInterest: Maybe[str] = Property(String())


class GSMAFIWAREWeatherForecastSchema(Object):

    location: Maybe[str] = Property(String())

    alert: Maybe[Any] = Property(Element(enum=['rainfall', 'highTemperature', 'lowTemperature', 'heatWave', 'coldWave', 'ice', 'snow', 'wind', 'fog', 'flood', 'tsunami', 'tornado', 'tropicalCyclone', 'hurricane', 'snow/ice', 'thunderstorms', 'coastalEvent', 'forestFire', 'avalanches', 'rain/flood']))

    date: Maybe[str] = Property(String(format='date-time'))

    current: Maybe[WeatherCommons] = Property(WeatherCommons)

    dayMaximum: Maybe[WeatherAirConditions] = Property(WeatherAirConditions)

    dayMinimum: Maybe[WeatherAirConditions] = Property(WeatherAirConditions)
