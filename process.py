from os import listdir
from matplotlib import pyplot as plt
import cv2
import numpy as np
import csv

PHOTO_DIRECTORY = "/home/george/Desktop/noir_images/2020-03-23 Farm IR Select/"
OUTPUT_DIRECTORY = "output/"
FASTIE = "fastie.txt"

lut = np.zeros((256, 1, 3), dtype=np.uint8)

r = []
g = []
b = []

with open(FASTIE, newline='\n') as csvfile:
	reader = csv.reader(csvfile, delimiter='\t')
	next(reader, None)
	for row in reader:
		r.append(row[1])
		g.append(row[2])
		b.append(row[3])

lut[:, 0, 0] = r
lut[:, 0, 1] = g
lut[:, 0, 2] = b

# exit(0)

#print(lut)

for filename in sorted(listdir(PHOTO_DIRECTORY)):
	full_filename = PHOTO_DIRECTORY + filename
	print(filename)

	img = plt.imread(full_filename)

	# plt.imshow(img)
	# plt.show()
	# print(img.shape)

	blue_channel = img[:, :, 0]/255
	green_channel = img[:, :, 1]/255
	red_channel = img[:, :, 2]/255

	ndvi = (blue_channel - red_channel)/(blue_channel + red_channel)

	# max_value = np.max(ndvi)
	# min_value = np.min(ndvi)
	# print(max_value, min_value)

	ndvi = 500*ndvi + 127 
	#emprical value of 255, 127 assumes good white balance

	# max_value = np.max(ndvi)
	# min_value = np.min(ndvi)
	# print(max_value, min_value)

	ndvi_gray = np.array(ndvi, dtype = np.uint8)

	#print(ndvi_gray)

	# plt.imshow(ndvi, cmap='gray',vmin=0, vmax=255)
	# plt.show()

	#ndvi_false_colour = cv2.applyColorMap(ndvi_gray, cv2.COLORMAP_JET)
	
	ndvi_false_colour = cv2.applyColorMap(ndvi_gray, lut)


	cv2.imwrite(OUTPUT_DIRECTORY + filename, ndvi_false_colour)