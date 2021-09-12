from flask import Flask, jsonify, request, render_template

from flask_cors import CORS


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

        requestData = request.get_json()
        name = requestData['name']
        
        #jsons a string
        #return jsonify("Lol")
        return name
        

    else:

        return "get"