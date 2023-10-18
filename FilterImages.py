import os
import cv2 as cv
import numpy as np
import pandas as pd

FOLDER = r'Crops\YES'
THRESHOLD = 107667200

images = [os.path.join(FOLDER, i) for i in sorted(os.listdir(FOLDER))]

# brightness = [np.sum(cv.imread(i)) for i in images]
# brightness = pd.DataFrame({'brightness': brightness})
# print(brightness.describe())

for img_path in images:
    img = cv.imread(img_path)
    img = np.sum(img)
    if img < THRESHOLD:
        print(img_path)
        os.remove(img_path)
