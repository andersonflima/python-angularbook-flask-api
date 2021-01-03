from flask import Flask
from flask_restful import Api, request
from flask_cors import CORS
from router import Auth, auth_endpoints

app = Flask(__name__)
CORS(app)
api = Api(app)

api.add_resource(Auth, *auth_endpoints)

@app.before_request
def before_request():
    print(request.path)

if __name__ == "__main__":
    app.run(port=3000)