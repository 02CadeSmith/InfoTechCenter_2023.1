print("******************************************************")
print("Gasoline Branch\n\n")
# Import Libraries here
import random
from time import sleep

# Function that lists Gas Stations, randomly choosing one, and returning its value

def gasLevelGauge():
    GasLevelList = ["Empty", "Low", "Quarter Tank", "Half Tank", "Three Quarter Tank", "Full Tank"]
    CurrentGasLevel = random.choice(GasLevelList)
    return CurrentGasLevel

# Function with a list of Gas Stations

def listOfGasStation():
    gasStations = ["Shell", " Speedway", "Exxon", "Meijer", "Costco", "Marathon", "BP", "Circle K", " Wesco"]
    gasStationsNearby = random.choice(gasStations)
    return gasStationsNearby

# Function will call the gas level gauge to determine gas level and then find a close gas station if low

def gasLevelAlert():
    milesToGasStationsLow = round(random.uniform(1, 25,), 1)
    milesToGasStationQuarterTank = round(random.uniform(25.1, 50, ), 1)
    gasLevelIndicator = gasLevelGauge()
    if gasLevelIndicator == "Empty":
        print("***WARNING - YOU ARE EMPTY***")
        sleep(1.25)
        print("Calling Triple AAA")
    elif gasLevelIndicator == "Low":
        print("Your gas tank is extremely low, checking Google Maps for the closest gas station")
        sleep(1.5)
        print("the closest gas station is", listOfGasStation(), "which is", milesToGasStationsLow, "miles away.")
    elif gasLevelIndicator == "Quarter Tank":
        print("You have one quarter tank left, checking Google Maps for the closest gas station")
        sleep(1.5)
        print("the closest gas station is", listOfGasStation(), "which is", milesToGasStationQuarterTank, "miles away.")
    elif gasLevelIndicator == "Half Tank":
        print("You have half a tank of gas left")
    elif gasLevelIndicator == "Three Quarter Tank":
        print("Your tank has three quarters of gas left")
    else:
         print("You have a full tank of gas")


gasLevelAlert()

