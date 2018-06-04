import cv2
import os
from flask import Flask,render_template,url_for, request

app = Flask(__name__)



@app.route('/')
def index():
    return ("Hello world"+"<a href='/face'>Face Recognition</a>")

@app.route('/face')
def face_recog():
 face_csc = cv2.CascadeClassifier("frontfaceharscade.xml")
 cam = cv2.VideoCapture(0)  
 while(True):
    tf, img= cam.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_csc.detectMultiScale(gray,1.1,4)
    for(x,y,w,h) in faces:
      cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,0),5)
      cv2.imshow('img',img)
      #key = cv2.waitKey(1)
      #if key == 1:
       # break
      if cv2.waitKey(1)& 0xFF == ord('s'):
        cv2.imwrite('test.jpg',image)
        break
        cam.release()
        cv2.destroyAllWindows()

@app.route('/close')
def close():
  cam = cv2.VideoCapture(0)
  cam.release()
  cv2.destroyAllWindows()
   
app.run(host='0.0.0.0', port='8080')

