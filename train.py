# University of Iowa Hackathon
# TensorFlow and Keras ASL Convolutional Neural Network

import numpy as np
import keras
#import cv2
import matplotlib.pyplot  as plt
from keras.datasets import mnist
from keras.models import Sequential, load_model
from keras.layers import Dense, Dropout, Flatten
from keras.utils import np_utils
from keras.layers.convolutional import MaxPooling2D, Conv2D

load_existing_model = True

conv = 'abcdefghijklmnopqrstuvwxyz'

def load_data_from_file(filename):
	x_data = []
	y_data = []
	with open(filename) as f:
		for n, line in enumerate(f):
			if n:
				data = line.strip().split(',')[1:]
				parsed_image = [[int(p) for p in data[i*28:(i+1)*28]] for i in range(28)]
				x_data.append(parsed_image)
				y_data.append(line.strip().split(',')[0])
	return np.asarray(x_data), np.asarray(y_data)

print('Loading image data')
x_train, y_train = load_data_from_file('training_data/mnist/sign_mnist_train.csv')
x_test, y_test = load_data_from_file('training_data/mnist/sign_mnist_test.csv')
print('Loaded image data')

def train_model(x_train, y_train, x_test, y_test):
	x_train = x_train.reshape((x_train.shape[0], 28, 28, 1)).astype('float32')
	x_test = x_test.reshape((x_test.shape[0], 28, 28, 1)).astype('float32')

	x_train = x_train / 255
	x_test = x_test / 255

	y_train = np_utils.to_categorical(y_train)
	y_test = np_utils.to_categorical(y_test)
	num_classes = y_test.shape[1]

	def larger_model():
		model = Sequential()
		model.add(Conv2D(30, (5, 5), input_shape=(28, 28, 1), activation='relu'))
		model.add(MaxPooling2D())
		model.add(Conv2D(15, (3, 3), activation='relu'))
		model.add(MaxPooling2D())
		model.add(Dropout(0.2))
		model.add(Flatten())
		model.add(Dense(128, activation='relu'))
		model.add(Dense(50, activation='relu'))
		model.add(Dense(num_classes, activation='softmax'))
		model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])
		return model
	model = larger_model()
	model.fit(x_train, y_train, validation_data=(x_test, y_test), epochs=10, batch_size=200)
	scores = model.evaluate(x_test, y_test, verbose=0)
	print("Finished training new large CNN model with error rate: %.2f%%" % (100-scores[1]*100))
	print("Saving training model...")
	model.save('trained_model.h5')
	print("Saved to trained_model.h5")
	return model

if load_existing_model:
	print('Loading trained model from file trained_model.h5')
	model = load_model('trained_model.h5')
	print('Loaded model from file')
else:
	print('Training new model')
	model = train_model(x_train, y_train, x_test, y_test)

"""
plt.subplot(221)
plt.imshow(x_test_original[4], cmap=plt.get_cmap('gray'))
plt.subplot(222)
plt.imshow(x_test_original[5], cmap=plt.get_cmap('gray'))
plt.subplot(223)
plt.imshow(x_test_original[6], cmap=plt.get_cmap('gray'))
plt.subplot(224)
plt.imshow(x_test_original[7], cmap=plt.get_cmap('gray'))
# show the plot

#print([conv[int(i)] for i in y_test[:4]])
print([conv[np.argmax(prediction)] for prediction in model.predict(x_test[4:8])])
plt.show()
"""