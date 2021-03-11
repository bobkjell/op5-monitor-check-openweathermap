#!/usr/bin/env python

# Modules
import requests, argparse

# Arguments
parser = argparse.ArgumentParser(description="Get weather statistics using OpenWeatherMap API.")
parser.add_argument("-l", "--location", help="Weather location. Find your location at: https://openweathermap.org/find. Example: London,UK.", type=str, required=True)
parser.add_argument("-k", "--apikey", help="API Key. Register at: https://openweathermap.org/appid", type=str, required=True)
parser.add_argument("-t", "--type", help="Type of weather statistic. Available types: temp, wind, humidity, pressure & description", type=str, required=True)
args = parser.parse_args()

# Make request
try:
  r = requests.get("http://api.openweathermap.org/data/2.5/weather?q=" + args.location + "&appid=" + args.apikey + "&units=metric")
  r.raise_for_status()
except requests.exceptions.HTTPError as error:
  if r.status_code == 404:
    print ("UNKNOWN: 404 Location not found.")
    exit(3)
  raise SystemExit(error)

# JSON
data = r.json()

# Temperature
if args.type == "temp":
  current_temp=(data["main"]["temp"])
  feels_like=(data["main"]["feels_like"])
  max_temp=(data["main"]["temp_max"])
  min_temp=(data["main"]["temp_min"])
  print ("INFO: Current temp is: " + str(round(current_temp,1)) + "C. It feels like: " + str(round(feels_like,1)) + "C. Todays max temp is: " + str(round(max_temp,1)) + "C. Todays min temp is: " + str(round(min_temp,1)) + "C | current_temp=" + str(round(current_temp,1)) + "C feels_like=" + str(round(feels_like,1)) + "C max_temp=" + str(round(max_temp,1)) + "C min_temp=" + str(round(min_temp,1)) + "C")
  exit(0)
# Wind
elif args.type == "wind":
  current_wind=(data["wind"]["speed"])
  print ("INFO: Current wind speed is: " + str(current_wind) + "ms | wind_speed=" + str(current_wind) + "ms")
  exit(0)

# Humidity
elif args.type == "humidity":
  current_humidity=(data["main"]["humidity"])
  print ("INFO: Current humidity is: " + str(current_humidity) + "% | humidity=" + str(current_humidity) + "%")
  exit(0)

# Pressure
elif args.type == "pressure":
  current_pressure=(data["main"]["pressure"])
  print ("INFO: Current pressure is: " + str(current_pressure) + "hPa | pressure=" + str(current_pressure) + "hPA")
  exit(0)

# Weather description
elif args.type == "description":
  weather_desc=(data["weather"][0]["description"])
  print ("INFO: Weather description is: " + weather_desc + ".")

# Invalid weather type
else:
  print ("UNKNOWN: Type invalid. Valid types are temp, wind, humidity, pressure & description.")
  exit(3)
