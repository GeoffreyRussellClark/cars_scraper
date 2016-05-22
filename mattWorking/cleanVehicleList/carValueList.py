
#/matt/usr/bin/python

import calibrationCode.settings
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from sklearn import linear_model

# Parameters
priceInflation = 0.1
maxInflation = 0.2
maxYear = 2018
minYear = 1990

# Initialise pricing data frame
allPrices = pd.DataFrame();

# Load in raw data
rawData = pd.read_csv("rawData/clean_cars.csv")
cars = rawData

# Generating unique key per vehicle
cars["key"] = cars["make"] + cars["model"]

# Getting unique vehicles for processing
keys = np.unique(cars["key"])

# Start of loop for all the vehicles in the data set
for key in keys:

    # Extract all entries relating to specific vehicle
    subSet = cars.ix[cars["key"]==key,:];
    subSet_shape = np.shape(subSet)
    priceSet = pd.DataFrame();

    # Populating year, make and model of the vehicle being
    # considered.
    years = [];
    make = [];
    model = [];
    prices = [];
    predType = [];

    for year in range(maxYear-minYear):
        years.append(minYear + year);
        make.append(subSet["make"].values[0]);
        model.append(subSet["model"].values[0]);

    priceSet["year"] = years
    priceSet["make"] = make
    priceSet["model"] = model

    # Determine the price of vehicle if only one
    # value is available
    if subSet_shape[0] == 1:
        year = subSet["year"].values[0]
        price = subSet["price"].values[0]

        for proj_year in range(minYear,maxYear):
            est_price = price*(1+priceInflation)**(proj_year - year)
            prices.append(est_price)
            predType.append("estimate")

        priceSet["price"] = prices

    # Determine the price of vehicle through linear
    # interpolation using points available
    else:
        year = subSet["year"].values.reshape(-1,1)
        price = subSet["price"].values.reshape(-1,1)

        #Create linear regression object
        regr = linear_model.LinearRegression()

        # Train the model using the training sets
        regr.fit(year, price)

        # The coefficients
        print('Coefficients: \n', regr.coef_)
        # The mean square error
        print("Residual sum of squares: %.2f"
              % np.mean((regr.predict(year) - price) ** 2))
        # Explained variance score: 1 is perfect prediction
        print('Variance score: %.2f' % regr.score(year, price))

        # Plot outputs
        """plt.scatter(year, price,  color='black')
        plt.plot(year, regr.predict(year), color='blue',
                 linewidth=3)
        plt.xticks(())
        plt.yticks(())
        plt.show()"""

        for proj_year in range(minYear, maxYear):
            predType.append("model")

        # Predicting prices for each year
        est_price = regr.predict(np.asarray(years).reshape(-1,1))
        priceSet["price"] = est_price

    priceSet["predType"] = predType;

    allPrices = pd.concat([allPrices, priceSet], axis=0)

allPrices.to_csv("cleanVehicleList/carPrices/allPrices.csv",index=False)


plt.plot(priceSet["price"])
