import cv2
import serial,time

cap = cv2.VideoCapture('in.avi')


human_cascade = cv2.CascadeClassifier('haarcascade_fullbody.xml')

ArduinoSerial=serial.Serial('com7',9600,timeout=0.1)
#out= cv2.VideoWriter('face detection4.avi',fourcc,20.0,(640,480))
time.sleep(1)

while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()

    # Our operations on the frame come here
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    humans = human_cascade.detectMultiScale(gray, 1.9, 1)
    
    # Display the resulting frame
    for (x,y,w,h) in humans:
         cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),2)
         #if detected anything then it will put frame around it by above statement 
         #and below statement will respondst this to arduino where it could be read
         print("detected")
         
         #ArduinoSerial.write(string.encode('utf-8'))
         ArduinoSerial.write('x')
         
         #time.sleep(0.05)

    cv2.imshow('frame',frame)
    
    '''for testing purpose
    read= str(ArduinoSerial.readline(ArduinoSerial.inWaiting()))
    time.sleep(0.05)
    print('data from arduino:'+read)
    '''

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()
