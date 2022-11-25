from flask import Flask, jsonify, request
from markupsafe import escape


app = Flask(__name__)


@app.route("/")
def hello_world():
    name = request.args.get("name", "World")
    return f"Hello, {escape(name)}!", 200, {"Content-Type": "text/plain"}


@app.route("/plain-json")
def plain_json():
    return jsonify({"message": "Hello, World!"})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=44778, debug=False)
