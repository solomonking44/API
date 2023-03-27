from flask import Flask, request, render_template
from flask_restful import Api, Resource
import json

#app declaration
app = Flask(__name__)
api = Api(app)

class Doctor(Resource):
    def get(self):
        return JSON_FILE
    
    def post(self, category):
        

api.add_resource(Doctor, "/doctor")
api.add_resource(Doctor, "/specialty")

f = open('json2.json')

JSON_FILE = json.load(f)
 

#redirecting function incase of 404   
@app.errorhandler(404)
def page_not_found(error):
    return render_template('404.html')

if __name__ == "__main__":
    app.run(debug=True)
    
    
