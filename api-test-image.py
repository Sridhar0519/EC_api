import json, requests

url = 'https://predict-titanic-api.herokuapp.com/im_size' # change to your url

# url = 'http://127.0.0.1:5000/im_size'
my_img = {'image': open('./18BMC040_0010.jpg', 'rb')}
r = requests.post(url, files=my_img)

print(r.json())