import pandas as pd
import numpy as np
from datetime import date
from math import floor

def Calc(Make,Model,Location,PurchasePrice,PurchaseYear,Millage):
	"""#input variables:
	Make = 'Honda'
	Model = 'Ballade'
	Location = 'Johannesburg'
	PurchasePrice = 185000
	PurchaseYear = 2015
	Millage = 100000"""

	#conservatisim factor - value all cars less depreciation less this percentage
	ConservFactor = 0.025

	#data validation:
	DataValid = True

	#initial checks to ensure that the server requester is not just fishing randomly
	try:
		#python v2
		if isinstance(Make, basestring) is False:
			DataValid = False
		if isinstance(Model, basestring) is False:
			DataValid = False
		if isinstance(Location, basestring) is False:
			DataValid = False
		if isinstance(PurchasePrice, (int,long)) is False:
			DataValid = False
		if isinstance(PurchaseYear, (int,long)) is False:
			DataValid = False
		if isinstance(Millage, (int,long)) is False:
			DataValid = False
	except:
		#python v3
		if isinstance(Make, str) is False:
			DataValid = False
		if isinstance(Model, str) is False:
			DataValid = False
		if isinstance(Location, str) is False:
			DataValid = False
		if isinstance(PurchasePrice, int) is False:
			DataValid = False
		if isinstance(PurchaseYear, int) is False:
			DataValid = False
		if isinstance(Millage, int) is False:
			DataValid = False

	# logic checks 
	MakeModels = pd.read_csv('MakeModels.csv')

	if DataValid is False:
		return "One or more of the parameters were incorrect - could not calculate a value"
	else:
		if Make not in MakeModels['make'].values:
			DataValid = False
		if Model not in MakeModels['model'][MakeModels['make'] == Make].values:
			DataValid = False
		if PurchasePrice > 5000000 or PurchasePrice < 5000:
			DataValid = False
		if PurchaseYear < 1900 or PurchaseYear > date.today().year:
			DataValid = False
		if Millage < 0 or Millage > 1000000:
			DataValid = False
		#!!add check to see if purchase price is within 1 std dev of the price that we have on record for the car (with inflationarey adj.
			
	#print(DataValid)

	if DataValid is False:
		return "One or more of the parameters were incorrect - could not calculate a value"
	else:
		
		DepFactors = pd.read_csv('DepreciationFactors.csv')
		DepFactors = 1 - DepFactors
		NumYears = date.today().year - PurchaseYear
		
		# if Location provided is one that we have records for then use it, otherwise just use records for South Africa
		try:
			DepPerc = DepFactors[Location][DepFactors.index < NumYears].product()
			if DepPerc < 0.001:
				DepPerc = DepFactors['South Africa'][DepFactors.index < NumYears].product()
		except:
			DepPerc = DepFactors['South Africa'][DepFactors.index < NumYears].product()
		
		CurrentValue = PurchasePrice * DepPerc * (1-ConservFactor)
		
		return floor(CurrentValue/1000)*1000
