import time
import pyrebase
import random
#from pyjoystick.sdl2 import Key, Joystick, run_event_loop
import smbus
# Get I2C bus
bus = smbus.SMBus(1)

# SHT31 address, 0x44(68)
#bus.write_i2c_block_data(0x44, 0x2C, [0x06])

time.sleep(0.5)
#config = {
#  "apiKey": "apiKey",
#  "authDomain": "mobilerobotgh-eb60a.firebaseapp.com",
#  "databaseURL": "https://databaseName.firebaseio.com",
#  "storageBucket": "mobilerobotgh-eb60a.appspot.com"
#}

config = {
  "apiKey": "AIzaSyAUK_-9jzfpKwkj1yPlUvnIzNrjwmT13Sc",
  "authDomain": "trymobilerobot.firebaseapp.com",
  "databaseURL": "https://trymobilerobot-default-rtdb.asia-southeast1.firebasedatabase.app/",
  "storageBucket": "trymobilerobot.appspot.com"
}

firebase = pyrebase.initialize_app(config)

# Get a reference to the auth service
#auth = firebase.auth()
te= 0
rh =0
# Log the user in
#user = auth.sign_in_with_email_and_password('cs.belajarobot@gmail.com', '12345abcde')

# Get a reference to the database service
#"nilai"
def bacaSensor():
    bus.write_i2c_block_data(0x44, 0x2C, [0x06])

    time.sleep(0.5)

    data = bus.read_i2c_block_data(0x44, 0x00, 6)
    # Convert the data
    temp = data[0] * 256 + data[1]
    cTemp = -45 + (175 * temp / 65535.0)
    #fTemp = -49 + (315 * temp / 65535.0)
    global te  
    te = round(cTemp)
    humidity = 100 * (data[3] * 256 + data[4]) / 65535.0
    global rh
    rh = round(humidity)
    
while True:                                                                              #the beginning of the main program.
    database = firebase.database()                                             #take an instance from the firebase database which is pointing to the root directory of your database.
    #dbread = database.child("Sensor")                            #get the child "RGBControl" path in your database and store it inside the "RGBControlBucket" variable.
    #arah= dbread.child("Arah").get().val()   
    #database = firebase.database()                                             #take an instance from the firebase database which is pointing to the root directory of your database.
    #dbread = database.child("Console")                      #read the power state value from the tag "powerState" which is a node inside the database.
    #servo= dbread.child("Servo").get().val()  
    bacaSensor()
    #print(temp)
    #print(humidity)

    textKirim = 'A%dB%dC\n' % (te,rh)                      #read the power state value from the tag "powerState" which is a node inside the database.
    #se.write(str.encode(textKirim))
    #angka = random.randint(1,100)
    database.child("Sensor").update({"Suhu": te})
    database.child("Sensor").update({"Rh": rh})
    #print(arah)
    #print(servo)
    print(textKirim)
    #run_event_loop(print_add, print_remove, key_received)
    time.sleep(0.5)

