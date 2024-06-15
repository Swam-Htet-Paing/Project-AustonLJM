from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# Global counter variable
counter = 0

@app.route('/')
def control_template():
    global counter
    return render_template('page.html', num=counter)

@app.route('/<command>')
def cmd(command):
    global counter
    if command == 'w':
        counter += 1
        return jsonify({'num': counter})
    else:
        return jsonify({'error': 'wrong command'}), 400

if __name__ == '__main__':
    app.run(debug=True)