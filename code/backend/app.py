import os
import time
import cv2

from flask import Flask, jsonify, request
from flask_cors import CORS
from mtcnn.mtcnn import MTCNN

app = Flask(__name__)
UPLOAD_FOLDER = 'upload'
LOG_FOLDER = 'logs'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
CORS(app, supports_credentials=True)


@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route('/api/upload', methods=['POST'], strict_slashes=False)
def api_upload():
    file_dir = os.path.join(app.config['UPLOAD_FOLDER'])
    if not os.path.exists(file_dir):
        os.makedirs(file_dir)

    f = request.files['file']  # 从表单的file字段获取文件，myfile为该表单的name值
    if f is None:

        return jsonify({"code": 1001, "msg": "上传失败"})

    else:
        current_time = int(time.time())
        new_filename = str(current_time) + '.jpg'
        f.save(os.path.join(file_dir, new_filename))

        return jsonify({"code": 200,
                        "message": "上传成功, 已获取生成的服务器地址",
                        "filename": f.filename,
                        "token": "/api/detection/" + new_filename})


@app.route('/api/detection/<filename>', methods=['GET', 'POST'])
def get_img(filename):
    img_file = os.path.join(UPLOAD_FOLDER, filename)
    if os.path.isfile(img_file):
        img = cv2.imread(img_file)
        detector = MTCNN()
        face_data = detector.detect_faces(img)
        count = len(face_data)
        if count > 0:
            return jsonify({"message": "发现人脸,详情请看检测结果",
                            "count": count,
                            "face_data": face_data})
        elif count is 0:
            return jsonify({"code": "200",
                            "message": "未检测出人脸！（若检测有误可以）"})
        else:
            return jsonify({"code": "500",
                            "message": "服务器内部错误"})
    else:
        return jsonify({"code": "404",
                        "message": "图片不存在或参数错误！"})


@app.route('/api-test', methods=['POST', 'GET'])
def api_server_test():
    result = "The backend is connecting!"

    return jsonify({"code": "200",
                    "message": result})


if __name__ == '__main__':
    app.run()
