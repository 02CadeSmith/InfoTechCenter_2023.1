print("\n****************************\n")

print("weather Branch")

# Import Libraries here
import random
from time import sleep

# Create a function randomly choosing the weather from a list
def weather():
    weatherForecast = ["Snowing", "Blizzard", "Rain", "Foggy", "Windy", "Icy", "Sunny", "Cloudy"]
    weatherCondition = random.choice(weatherForecast)
    return weatherCondition
    