# from flask import Flask, request, render_template
from flask import Flask, request

#app declaration
app = Flask(__name__)

with app.test_request_context('/hello', method='GET'):
    assert request.path == '/hello'
    assert request.method == 'GET'



# #login function
# def do_the_login():
#     return render_template('index.html', name="harry")

# #redirect function
# def show_the_login_form():
#     return "This is the login page"

# #routing function
# @app.route('/login', methods=['GET', 'POST'])
# def login():
#     if request.method == 'POST':
#         return do_the_login()
#     else:
#         return show_the_login_form()
    
#redirecting function incase of 404   
@app.errorhandler(404)
def page_not_found(error):
    return render_template('404.html')

if __name__ == "__main__":
    app.run(debug=True)
    
    
