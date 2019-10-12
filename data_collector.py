import tkinter as tk
from PIL import Image
from random import choice
import glob
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
ret = True
printed = False

def write_original_image(cv2, frame, letter):
	if not os.path.exists(f'training_data/capture/original_images/'):
		os.makedirs(f'training_data/capture/original_images/')
	try:
		last_number = int(glob.glob(f'training_data/capture/original_images/{letter}_*.png')[-1][-8:-4])
	except Exception as e:
		last_number = 0
	path = f'training_data/capture/original_images/{letter}_{str(last_number+1).zfill(4)}.png'
	cv2.imwrite(path, frame[60:375, 60:375])
	print('Wrote to file ' + path)
	return path

def write_data(frame, letter):
	data_string = ''.join([str(int(i)) for j in frame/255 for i in j])
	with open('training_data/capture/output.csv', 'a') as f:
		f.write(f'{alpha.index(letter.lower())},{data_string}\n')

while ret:
	ret, frame = camera.read()

	raw_image = cv2.rectangle(frame,(60,60),(375,375),(0,255,0),2)
	cv2.imshow("Data Capture", raw_image)

	frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
	downscale = cv2.resize(frame[60:375, 60:375], (128, 128), interpolation=cv2.INTER_LINEAR)
	upscale = cv2.resize(downscale, (512, 512), interpolation=cv2.INTER_NEAREST)
	cv2.imshow("Down Scaled Capture", upscale)

	data_output = cv2.Canny(downscale,100,120)
	data_output = cv2.resize(data_output, (512, 512), interpolation=cv2.INTER_NEAREST)
	cv2.imshow("Cropped", data_output)

	k = cv2.waitKey(1)
	if k%256 == 27:
		break
	if mode in ['random', '1']:
		if not printed:
			key = choice(alpha).capitalize()
			print(key)
		printed = True
		if k%256 == 32:
			write_original_image(cv2, frame, key)
			write_data(data_output, key)
			printed = False
	elif mode in ['selected', '2']:
		if 123 > k%256 > 96:
			key = alpha[k%256-97].capitalize()
			write_original_image(cv2, frame, key)
			write_data(data_output, key)

camera.release()
cv2.destroyAllWindows()
