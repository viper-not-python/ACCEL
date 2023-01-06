import serial
import time
import cv2

SerialIn = serial.Serial("COM9",9600)

frame = cv2.imread("white.jpg")
frame_original = frame

width = 600
height = 600

def data():
    data = SerialIn.readline()
    data = data.decode()
    ind_y = data.find("y")
    acc_x = data[0:ind_y]
    acc_y = data[ind_y+1:]  
    acc_y = float(acc_y)
    acc_x = float(acc_x)
    data = acc_x, acc_y
    return data

frame_original = cv2.resize(frame_original, (width, height))
frame_original = cv2.line(frame_original, (0, int(height/2)), (width, int(height/2)), (0, 255, 0), 5)
frame_original = cv2.line(frame_original, (int(width/2), 0), (int(width/2), height), (0, 255, 0), 5)

while True:
    try:
        frame = frame_original
        print(data())
        x, y = data()
        c_w = width / 2 + y * 100
        c_h = height / 2 + x * 100
        frame = cv2.resize(frame, (width, height))
   
        frame = cv2.circle(frame, (int(c_w), int(c_h)), 25, (0, 0, 255), -1)



        cv2.imshow("frame", frame)
        time.sleep(0.001)

    except Exception as e:
        print(e)

    if cv2.waitKey(1) == ord('q'):
        break

cv2.destroyAllWindows()