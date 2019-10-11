import Tkinter as tk
from PIL import Image, ImageTk
import cv2

print('Starting data collector')

camera = cv2.VideoCapture(0)
cv2.namedWindow("Data Capture")

count = 0
ret = True
while ret:
	ret, frame = camera.read()
	cv2.imshow("Data Capture", frame)
	if k%256 == 27:
		break
	elif k%256 == 32:
		img = f"{count.zfill(5)}.png"
		cv2.imwrite(img, frame)
		print(f'Wrote to file {count.zfill(5)}.png')
		img += 1
camera.release()
cv2.destroyAllWindows()