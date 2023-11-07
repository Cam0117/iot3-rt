import pyrebase

config = {
  "apiKey": "AIzaSyDFlZ9j2-p6EjsYt-f9KWMnmi5waSoRpDk",
  "authDomain": "iot-rt-254b2.firebaseapp.com",
  "databaseURL": "https://iot-rt-254b2-default-rtdb.firebaseio.com/",
  "storageBucket": "iot-rt-254b2.appspot.com"
}

firebase = pyrebase.initialize_app(config)