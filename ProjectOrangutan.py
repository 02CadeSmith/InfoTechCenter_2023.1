print("******************************************************")
print("Gasoline Branch\n\n")
# Import Libraries here
import random
from time import sleep

def gasLevelGuage():
    GasLevelList = ["Empty", "Low", "Quarter Tank", "Half Tank", "Three Quarter Tank", "Full Tank"]
    CurrentGasLevel = random.choice(GasLevelList)
    return CurrentGasLevel

