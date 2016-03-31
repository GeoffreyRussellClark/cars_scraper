import pandas as pd
import numpy as np
from datetime import date

#input variables:
Make = 'Honda'
Model = 'Ballade'
Location = 'Johannesburg'
Year = 2010
Millage = 100000

#data validation:
DataValid = True

MakeModels = pd.read_csv('MakeModels.csv')

try:
	#python v2
	if isinstance(Make, basestring) is False:
		DataValid = False
	if isinstance(Model, basestring) is False:
		DataValid = False
	if isinstance(Location, basestring) is False:
		DataValid = False
	if isinstance(Year, (int,long)) is False:
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
	if isinstance(Year, int) is False:
		DataValid = False
	if isinstance(Millage, int) is False:
		DataValid = False
		
if DataValid:
	if Make not in MakeModels['make'].values:
		DataValid = False
	if Model not in MakeModels['model'][MakeModels['make'] == Make].values:
		DataValid = False
	if Year < 1900 or Year > date.today().year:
		DataValid = False
	if Millage < 0 or Millage > 1000000:
		DataValid = False
		
print(DataValid)

if DataValid is False:
	pass
else:
	
	Depfactors = pd.read_csv('DepreciationFactors.csv')


