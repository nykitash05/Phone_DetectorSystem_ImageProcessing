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

def calculatingaccuracy():
    orgfile = glob.glob(sys.argv[1][2:]+'/*.txt')
    filepath = "outputstats.txt"
    result = open("result.txt","w+")
    result.write("Filename\t" + "X\t" +"Y\t" + "Accepted/Not Accepted \n")
    count = orgcount = 0
    with open(orgfile[0]) as file1:
        org = [line.rstrip('\n').split(' ') for line in file1]
    file1.close() 
    with open(filepath) as file2:
        next(file2)
        for line in file2:
            orgcount = orgcount+1
            test = line.rstrip('\n').split('\t')
            res = [org[i] for i in range(len(org)) if (test[0] == org[i][0])]
            if res:
                if ((float(res[0][1])-0.05 <=float(test[1])<= float(res[0][1])+0.05) or (float(res[0][1]) -0.05 <=float(test[2])<= float(res[0][1])+0.05)):
                    var = 'Accepted'
                    count = count+1
                else:
                    var = 'Not Accepted'
            else:
                var = 'N'
            result.write(  line.rstrip('\n') + '\t' + var + '\n')
        Accuracy = round((count/orgcount) * 100 , 3)
        result.write("Model gives " + str(Accuracy) + "% accurate result of the prediction")
    file2.close() 
    result.close()   
    



def main():
    #Read image path
    images = glob.glob(sys.argv[1][2:]+'/*.jpg')
    
    # Looping through each image
    file = open("outputstats.txt","w+")
    file.write("Filename\t" + "X\t" +"Y\n")
    for im in images:
        with open(im, 'rb') as file:
            image = Image.open(file)
            h,w = image.height,image.width
            image = cv2.cvtColor(np.array(image), cv2.COLOR_RGB2BGR)
            gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
            ret,thresh = cv2.threshold(gray,67,250,0)
            thresh = cv2.dilate(thresh, None)  # fill some holes
            thresh = cv2.dilate(thresh, None)
            thresh = cv2.erode(thresh, None)   # dilate made our shape larger, revert that
            thresh = cv2.erode(thresh, None)
            contours, hierarchy = cv2.findContours(thresh, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
            rc = cv2.minAreaRect(contours[0])
            box = cv2.boxPoints(rc)
            box = np.int0(box)
            cv2.drawContours(image,[box],0,(0,255,0),2)
            centre = [rc[0][0]/w, rc[0][1]/h]
            filename = im.split('\\')[1]
            plt.imsave ('outputimage/'+ filename , image)
            file = open("outputstats.txt","a")
            file.write(filename + '\t' + str(math.ceil(centre[0] * 10000.0) / 10000.0) + '\t' + str(math.ceil(centre[1] * 10000.0) / 10000.0) + '\n')
    file.close()
    
    calculatingaccuracy()
main()