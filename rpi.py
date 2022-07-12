import cv2
import numpy as np
import os
import model
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setup(4,GPIO.OUT)

def lockdown():
    GPIO.output(4,GPIO.HIGH)

def unlock():
    GPIO.output(4, GPIO.LOW)
