import socket as sio
import cv2


# Video Capture Object
vid = cv2.VideoCapture(0)
host = "127.0.0.1"
port = 8585

# socket object
s = sio.socket()

# binding ojbect
s.bind((host, port))
print("Bind To port: ", port)

s.listen(5)

num = 2
while True:
    try:
        c, add = s.accept()
        print("Got Connection from :", add)
        while True:
            # read from camera and save to the File
            flg, img = vid.read()
            cv2.imwrite("photo.png", img)

            # send message
            c.send("{}\n".format("1").encode())
            num = c.recv(1024).decode()
            print("Receive Number: ", num)

            # loop Break Condition
            if "500" in num:
                print("Breaking")
                break
        
        # Comment Below break for infinite time
        break

    except KeyboardInterrupt:
        print("Beaking Connection.")
        break
    
vid.release()
c.close()