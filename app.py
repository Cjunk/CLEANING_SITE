from flask import Flask, render_template,session,request,redirect
from dotenv import load_dotenv,dotenv_values
import os
app = Flask(__name__)
load_dotenv() 
app.secret_key = os.getenv("SECRET_KEY")
SECRET_KEY = os.getenv("SECRET_KEY")
print(SECRET_KEY)

@app.route('/')
def index():
    template = render_template('home.html')
    return template

if __name__ == '__main__':
    app.run(debug=True)