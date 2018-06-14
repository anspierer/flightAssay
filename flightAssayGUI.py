#! /usr/bin/python

## Flight Assay -- Script 1 of 3
## For Raspberry Pi with PiCamera
## Takes a standardized picture of final flight assay film
## Also useful for taking standardized pictures with Raspberry Pi and PiCamera
## Use this script if going headless/without a monitor
## Written by Adam Spierer -- June 2018
## Modified from: http://smokespark.blogspot.com/2015/05/a-python-graphical-user-interface-for.html
## Accessed Feb 15, 2018

from   Tkinter import *
import time
import picamera 
import numpy as np
import io
import os
import os.path
from   datetime import datetime, timedelta

homeFolder = '~/flightAssay/'
camera = picamera.PiCamera()
previewTime = 4 

try:
	os.mkdir(homeFolder)
os.chdir(homeFolder)

# Where to place the center of the GUI window
def centre_window(w, h):
	ws = root.winfo_screenwidth()
	hs = root.winfo_screenheight()
	x = 1615 #(ws/2) -100
	y = 35 # (hs/2) - 0 
	root.geometry('%dx%d+%d+%d' % (w, h, x, y))

# Preview function to confirm frame of view
def preview():
#	camera.rotation = 180 # Rotates image if camera is upside down
	camera.resolution = (960,1280)
	camera.video_stabilization = True
	camera.start_preview()
	time.sleep(previewTime) # Change previewTime on line 22
	camera.stop_preview()
	return

# Entry fields for file name and experiment descriptors
def show_entry_fields():
   geno = e1.get()
   sex = e2.get()
   cond = e3.get()
   fileName = geno + '_' + sex + '_' + cond + '.jpg'
   return geno,sex,fileName

# Function to capture image and name file
def still():
	geno = e1.get()
	sex = e2.get()
   	cond = e3.get()
	fileName = geno + '_' + sex + '_' + cond + '.jpg'
	if os.path.exists(fileName) == False:
	   	camera.preview_fullscreen = False
		camera.brightness = 60
#		camera.rotation = 180 # Rotates image if camera is upside down
	#	camera.preview_window = (0, 0, 960, 1280)
		camera.resolution = (960,1280)
		fileName = homeFolder + show_entry_fields()[2]
		print 'Capturing: ', fileName
		camera.capture(fileName)
		camera.stop_preview()
	else:
		reEnter = 'File exists, is this a duplicate (y) or accident (n)?' # In future commits, this will make sure there are no duplicates...but until then, don't mess up?
		

root = Tk()
root.title("flightCamera")
centre_window(300, 200)

# Quit button
quitButton = Button(root, bg="pink", text="       Quit      ", command=exit)
quitButton.grid(row=0, column=0)

# Preview button
previewButton = Button(root, text="    Preview    ", command=preview)
previewButton.grid(row=0, column=1)

# Displays the path
pathButton = Label(root, text = 'homeFolder:', ).grid(row=2, column=0)
pathButton = Label(root, text = homeFolder).grid(row=2, column=1)

# Experiment detail entry 1: Genotype
Label(root, text="Geno").grid(row=3)
e1 = Entry(root)
e1.grid(row=3, column=1)

# Experiment detail entry 2: Sex
Label(root, text="Sex").grid(row=4)
e2 = Entry(root)
e2.grid(row=4, column=1)

# Experiment detail entry 3: Condition
Label(root, text="Cond").grid(row=5)
e3 = Entry(root)
e3.grid(row=5, column=1)

# Capture button
takeStillButton = Button(root, bg="#66ff99", text="   Capture  ", command=still)
takeStillButton.grid(row=6, column = 1)

root.mainloop()