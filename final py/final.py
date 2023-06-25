import cv2
import numpy as np
import serial,time

import imutils

# Importing twilio library for sending sms
import os
from twilio.rest import Client

# Setting the environment variables
TWILIO_ACCOUNT_SID = 
TWILIO_AUTH_TOKEN = 

# Creating a twilio client
account_sid = 
auth_token = 
client = Client(account_sid, auth_token)

# Initializing the gun cascade classifier
gun_cascade = cv2.CascadeClassifier('guncascade.xml')

# Load the cascade
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

# Initializing the flags
firstFrame = None
gun_exist = False
cnt = 0

# To capture video from webcam. 
# Initializing the camera
camera = cv2.VideoCapture(0)

# To use a video file as input 
# cap = cv2.VideoCapture('filename.mp4')

#ArduinoSerial = serial.Serial(port='COM4', baudrate=9600, timeout=.1)


while True:
    # Reading the frame from the camera
    ret, frame = camera.read()

    # Checking if the frame is None
    if frame is None:
        break

     # Resizing the frame
    frame = imutils.resize(frame, width=500)

   
 # Converting the frame to grayscale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Detect the faces
    faces = face_cascade.detectMultiScale(gray, 1.1, 4)

     # Detecting guns in the grayscale frame
    gun = gun_cascade.detectMultiScale(gray, 1.3, 20, minSize=(100, 100))
    print("cascase = ", len(gun))

        # Checking if any guns are detected
    if len(gun) > 0:
        gun_exist = True
        cnt =cnt+ 1
    else:
        cnt = 0
        gun_exist = False

    # Looping over the gun detections
    for (x, y, w, h) in gun:

        # Initializing the roi_gray and roi_color variables
        roi_gray = gray[y:y + h, x:x + w]
        roi_color = frame[y:y + h, x:x + w]

        # Drawing a rectangle around the gun detection
        frame = cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)


    # Draw the rectangle around each face and switch on the light
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x+w, y+h),  (255, 0, 0), 2)
        #ArduinoSerial.write('x'.encode('utf-8'))
        print("face detected")
#        time.sleep(1)

     # Checking if the first frame is None
    if firstFrame is None:
        firstFrame = gray
        continue

    # Checking if a gun is detected and the counter is less than or equal to 2
    if gun_exist and cnt == 1:
        print("Guns detected" , cnt)
        message = client.messages.create(
            body="""
            ALERT: HIGH,
            CRIME: GUNS detected,
            LOCATION:Maharaja Agrasen Institute Of Technology 
                         """,
            from_='whatsapp:+14155238886',
            to='whatsapp:+917838584710'
        )
        
    #ArduinoSerial.write('y'.encode('utf-8'))
    #print("false")
    # Display
    cv2.imshow('img', frame)

    # Getting the key pressed by the user
    key = cv2.waitKey(1) & 0xFF
    # Checking if the user pressed the q key
    if key == ord('q'):
        break
        
# Releasing the camera
camera.release()

# Destroying all the windows
cv2.destroyAllWindows()
