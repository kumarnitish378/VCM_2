import socket as sio
from random import randint
import numpy as np
import cv2
import matplotlib.pyplot as plt

ser = sio.socket()
port = 8585

def convert_to_img(lst):
    dt = lst.replace("[", "").replace("]", "")
    print(dt)
    img_lst = np.array([int(i) for i in dt.split(", ")])
    img = np.reshape(img_lst, (150, 150, 3))
    print(img)
    plt.imshow(img)
    plt.show()

ser.connect(("127.0.0.1", port))
c = 0
while True:
    try:
        data = ser.recv(3561756).decode()
        print(data)

        # check message and display img from file. and
        # send ack for next frame
        if "1" in data:
            img = cv2.imread(f"photo.png")
            try:
                cv2.imshow('frame', img)
                if cv2.waitKey(1) & 0xFF == ord('q'):
                    cv2.destroyAllWindows()
                    break
            except Exception as e:
                print(e)
                pass
        
        # break Condition 100 number of frame, can be extended
        if c >= 100:
            cv2.destroyAllWindows()
            ser.send("{}".format(500).encode())
            break
        else:
            print(n:= randint(1, 100))
            ser.send("{}".format(n).encode())
        c += 1
        # break
    except KeyboardInterrupt:
        print("Key Borewoṭṅ oglk;fhp ")
        break
cv2.destroyAllWindows()
ser.close()
