import tkinter as tk
from PIL import Image
import cv2

print('Starting data collector')

camera = cv2.VideoCapture(0)
cv2.namedWindow("Data Capture")

count = 0
ret = True
while ret:
	ret, frame = camera.read()
	cv2.imshow("Data Capture", frame)
	k = cv2.waitKey(1)
	if k%256 == 27:
		break
	elif k%256 == 32:
		img = f"training_data/capture/{str(count).zfill(5)}.png"
		cv2.imwrite(img, frame)
		print(f'Wrote to file '+img)
		count += 1
camera.release()
cv2.destroyAllWindows()
