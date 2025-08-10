from flask import Flask, render_template, Response
from flask_ngrok import run_with_ngrok
import urllib
import cv2
import numpy as np
from ultralytics import YOLO
import telegram
import asyncio
import nest_asyncio
import re
import datetime
import os

app = Flask(__name__)
# run_with_ngrok(app)

model_detect = YOLO('yolov8n.pt')
root = "C:/Users/Buu/PycharmProjects/Video_streaming_flask_ngrok/New_Faces/"

nest_asyncio.apply()
my_token = "7485186086:AAG6T4-iMv9LfQpytTfKjHYxmYPgeyWy3R8"
bot = telegram.Bot(token=my_token)

@app.route("/")
def index():
    return render_template("index.html")

def frame_from_webcam():
    while True:
        try:
            responce = urllib.request.urlopen("http://192.168.1.245/capture?")
            img = np.array(bytearray(responce.read()), np.uint8)
            # frame = cv2.VideoCapture()
        except:
            print("Disconnect")
            continue
        frame = cv2.imdecode(img, -1)
        results = model_detect.track(frame)
        if len(results[0])>0:
            classes_name = results[0].names
            for i in range(len(results[0])):
                box = results[0].boxes[i]
                cls = int(box.cls[0])
                name = classes_name[cls]
                if name == 'person' and box.conf[0] > 0.7:
                    [x_min,y_min,x_max,y_max] = box.xyxy[0]
                    x_min,y_min,x_max,y_max = int(max(0,x_min)),int(max(0,y_min)),int(min(frame.shape[1],x_max)),int(min(frame.shape[0],y_max))
                    name_object = '_'.join(re.split("[:.]",f'{datetime.datetime.now()}')) + "_" + str(i) + ".jpg"
                    path = os.path.join(root,name_object)
                    cv2.imwrite(path,frame[y_min:y_max,x_min:x_max])
                    cv2.rectangle(frame,(x_min,y_min),(x_max,y_max),(0,255,0))
                    cv2.putText(frame,name,(x_min+5,y_min+5),cv2.FONT_ITALIC,0.5,(0,255,0),2)
                    asyncio.run(bot.sendPhoto(chat_id = "XXX", photo = open(path,'rb'), caption = "Phát hiện chuyển động"))
                    asyncio.run(bot.sendPhoto(chat_id = "XXX", photo = open(path,'rb'), caption = "Phát hiện chuyển động"))
            img = np.array(cv2.imencode(".jpg",frame)[1])
            yield b'Content-Type: image/jpeg\r\n\r\n' + bytearray(img) + b'\r\n--frame\r\n'

        else:
            yield b'Content-Type: image/jpeg\r\n\r\n' + bytearray(img) + b'\r\n--frame\r\n'

@app.route("/image_feed")
def image_feed():
    return Response(frame_from_webcam(), mimetype="multipart/x-mixed-replace; boundary=frame")

if __name__ == "__main__":
    #app.run(host='0.0.0.0', debug=False)
    app.run()