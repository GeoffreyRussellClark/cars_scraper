import pandas as pd
import numpy as np

StartYear = 2016

CarData = pd.read_csv('clean_cars.csv', dtype={'id': np.int64, 'make': str, 'model': str, 'year': np.int64, 'location': str, 'price': np.float64})

#delete data where the location is not "South Africa" - the other data will be used to make regional adjustments
#CarData = CarData[CarData['location'] == 'South Africa']

#CarData = CarData[CarData['make'] == 'Volvo']
#CarData = CarData[CarData['model'] == 'Corolla']

#print(CarData.head(5))
#print(CarData.sort_values(by=['price'], ascending=1).head(5))
#print(CarData.sort_values(by=['price'], ascending=0).head(5))

#crude clean of data
CarData = CarData[CarData['price'] > 5000]
CarData = CarData[CarData['price'] < 1000000]

#not a very effiecient function but it anyway
def CalcDepYr(Yr1, Yr2, CarDataLoc):
	CarDataYr1 = CarDataLoc[CarDataLoc['year'] == Yr1]
	CarDataYr2 = CarDataLoc[CarDataLoc['year'] == Yr2]

	SumYr1 = 0
	SumYr2 = 0
	for index, car in CarDataYr1.iterrows():
		if (car['make'] in CarDataYr2['make'].values) and (car['model'] in CarDataYr2['model'].values):
			SumYr1 += car[5]
	for index, car in CarDataYr2.iterrows():
		if (car['make'] in CarDataYr1['make'].values) and (car['model'] in CarDataYr1['model'].values):
			SumYr2 += car[5]
	
	if SumYr1 > 0:
		ans = (1 - SumYr2/SumYr1)
	else:
		ans = 0
	
	return ans

def CalcFactorsLocation(Location):
	CarDataLoc = CarData[CarData['location'] == Location]
	
	#cycle through all the years from the start all the way back to 1980 to calculate the average depreciation factors across the book
	YrRange = range(StartYear, 1995 - 1, -1)
	
	DepFactors = []
	for Yr in YrRange:
		DepFactors.append(CalcDepYr(Yr, Yr-1, CarDataLoc))
		
	DepFactorsDF = pd.DataFrame(DepFactors, columns=['DepFactor'])
	
	#print(DepFactorsDF)
	return DepFactorsDF

Locations = pd.Series(CarData['location'].values.ravel()).unique()

#DepFactorsDF = CalcFactorsLocation('South Africa')
DepFactorsDF = pd.DataFrame()

for loc in Locations:
	DepFactorsDF[loc] = CalcFactorsLocation(loc)

#write out to a csv file:
DepFactorsDF.to_csv('DepreciationFactors.csv', encoding = 'utf-8')

#write out a dataset of unique  car makes and models
MakeModelDF = CarData[['make','model']]
MakeModelDF = MakeModelDF.drop_duplicates()
MakeModelDF.to_csv('MakeModels.csv', encoding = 'utf-8')
