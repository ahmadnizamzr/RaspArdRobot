import io
import socket
import struct
import time
import picamera
import sys
import cv2

kamera = cv2.VideoCapture('/dev/video0')

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((sys.argv[1], int(sys.argv[2])))

connection = client_socket.makefile('wb')
try:
    #with picamera.PiCamera() as camera:
    with kamera as camera:
    
        camera.resolution = (240, 180)
	    #print("starting Camera...........")
        time.sleep(2)
        stream = io.BytesIO()        
        for foo in camera.capture_continuous(stream, 'jpeg'):
            connection.write(struct.pack('<L', stream.tell()))
            connection.flush()
            stream.seek(0)
            connection.write(stream.read())
            stream.seek(0)
            stream.truncate()
finally:
    connection.close()
    client_socket.close()

