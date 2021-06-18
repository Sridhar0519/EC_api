# import face_recognition
import cv2
import os.path
from os import path


def read_img(path):
  img=cv2.imread(path)
  (h,w)=img.shape[:2]
  width=500
  ratio=width/float(w)
  height=int(h*ratio)
  return cv2.resize(img,(width,height))

# os.chdir('../images')
known_encodings = []
known_names = []
known_dir = './images'
# print(os.listdir(known_dir))

for file in os.listdir(known_dir):
    img=read_img(known_dir +'/'+ file)
    img_enc=face_recognition.face_encodings(img)
    known_encodings.appsend(img_enc)
    known_names.append(file.split('.')[0])


# Checking whether Image is loaded or not
# while 1:
#     img=cv2.imread(known_dir +'/'+ known_names[0] + '.jpg')
#     cv2.imshow('image', img)
#     k = cv2.waitKey(30) & 0xff
#     if k == 27:
#         break
  


# unknown_dir='unknown'
# for file in os.listdir(unknown_dir):
def similarity(file):
    print("Processing",file)
    # img = read_img(unknown_dir + '/' + file)
    
    img_enc=face_recognition.face_encodings(img)[0]
    results=face_recognition.compare_faces(known_encodings,img_enc)
    print(min(face_recognition.face_distance(known_encodings,img_enc)))

    return results

