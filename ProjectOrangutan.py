
"""
Our Welcome Screen will star our progrImport Libraries Here
import time
import sys
"""
import random
import sys
import time
from time import sleep

timeToSleep = 2

print("\n\nWelcome - InfoTech Center 2023\n")

time.sleep(timeToSleep)

# Add code to have the ellipsis add a dot every .5 seconds
x = 0
ellipsis = 0

while x != 20:
    x += 1
    message = ("InfoTech Center 2023 is loading" + "." * ellipsis)
    ellipsis = ellipsis + 1
    sys.stdout.write("\r" + message)  # \r prints a carriage return first, so, message is printed on top of the previous line
    time.sleep(.5)
    if ellipsis == 4:
        ellipsis = 0
    if x == 20:
        print("\n\nOperating System Loaded - Retina Scanned - Access Granted")

print("\n******************************************************\n")
print("Checking current gas levels\n\n")
sleep(1)

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
