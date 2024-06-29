from flask import Flask, jsonify, request, json
from managers import UserInfo

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World'

@app.route('/api/create_user', methods=['POST'])
def create_resource():
    data = request.json
    validity = UserInfo.create_user(data)
    return jsonify(validity)


if __name__ == '__main__':
    app.run(debug=True)
