from flask import render_template, Flask,  request, Response
import cv2
import serial #python3 -m serial.tools.list_ports

#ser = serial.Serial('/dev/ttyUSB0', baudrate=9600)

app = Flask(__name__)

# def sendCmd(command):
#    ser.write(command.encode('utf-8'))

def gen_frames():
  cap = cv2.VideoCapture(1)
  while True:
    success, frame = cap.read()
    if not success:
      break
    
    ret, buffer = cv2.imencode('.jpg', frame)
    frame = buffer.tobytes()
    yield (b'--frame\r\n'
           b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')
           
@app.route("/")
def index():
    return render_template('page.html')

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
