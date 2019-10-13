from flask import Flask, jsonify, request
from flask_cors import CORS
from flask_restful import Api, Resource, reqparse

# configuration
DEBUG = True

# instantiate the app
app = Flask(__name__)
app.config.from_object(__name__)
api = Api(app)

images = {
        "character": "",
        "imageData": "kot2"
    }


# enable CORS
CORS(app, resources={r'/*': {'origins': '*'}})

@app.route('/asl', methods=['GET','PUT'])
def get_image():
    res = {'status':'success'}
    if request.method=='GET':
        res['images'] = images
    if request.method=='PUT':
        data = request.get_data()
        res['images'] = data
    return jsonify(res)

if __name__ == '__main__':
    app.run()