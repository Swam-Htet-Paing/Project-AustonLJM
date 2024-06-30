from flask import render_template, Flask,  request, Response, jsonify
import cv2
import serial #python3 -m serial.tools.list_ports
import torch
from yolov5 import detect
import ollama as ol

#ser = serial.Serial('/dev/ttyUSB0', baudrate=9600)
# def sendCmd(command):
#    ser.write(command.encode('utf-8'))

app = Flask(__name__)
model = torch.hub.load('ultralytics/yolov5', 'yolov5s', pretrained=True)
label = "Hi"
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
def index():
    global label
    return render_template('page.html', msg=label)

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
    
@app.route('/get_slider_value', methods=['POST'])
def get_slider_value():
    slider_value = request.json.get('slider_value')
#    sendCmd(slider_value)
    return slider_value
    
if __name__ == '__main__':
   app.run()
