import os
from config import CONFIG
from flask import Flask
from flask_smorest import Api, Blueprint

app = Flask(__name__)
app.config.update(CONFIG)
api = Api(app)

blp = Blueprint("test", "items", description="Operations on ML model endpoint")


@blp.route("/")
def index():
    return {
        "status_code": 200,
        "message": "Success!"
    }


@blp.route("/hello/<string:name>")
def hello_name(name):
    return "Hello! {}".format(name)


@blp.errorhandler(400)
def bad_request(error):
    return {
        "status_code": 400,
        "message": "Client side error!"
    }, 400


@blp.errorhandler(404)
def not_found(error):
    return {
        "status_code": 404,
        "message": "URL not found"
    }, 404


@blp.errorhandler(405)
def method_not_allowed(error):
    return {
        "status_code": 405,
        "message": "Request method not allowed!"
    }, 405


@blp.errorhandler(500)
def internal_server_error(error):
    return {
        "status_code": 500,
        "message": "Server error"
    }, 500


api.register_blueprint(blp)

if __name__ == "__main__":
    app.run(debug=True,
            host="0.0.0.0",
            port=int(os.environ.get("PORT", 8080)))
