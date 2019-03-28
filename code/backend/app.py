from flask import Flask, jsonify

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route('/face-detection', methods=['POST'])
def img_detection():
    return


@app.route('/api-test', methods=['POST', 'GET'])
def api_server_test():
    result = "The backend is starting and just enjoying!"

    return jsonify({'result': result})


if __name__ == '__main__':
    app.run()
