from flask import Flask, request, render_template
from flask_restful import Api, Resource
import json

#app declaration
app = Flask(__name__)
api = Api(app)

# @app.route('/')
# def home():
    # return render_template('index.html')
    
    
def valid_login(username, password):
    if username == 'solomon' and password == 'admin':
        return True
    else:
        return False

class Doctor(Resource):
    def get(self):
        return render_template('index.html')
    
    def post(self):
        if request.method == 'POST':
            name = request.form['username']
            if valid_login(request.form['username'], request.form['password']):
                print("welcome")
                print(request.form['username'])
                print(request.form['password'])
                # return render_template('index.html', name=name)
            else:
                print("not welcome")
                print(request.form['username'])
                print(request.form['password'])
                # return render_template('navbar.html')
        return render_template('index.html', name=name)
        

api.add_resource(Doctor, "/login")
# api.add_resource(Doctor, "/doctor")

f = open('json2.json')

JSON_FILE = json.load(f)
 

#redirecting function incase of 404   
@app.errorhandler(404)
def page_not_found(error):
    return render_template('404.html')

if __name__ == "__main__":
    app.run(debug=True)
    
    
