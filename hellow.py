from flask import Flask, render_template, request
import serial
import time

app = Flask(__name__)

# Cambia 'COM3' por el puerto al que tu Arduino esté conectado.
try:
    arduino = serial.Serial('/dev/cu.usbserial-1330', 9600)
except:
    print("No se pudo conectar a '/dev/ttyACM0'")

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/control_motor", methods=["POST"])
def control_motor():
    try:
        direccion = request.form["direccion"]
        if direccion == "izquierda":
            arduino.write(b'i')# Suponiendo que 'L' hace girar a la izquierda
            print('izquierda')
        elif direccion == "pausa":
            arduino.write(b's')  # Suponiendo que 'S' detiene el motor
            print('pausa')
        elif direccion == "derecha":
            arduino.write(b'd')  # Suponiendo que 'R' hace girar a la derecha
            print('derehca')        
        return ("", 204)
    except:
        print("Error")
        return ("23", 500)

if __name__ == "__main__":
    app.run(debug=True)