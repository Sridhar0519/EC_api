from flask import Flask, request, jsonify
from flask_cors import CORS, cross_origin
from PIL import Image

# Embedding All Image Files 
import face_recognition
import cv2
import os.path
from os import path


# os.chdir('../images')
known_encodings = []
known_names = []
known_dir = './images'
# print(os.listdir(known_dir))

def create_embedding():
    def read_img(path):
        img=cv2.imread(path)
        (h,w)=img.shape[:2]
        width=500
        ratio=width/float(w)
        height=int(h*ratio)
        return cv2.resize(img,(width,height))



    for file in os.listdir(known_dir):
        img=read_img(known_dir +'/'+ file)
        img_enc=face_recognition.face_encodings(img)
        known_encodings.appsend(img_enc)
        known_names.append(file.split('.')[0])




# Initializing flask application
app = Flask(__name__)
cors = CORS(app)

# Calling the embedding function before the request itself
create_embedding()

@app.route("/im_size", methods=["POST"])
def process_image():
    file = request.files['image']
    # Read the image via file.stream
    img = Image.open(file.stream)

    img_enc = face_recognition.face_encodings(img)[0]
    results = face_recognition.compare_faces(known_encodings,img_enc)
    
    nameStr = "nil"
    for i in range(len(results)):
        if (results[i]):
            nameStr = known_names[i]

    return jsonify({'msg': nameStr, 'size': [img.width, img.height]})


if __name__ == "__main__":
    app.run(debug=False)