from flask import render_template, Flask,  request, Response, jsonify, session
import cv2
import serial #python3 -m serial.tools.list_ports
import torch
from yolov5 import detect
import ollama as ol
from flask_mysqldb import MySQL
import MySQLdb.cursors
import re

#ser = serial.Serial('/dev/ttyUSB0', baudrate=9600)
# def sendCmd(command):
#    ser.write(command.encode('utf-8'))

app = Flask(__name__)
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'swam'
app.config['MYSQL_PASSWORD'] = 'swam123'
app.config['MYSQL_DB'] = 'iotDB1'

mysql = MySQL(app)

model = torch.hub.load('ultralytics/yolov5', 'yolov5s', pretrained=True)

def gen_frames():
  cap = cv2.VideoCapture(1)
  while True:
    success, frame = cap.read()
    if not success:
      break
      
    results = model(frame)
    frame = results.render()[0]

    labels = results.pandas().xyxy[0]['name'].tolist()
    confidences = results.pandas().xyxy[0]['confidence'].tolist()
    
    if confidences:
        global label
        max_conf_idx = confidences.index(max(confidences))
        label = str(labels[max_conf_idx])
        
    ret, buffer = cv2.imencode('.jpg', frame)
    frame = buffer.tobytes()
    
    yield (b'--frame\r\n'
           b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')
           
@app.route("/")
@app.route('/login', methods=['GET', 'POST'])
def login():
    msg = ''
    if request.method == 'POST' and 'username' in request.form and 'password' in request.form:
       username = request.form['username']
       password = request.form['password']
       cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
       cursor.execute('SELECT * FROM users WHERE username = % s AND password = % s', (username, password, ))
       account = cursor.fetchone()
       if account:
          session['loggedin'] = True
          session['username'] = account['username']
          msg = 'Logged in successfully!'
       else:
          msg = "Incorrect password or username"
    return render_template('login.html', msg=msg)

@app.route('/<command>', methods=['POST'])
def handle_command(command):
    # Handle the command here (e.g., print it)
    if command == 'i':
        result = ol.chat(model="tinyllama", messages=[{ "role": "user", "content": "Hi"}])
        response = result["message"]["content"]
        print(response)
    print(f"Received command: {command}")
    return f"Command '{command}' received!"
    
@app.route('/video_feed/')
def video_feed():
    return Response(gen_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')
    
@app.route('/register', methods=['POST', 'GET'])
def register():
   pass
    
if __name__ == '__main__':
   app.run()
