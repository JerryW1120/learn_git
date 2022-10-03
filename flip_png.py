import cv2
import os

png_dir = '/Users/jerryw/Desktop/fix'
for pic in os.listdir(png_dir):
    png = os.path.join(png_dir, pic)
    a = cv2.imread(png)
    a = cv2.flip(a, 1, dst = None)
    cv2.imwrite(png, a)

print("success")

