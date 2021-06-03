from flask import Flask
from flask import *
import pickle
import base64

class Student:
    def __init__(self,username):
        self.name = username
        self.ROLE = "USESR"
    def status(self):
        return(f"Hello {self.name} . You are having {self.ROLE} privilages.")
app = Flask(__name__)

@app.route("/")
def homepage():
    response = make_response( render_template("registrationPage.html") )
    return response

@app.route('/register', methods=['GET'])
def registerUser():
    username = request.args.get('username')
    serializedString = pickle.dumps(Student(username) ) # serializing 
    
    serializedString = base64.b64encode(serializedString)
        
    response = make_response( render_template("login.html") )
    response.set_cookie( "serialized", serializedString )
    return response

@app.route("/login")
def login():
    serializedString = request.cookies.get('serialized')
    serializedString = base64.b64decode(serializedString)
    print("Deserializing : ",serializedString)
    studentObject = pickle.loads(serializedString) # deserializing
    return studentObject.status()

if __name__ == "__main__":
    app.run()
    
