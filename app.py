from flask import Flask, jsonify, request, render_template
from flask_cors import CORS
import tensorflow as tf
from tensorflow import keras
from keras.models import load_model
from keras.preprocessing import image
import numpy as np
import base64

# loads model
model = load_model('./model/mlmodel1.h5')

# gets image and makes it readable by the model
def getPrediction(img):
    # not sure if this part works
    byteImg = base64.b64decode(img) #goes to bytes
    img = image.load_img(byteImg,target_size=(128,128)) #changes to PIL image instance supposedly
    imgData = image.img_to_array(img) #changes img to array
    prediction = model.predition(np.array([imgData])) #predices
    return prediction

app = Flask(__name__)
if __name__ == "__main__":
    app.run(port=5000)

@app.route('/')
def homepage():
    return "<h1>Hello Word!</h1>"

@app.route('/data', methods=["GET","POST"])
def data():

    #incoming data

    if request.method == "POST":

        classifications ["Heart","Oblong","Oval","Round","Square"]
        requestData = request.get_json()
        b64id = requestData['base64ID']
        
        pred = getPrediction(b64id)
        
        maxi = -1
        index = 0
        for i in range(len(pred[0])):

            if pred[0][i] > maxi:
                maxi=pred[0][i]
                index = i
        

        #jsonify importante
        #return jsonify(b64id)
        return jsonify(index)
        

    else:

        return "get"