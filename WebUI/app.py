from flask import render_template, Flask,  request, Response, jsonify, session
import cv2
import requests
from flask_mysqldb import MySQL
import MySQLdb.cursors
from ultralytics import YOLO
import serial
import os

# Place /your/serial/port with your arduino usb or bluetooth connection serial port number 
# ser = serial.Serial('/your/serial/port', baudrate=9600)
# def sendCmd(command):
#    ser.write(command.encode('utf-8'))

#Sends command to esp8266 if presents
def send(command):
    try:
        response = requests.get(f"http://{ESP8266_IP}/{command}")
        print(response.text)
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")

#Starts an instance of Flask app object
app = Flask(__name__)

#Database access credentials
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = os.getenv('DB_UNAME')
app.config['MYSQL_PASSWORD'] = os.getenv('DB_PASSWORD')
app.config['MYSQL_DB'] = os.getenv('DB_NAME')
global_password = 'hellouser'

#MySQL Object started, ESP8266 address and port number it comes from are decleared, Trained uniform detection model is loaded
mysql = MySQL(app)
ESP8266_IP = "172.18.120.5"
ESP_PORT = 8080 
model = YOLO('./yolov5/runs/detect/train2/weights/last.pt')

#Access camera feed
def gen_frames():
  cap = cv2.VideoCapture(1)
  while True:
    success, frame = cap.read()
    if not success:
      break
    results = model(frame, verbose=False)[0]
    for result in results.boxes.data.tolist():
        x, y, x1, y1, score, class_id = result
        if score:
            cv2.rectangle(frame, (int(x), int(y)), (int(x1), int(y1)), (255,0,255), 4)
            cv2.putText(frame, results.names[int(class_id)].upper(), (int(x), int(y)), cv2.FONT_HERSHEY_COMPLEX, 1.3, (255,0,255), 3, cv2.LINE_AA)   
    success, buffer = cv2.imencode('.jpg', frame)
    frame = buffer.tobytes()
    
    yield (b'--frame\r\n'
           b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')

#Main "home" route of the web app, also the login page route if entered for the first time           
@app.route("/")
@app.route('/login', methods=['GET', 'POST'])
def login():
    msg = ''
    if request.method == 'POST' and 'username' in request.form and 'password' in request.form:
        username = request.form["username"]
        password = request.form['password']
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute('SELECT * FROM users WHERE username = % s AND password = % s', (username, password))
        account = cursor.fetchone()
        if account:
            return render_template('move.html')
        else:
            msg = "Incorrect password or username!"
    return render_template('login2.html', msg=msg)

#Handles registeration 
@app.route('/register', methods=['POST', 'GET'])
def register():
    msg = ''
    if request.method == 'POST' and 'username' in request.form and 'password' in request.form and 'email' in request.form:
       username = request.form['username']
       password = request.form['password']
       email = request.form['email']
       cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
       cursor.execute('SELECT * FROM users WHERE email = % s', (email, ))
       account = cursor.fetchone()
       
       if account:
          msg = 'Account with the email % s already exists', email
       
       else:
          cursor.execute('INSERT INTO users (username, password) VALUES (% s, % s)', (username, password, ))
          mysql.connection.commit()
          msg = 'Registration Completed!'
          return render_template('login2.html', msg=msg)       
    return render_template('register2.html', msg=msg)

#Receives commands sent from the UI
@app.route('/<command>', methods=['POST'])
def handle_command(command):
    send(command) # use this if connection is via WiFi (ESP8266) and comment out sendCmd()
    sendCmd(command) # use this if connection is via serial communication and comment out send()
    return "Command sent successfully!"

if __name__ == "__main__":
  app.run(debug=True)

#Streams camera feed to UI
@app.route('/video_feed/')
def video_feed():
    return Response(gen_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')
    
if __name__ == '__main__':
   app.run()
