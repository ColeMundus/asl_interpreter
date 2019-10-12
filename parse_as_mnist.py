import glob
import cv2
import matplotlib.pyplot as plt
from keras.models import Sequential, load_model
import numpy as np

conv = 'abcdefghijklmnopqrstuvwxyz'

model = load_model('trained_model.h5')
file_list = glob.glob(f'training_data/capture/original_images/*.png')
for file in file_list:
	print(file)
	img = cv2.imread(file)
	frame = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
	downscale = cv2.resize(frame, (28, 28), interpolation=cv2.INTER_LINEAR)
	x_data = [downscale]
	x_data = np.asarray(x_data)
	x_data = x_data.reshape((x_data.shape[0], 28, 28, 1)).astype('float32')
	print([conv[np.argmax(prediction)] for prediction in model.predict(x_data)])
	cv2.imshow('image', downscale)
	cv2.waitKey(0)
	#
	#plt.subplot(221)
	#plt.imshow(img, cmap=plt.get_cmap('gray'))