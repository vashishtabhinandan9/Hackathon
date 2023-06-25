import numpy as np
import cv2
import imutils
import datetime

# Importing twilio library for sending sms
import os
from twilio.rest import Client

# Setting the environment variables
TWILIO_ACCOUNT_SID = 'AC1c0a96e3d7f4756b98d4045b5b5164f0'
TWILIO_AUTH_TOKEN = '4e63908efa23a4f5429c1e9de0b9ac9b'

# Creating a twilio client
account_sid = 'AC1c0a96e3d7f4756b98d4045b5b5164f0'
auth_token = '4e63908efa23a4f5429c1e9de0b9ac9b'
client = Client(account_sid, auth_token)

# Initializing the gun cascade classifier
gun_cascade = cv2.CascadeClassifier('guncascade.xml')

# Initializing the camera
camera = cv2.VideoCapture(0)

# Initializing the flags
firstFrame = None
gun_exist = False
cnt = 0

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
        
    
        #cv2.imshow(" ",frame)
        #break

    # Displaying the frame
    cv2.imshow(" ", frame)

    # Getting the key pressed by the user
    key = cv2.waitKey(1) & 0xFF

    # Checking if the user pressed the q key
    if key == ord('q'):
        break

# Releasing the camera
camera.release()

# Destroying all the windows
cv2.destroyAllWindows()