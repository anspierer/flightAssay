#! /usr/bin/python

## Flight Assay -- Script 1 of 3
## For Raspberry Pi with PiCamera
## Takes a standardized picture of final flight assay film
## Use this script if going headless/without a monitor
## Written by Adam Spierer -- June 2018

import os
import time
import picamera

# Setting up a folder. This can be changed
homeFolder = "~/flightAssay/"
try:
	os.mkdir(homeFolder)
os.chdir(homeFolder)

# Function to preview field of view
def previewer():
	delayTime = 0.1
	while delayTime != 0:
		camera.resolution = (960,1280)
#		camera.rotation = 180
		camera.start_preview()
		time.sleep(delayTime)
		camera.stop_preview()
		delayTime = raw_input('Preview time (0 to exit)')
		if delayTime == '':
			delayTime = 0
		else:
			delayTime = float(delayTime)
	print 25*'-'

# Function to capture the image
def capture(fileName):
	with picamera.PiCamera() as camera:
		camera.resolution = (960,1280)
#		camera.rotation = 180
		camera.brightness = 60 # User should find a value that works
		camera.start_preview() # Displays the image that is being captured
		camera.capture(fileName)
		camera.stop_preview()
		print 'File: %s captured!' % fileName
	print 25*'='

# Allows for prolonged framing of new set ups
with picamera.PiCamera() as camera:
	while move_on == False:
		move_on = previewer()

# Main loop to name and capture images
while True:
	geno = str(raw_input('Genotype:  '))
	sex  = str(raw_input('Sex:       '))
	cond = str(raw_input('Condition: '))
	fileName = homeFolder + geno + '_' + sex + '_' + cond + '.jpg'
	capture(geno,sex,fileName)
	
## Exit program by pressing control + 'c'
