from flask import Flask, request, render_template
# from flask_restful import Api, Resource
import json

#app declaration
app = Flask(__name__)
# api = Api(app)

@app.route('/')
def home():
    return render_template('index.html')

def check(username, password):
    if(username == "solomon", password == "admin"):
        return True
    else:
        return False

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        if check(request.form['username'], request.form['password'] == True):
            response = {"username": f"{request.form['username']}", "password": f"{request.form['password']}"}
            return response
        else:
            return render_template('404.html', message=request.form['username'])
    else:
        return render_template('404.html', message="Wrong method")
    

f = open('json2.json')

JSON_FILE = json.load(f)
 

#redirecting function incase of 404   
@app.errorhandler(404)
def page_not_found(error):
    return render_template('404.html')

if __name__ == "__main__":
    app.run(debug=True)
    
    