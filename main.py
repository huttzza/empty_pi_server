from flask import Flask, render_template, send_file, request, redirect,url_for
from picamera import PiCamera
from time import sleep

app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello World'

@app.route('/images')
def images():
    camera = PiCamera()
    img_name = '/home/pi/capture/static/image/test.jpg'
    camera.capture(img_name)
    camera.close()
    print("captured")
    return redirect(url_for('static', filename='image/test.jpg'))
    #return "<img src='static/image/test.jpg'>"

if __name__ == '__main__':
    app.run(debug=True,port=80, host='0.0.0.0')
