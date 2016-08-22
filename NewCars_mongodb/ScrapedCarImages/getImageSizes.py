from PIL import Image
import os
import csv

baseDirectories = ['NewCars/full/', 'UsedCars/full/', 'UsedCarsAT/Toyota/']

imageSize = []
imageRatios = {}
counter = 0
errCount = 0

for baseDirectory in baseDirectories:
	for i in os.listdir(baseDirectory):
		#if i.endswith('.jpg') or i.endswith('.png'): # all files are photos - so don't really need this
		try:
			with Image.open(baseDirectory + i) as im:
				width, height = im.size
				#want to get the ratio (std want to use is 4:3 - want to see how close the image is to this')
				ratio = '4:'+ str(round(float(height)/float(width) * 4,1))
				imageSize.append([width, height, ratio])
				
				if ratio in imageRatios:
					imageRatios[ratio] += 1
				else:
					imageRatios[ratio] = 1
					
				counter += 1		
				if counter % 500 == 0:
					print str(counter) + ' photos processed'
		except:
			errCount += 1
			

print(imageSize[0:5])
print(imageRatios)
print('Errors with images: ' + str(errCount))

#write the dictionary to a csv
with open('imageSizes.csv', 'wb') as f:
	w = csv.DictWriter(f, imageRatios.keys())
	w.writeheader
	w.writerow(imageRatios)		
			
