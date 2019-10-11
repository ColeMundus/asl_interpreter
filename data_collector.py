import tkinter as tk
from PIL import Image
from random import choice
import cv2
import os

alpha = 'abcdefghijklmnopqrstuvwxyz'

print('Starting data collector')

camera = cv2.VideoCapture(0)
cv2.namedWindow("Data Capture")

print('Please select capture mode: [random](1) [selected](2)')
while True:
	mode = '1'#input('Capture mode [1] 2: ')
	if mode in ['1', '2', 'random', 'selected']:
		break
	else:
		print('Invalid mode selected, please select between random or selected')

print('Starting capture, press ESC to close')
count = 0
ret = True
printed = False
while ret:
	ret, frame = camera.read()
	frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
	edDet = cv2.Canny(frame,100,120)
	#mask = cv2.createBackgroundSubtractorKNN().apply(frame)
	with_rect = cv2.rectangle(frame,(60,60),(375,375),(0,255,0),2)
	cv2.imshow("Data Capture", with_rect)
	cv2.imshow("Edge Detection", edDet)
	cv2.imshow("Cropped", frame[60:375, 60:375])
	k = cv2.waitKey(1)
	if k%256 == 27:
		break
	if mode in ['random', '1']:
		if not printed:
			key = choice(alpha).capitalize()
			print(key)
		printed = True
		if k%256 == 32:
			if not os.path.exists(f'training_data/capture/{key}/'):
				os.makedirs(f'training_data/capture/{key}/')
			img = f"training_data/capture/{key}/{str(count).zfill(5)}.png"
			cv2.imwrite(img, frame)
			print(f'Wrote to file '+img)
			printed = False
			count += 1
	elif mode in ['selected', '2']:
		if 123 > k%256 > 96:
			key = alpha[k%256-97].capitalize()
			if not os.path.exists(f'training_data/capture/{key}/'):
				os.makedirs(f'training_data/capture/{key}/')
			img = f"training_data/capture/{key}/{str(count).zfill(5)}.png"
			cv2.imwrite(img, frame)
			print(f'Wrote to file '+img)
			count += 1

camera.release()
cv2.destroyAllWindows()
