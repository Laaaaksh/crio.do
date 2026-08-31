# crio.do

A desktop weather app in Python, built during the Crio Winter of Doing
externship. Enter a city name in a Tkinter window and it fetches current
conditions (temperature, min/max, pressure, humidity, wind, sunrise/sunset)
from the OpenWeatherMap API and displays them.

## Stack

Python 3, Tkinter for the UI, `requests` for the API call.

## Status

Written in 2021–2023 as an externship project. Not maintained. Note: the
OpenWeatherMap API key is hardcoded directly in `weatherapp.py` and has been
public in this repo's history — worth rotating/removing if it's still live.

## Running it

Not verified end-to-end (the hardcoded OpenWeatherMap key may no longer be
valid). To try it:

```
pip install requests
python3 weatherapp.py
```
