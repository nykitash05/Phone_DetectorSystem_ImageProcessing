# Object Detection System
The task is to find a location of a phone dropped on the floor in a single RGB camera image.

# Introduction
This repository is created to design a prototype of a visual object detection system for a customer. You don't need a large dataset here to train your model. The solution designed can be implemented on any image to see the result. However we have used a small dataset of 100 images to test the accuracy of our model.

# Problem Statement:
To design a prototype of a phone detection system to get the location(centre coordinates) of the phone dropped on the floor in a single RGB camera image.

# Solution:

The protoype has been designed using python programming languages with OpenCV to help us perform image processing. This code has been tested on Windows Terminal only. In the repository you will find two .py files:
1) train_phone_finder.py : This file is executed using- 'python train_phone_finder.py ~/find_phone' command from terminal so this will read all the images in the 'find_phone' folder and calculate centre cordinates for each of the images and write it in a text file named- outputstats.txt. It would also give us a visual image of the original image with bounding box around the object it has detected. This provision will help us to see at a glance whether correct object was detected or not. The output images with bounding boxes will be stored in 'outputimage' folder.
			 This file also has a function called as calculatingaccuracy(). This function will compare the results obtained by our model and the original results in the 'label.txt' file under 'find_phone' folder and give us another text file named- 'result.txt' with results of whether the coordinates were within the acceptable range of +- 0.05 or not and at the end gives the accuracy score of how many images were detected correctly.
Eg:
Filename	X	Y	Accepted/Not Accepted 
0.jpg	0.8338	0.1301	Accepted
1.jpg	0.8377	0.5032	Accepted
10.jpg	0.4888	0.4249	Accepted
103.jpg	0.499	0.4985	Not Accepted
Model gives 77.519% accurate result of the prediction

2) find_phone.py : This file is called using - 'python find_phone.py ~/find_phone_test_images/52.jpg' command from terminal. This is our script to get results for our test images. As there is only one image being passed. The output of the centre coordinates will be returned back in the console. 
Eg:
C:\Users\nykit\OneDrive\Desktop\My_Work\Brain_Corp\find_phone_task_4> python find_phone.py ~/find_phone_test_images/52.jpg
0.5448  0.2821

# Program execution can be done using following steps:

1) Download the repository at a location in your computer.
2) Open your terminal window and verify you have latest versions of python and pip installed. If not install them first.
3) Go to the directory where your files from this repository exists. If you try to execute the first .py file you may get an error saying no module named cv2. So we need to execute following three commands:
	pip install opencv-python
	pip install Pillow
	pip install matplotlib
4) Run 'python train_phone_finder.py ~/find_phone' command in terminal and wait for ~4 seconds to check the results.
5) Observe the results in outputimage folder and result.txt file.
6) Run python 'find_phone.py ~/find_phone_test_images/52.jpg' command in terminal and observe the results in console.

# Assumptions:
1) The code will be run in the given format i.e. 'find_phone.py ~/find_phone_test_images/52.jpg' only as ~/ is not needed here in windows terminal execution so this has been appended in the code. 
2) This code will be tested on Windows terminal only. This code may have to be changes slightly to be executed on other systems
