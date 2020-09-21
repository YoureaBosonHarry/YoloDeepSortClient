import imagezmq
import picamera
import io
import numpy as np
import socket
import time

sender = imagezmq.ImageSender(connect_to="tcp://192.168.50.117:5555")

with picamera.PiCamera() as camera:
    rpiName = socket.gethostname()
    camera.resolution = (1088, 720)
    while True:
        output = np.empty((720, 1088, 3), dtype=np.uint8)
        camera.capture(output, 'rgb')
        print("Sending...")
        msg = sender.send_image(rpiName, output)
        print(msg)
        time.sleep(0.5)