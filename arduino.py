from flask import Flask, request
import serial

app = Flask(__name__)

# Arduino setup (you need to adjust the port and baudrate based on your setup)
arduino = serial.Serial('COM_PORT', 9600)

@app.route("/send_data", methods=["POST"])
def send_data_to_arduino():
    data = request.json
    prediction = data.get('prediction')
    
    if prediction == 1:
        arduino.write(b'1')  # Send '1' to Arduino to turn on the LED
    else:
        arduino.write(b'0')  # Send '0' to Arduino to turn off the LED

    return "Data sent to Arduino", 200

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")
