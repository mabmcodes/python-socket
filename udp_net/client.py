import cv2, imutils, socket
import numpy as np
import time
import base64

BuFF_SIZE = 65535
client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
client.setsockopt(socket.SOL_SOCKET, socket.SO_RCVBUF, BuFF_SIZE)
HOST = socket.gethostname()
HOST_IP = "127.0.0.1"
PORT = 9999
socketAddress = (HOST_IP, PORT)
print(HOST_IP)
port = 9999

client.sendto("hello server".encode("utf-8"), socketAddress)
fps, st, frames_to_count, cnt = (0, 0, 20, 0)
while True:
    packet, _ = client.recvfrom(BuFF_SIZE)
    data = base64.b64decode(packet, " /")
    npdata = np.fromstring(data, dtype=np.uint8)
    frame = cv2.imdecode(npdata, 1)
    frame = cv2.putText(
        frame,
        "FPS: " + str(fps),
        (10, 40),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.7,
        (0, 0, 255),
        2,
    )
    cv2.imshow("RECEIVING VIDEO", frame)
    key = cv2.waitKey(1) & 0xFF
    if key == ord("q"):
        client.close()
        break
    if cnt == frames_to_count:
        try:
            fps = round(frames_to_count / (time.time() - st))
            st = time.time()
            cnt = 0
        except:
            pass
    cnt += 1
