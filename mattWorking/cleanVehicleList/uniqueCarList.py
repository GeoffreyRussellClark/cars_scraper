import pandas as pd
import sys
import numpy as np
import calibrationCode.settings

data = pd.read_csv("rawData/clean_cars.csv")

cars = data.ix[:,1:3]
cars["key"] = cars["make"] + cars["model"]
cars.columns

uniqueCars = cars.drop_duplicates(subset='key', keep='last').ix[:,0:2]

uniqueCars.to_csv("cleanVehicleList/carList/unique_car_list.csv",index=False)
