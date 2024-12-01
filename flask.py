from flask import Flask, request
import serial

app = Flask(__name__)

# Configure the serial port for Arduino (example)
arduino = serial.Serial('COM_PORT', 9600)  # Adjust COM port accordingly

@app.route('/send_data', methods=['POST'])
def send_data_to_arduino():
    data = request.json.get('prediction')  # Get prediction (1 for human detected, 0 for no human)
    if data == 1:
        arduino.write(b'1')  # Turn on the LED
    else:
        arduino.write(b'0')  # Turn off the LED
    return "Data sent to Arduino"

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
