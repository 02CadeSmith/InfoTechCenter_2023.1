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
    print("low =", milesToGasStationsLow)
    print("quarter tank =", milesToGasStationQuarterTank)


gasLevelAlert()