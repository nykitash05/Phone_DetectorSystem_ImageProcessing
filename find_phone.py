#Author  : Nikita Sharma
#Date    : 29th February 2020
#Purpose : To implement a prototype of a visual phone detection system for a customer

import cv2
from PIL import Image
import glob
import sys
import numpy as np
import matplotlib.pyplot as plt
import math


def main():
    #Read image path for sysin
    images = glob.glob(sys.argv[1][2:])                              # Append ~/ and read file name from command prompt
    for im in images:
        with open(im, 'rb') as file:                                 # Open Image to read
            image = Image.open(file)
            h,w = image.height,image.width
            image = cv2.cvtColor(np.array(image), cv2.COLOR_RGB2BGR) # Convert RGB to BGR
            gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)           # Convert RGB to GRAY
            ret,thresh = cv2.threshold(gray,67,250,0)                # To filter phone image from background of tiles/floor
            thresh = cv2.dilate(thresh, None)                        # fill some holes
            thresh = cv2.dilate(thresh, None)
            thresh = cv2.erode(thresh, None)                         # dilate made our shape larger, revert that
            thresh = cv2.erode(thresh, None)
            contours, hierarchy = cv2.findContours(thresh, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
            rc = cv2.minAreaRect(contours[0])
            centre = [rc[0][0]/w, rc[0][1]/h]
            sys.stdout.write(str(round(centre[0] ,4)) + "  " + str(round(centre[1] ,4)))
  
main()
