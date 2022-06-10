import cv2, imutils, socket
import numpy as np
import time
import base64
import cv2

BuFF_SIZE = 65535
server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server.setsockopt(socket.SOL_SOCKET, socket.SO_RCVBUF, BuFF_SIZE)
HOST = socket.gethostname()
HOST_IP = "127.0.0.1"
PORT = 9999
socketAddress = (HOST_IP, PORT)
server.bind(socketAddress)
print(f"listening at : {socketAddress}")

video = cv2.VideoCapture("video.mp4")  #  replace 'rocket.mp4' with 0 for webcam
fps, st, frames_to_count, cnt = (0, 0, 20, 0)

while True:
    data, clientAddress = server.recvfrom(BuFF_SIZE)
    print(f"got connection from: {clientAddress}")
    WIDTH = 400
    while video.isOpened():
        _, frame = video.read()
        frame = imutils.resize(frame, width=WIDTH)
        encoded, buffer = cv2.imencode(".jpg", frame, [cv2.IMWRITE_JPEG_QUALITY, 80])
        message = base64.b64encode(buffer)
        server.sendto(message, clientAddress)
        frame = cv2.putText(
            frame,
            "FPS: " + str(fps),
            (10, 40),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.7,
            (0, 0, 255),
            2,
        )
        cv2.imshow("TRANSMITTING VIDEO", frame)
        key = cv2.waitKey(1) & 0xFF
        if key == ord("q"):
            server.close()
            break
        if cnt == frames_to_count:
            try:
                fps = round(frames_to_count / (time.time() - st))
                st = time.time()
                cnt = 0
            except:
                pass
        cnt += 1
