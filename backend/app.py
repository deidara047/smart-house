from flask import Flask, jsonify, request
from flask_cors import CORS
from flask_socketio import SocketIO, send
from datetime import datetime

app = Flask(__name__)
CORS(app)

socketio = SocketIO(app, cors_allowed_origins="*")

# Estos datos (houseInfo) VIENEN de Arduino/Raspberry
# Están previamente guardados en Arduino/Raspberry
# Se van cambiando conforme se modifiquen en el Frontend y en Arduino/Raspberry
houseInfo = {
    "lights": {
        "room1": False,
        "room2": False,
        "livingRoom": False,
        "kitchen": False,
        "entrance": False
    },
    "lcd": {
        "upperText": "TextArriba",
        "lowerText": "TextAbajo"
    },
    "temperature": {
        "init": 0,
        "end": 100,
        "trigger": 40,
        "position": 0
    },
    "humidity": {
        "init": 0,
        "end": 100,
        "trigger": 40,
        "position": 0
    },
    "sound": {
        "init": 0,
        "end": 100,
        "trigger": 40,
        "position": 0
    },
    "isFire": False,
    "fan": False,
    "rotatingAd": False,
    "waterPump": False
}

# Estos datos (houseTrack) VIENEN de MongoDB
"""
"tableData": [{
        "action": "Apagar",
        "time": "12:23:24",
        "date": "28/08/2024"
    }]
"""
houseTrack = [{
    "myId": "room1",
    "name": "Cuarto 1",
    "tableData": []
},{
    "myId": "livingRoom",
    "name": "Sala",
    "tableData": []
},{
    "myId": "room2",
    "name": "Cuarto 2",
    "tableData": []
},{
    "myId": "isFire",
    "name": "Sensor de fuego",
    "tableData": []
},{
    "myId": "fan",
    "name": "Ventilador",
    "tableData": []
},{
    "myId": "kitchen",
    "name": "Cocina",
    "tableData": []
},{
    "myId": "entrance",
    "name": "Entrada",
    "tableData": []
},{
    "myId": "rotatingAd",
    "name": "Anuncio Rotante",
    "tableData": []
},{
    "myId": "waterPump",
    "name": "Bomba de agua",
    "tableData": []
}]

@app.route('/')
def index():
    return jsonify({
        "houseInfo": houseInfo,
        "houseTrack": houseTrack
    })
    
@app.route('/update_from_arduino_and_raspberry', methods=["POST"])
def update_data():
    houseInfo.update(request.get_json())
    socketio.emit('message', {"houseInfo": houseInfo})
    return jsonify(message="Datos del Arduino/Raspberry correctamente"), 200

@socketio.on('message')
def handle_message(message):
    print(f"Received message: {message}")
    object_to_return = None
    
    if message['part'][0:6] == "lights":
        houseInfo["lights"][message['part'][7:]] = message["state"]
        today_date = datetime.now().strftime("%d/%m/%Y")
        now_time = datetime.now().strftime("%H:%M:%S")
        houseTrackNewEntry = None
        
        for ht in houseTrack:
            if ht["myId"] == message['part'][7:]:
                dataToSave = {
                    "action": "Encender" if message["state"] == True else "Apagar",
                    "time": now_time,
                    "date": today_date
                }
                    
                ht["tableData"].append(dataToSave)
                houseTrackNewEntry = {
                    "myId": ht["myId"],
                    "tableData": dataToSave
                }
                break
        
        object_to_return = { "hsIn": {"lights": houseInfo["lights"]}, "hsTr": houseTrackNewEntry }
    elif message["part"] == "exit":
        object_to_return = { "exit": "exit" }
    elif message['part'][0:3] == "lcd":
        houseInfo["lcd"][message['part'][4:]] = message["state"]
        object_to_return = {"lcd": houseInfo["lcd"]}
    elif message['part'][0:6] == "sensor":
        houseInfo[message['part'][7:]]["position"] = message["state"]
        object_to_return = {message['part'][7:]: houseInfo[message['part'][7:]]}
    elif message['part'] == "clickedbutton":
        object_to_return = {"lastclickedbutton": message["state"]}
    else:
        houseInfo[message['part']] = message["state"]
        today_date = datetime.now().strftime("%d/%m/%Y")
        now_time = datetime.now().strftime("%H:%M:%S")
        houseTrackNewEntry = None
        
        for ht in houseTrack:
            if ht["myId"] == message['part']:
                dataToSave = {
                    "action": "Encender" if message["state"] == True else "Apagar",
                    "time": now_time,
                    "date": today_date
                }
                
                ht["tableData"].append(dataToSave)
                houseTrackNewEntry = {
                    "myId": ht["myId"],
                    "tableData": dataToSave
                }
                break
        object_to_return = { "hsIn": {message['part']: message["state"]}, "hsTr": houseTrackNewEntry }
    send(object_to_return, broadcast=True)

if __name__ == '__main__':
    socketio.run(app, host='0.0.0.0', port=5000, debug=True)
