from flask import Flask, request
from dotenv import load_dotenv
import requests, os

app = Flask(__name__)
load_dotenv()

@app.route("/",methods=['POST',"GET"])
def gogo():
    r = requests.post(os.getenv("WEBHOOK"),json=request.json)
    return r.text, r.status_code
    
app.run(debug=True)