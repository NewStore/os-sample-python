from requests import get
from flask import Flask
application = Flask(__name__)

@application.route("/")
def hello():
    return get('https://www.newstore.com').text

if __name__ == "__main__":
    application.run()
    
