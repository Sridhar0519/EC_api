import cv2
import os,sys
import numpy as np
import os


VIDEO_STREAM = "../videos/18BMC040.mp4"

root_dir = "../"
project_folder = "images"

if os.path.isdir(root_dir + project_folder) == False:
    root_dir = "./"
    os.mkdir(root_dir + project_folder)

os.chdir(root_dir + project_folder)
# print(os.path.isdir(root_dir + project_folder)) # True for images folder



# print(VIDEO_STREAM[-12:-4])
roll_no = VIDEO_STREAM[-12:-4]
cap = cv2.VideoCapture(VIDEO_STREAM)
count = 0

while 1:
    count = count + 1

    ret, frame = cap.read()
    print(count)
    print(frame)
    if (frame is None) == False:
        (h,w)=frame.shape[:2]
        width=500
        ratio=width/float(w)
        height=int(h*ratio)
        frame=cv2.resize(frame,(width,height))
        if count < 10:
            cv2.imwrite(roll_no + '_000' + str(count) + '.jpg', frame)
        elif count < 100:
            cv2.imwrite(roll_no + '_00' + str(count) + '.jpg', frame)
        elif count < 1000:
            cv2.imwrite(roll_no + '_0' + str(count) + '.jpg', frame)
        elif count < 10000:
            cv2.imwrite(roll_no + '_' + str(count) + '.jpg', frame)
    else:
        break
    k = cv2.waitKey(30) & 0xff
    if k == 27:
        break

cap.release()