# Importing flask module in the project is mandatory
# An object of Flask class is our WSGI application.
from flask import Flask, jsonify
import serial
import time
  
# Flask constructor takes the name of 
# current module (__name__) as argument.
app = Flask(__name__)

# define port for serial transmission
port = serial.Serial('/dev/ttyUSB0', 115200, timeout=1)

# The route() function of the Flask class is a decorator, 
# which tells the application which URL should call 
# the associated function.
@app.route('/')
# ‘/’ URL is bound with hello_world() function.
def hello_world():
    return 'Welcome to RPi gateway. Use /lock and /unlock endpoints to lock and unlock the cycles.'

# lock endpoint. Transmits signal to LoRA module to lock a bike
@app.route('/lock/<bike_id>', methods=['GET'])
def lock():
    if request.method == 'GET':
        command = f'{bike_id}0'
        response = {'bike': bike_id}
        try:
            port.write(bytes(bike_id, 'utf-8'))
            response['success'] = 1
            # successful status response is 1
            return response, 1
        except:
            response['success'] = 0
            # unsuccessful status response is 0
            return response, 0


# unlock endpoint. Transmits signal to LoRA module to unlock a bike
@app.route('/unlock/<bike_id>', methods=['GET'])
def lock():
    if request.method == 'GET':
        command = f'{bike_id}1'
        response = {'bike': bike_id}
        try:
            port.write(bytes(bike_id, 'utf-8'))
            response['success'] = 1
            # successful status response is 1
            return response, 1
        except:
            response['success'] = 0
            # unsuccessful status response is 0
            return response, 0

# lock endpoint. Transmits signal to LoRA module to lock a bike
@app.route('/lock/<bike_id>', methods=['GET'])
def lock():
    bike_id = f'{bike_id}0'
    port.write(bytes(bike_id, 'utf-8'))

# main driver function
if __name__ == '__main__':
    # run() method of Flask class runs the application 
    # on the local development server.
    app.run()
