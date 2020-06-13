from flask import Flask, request, render_template, jsonify
from flask_cors import CORS

from util import predict_tag, user_history

app = Flask(__name__)
CORS(app)

user_id =1


@app.route('/', methods=['GET'])
def home():
    return render_template('index.html')


@app.route('/add', methods=['POST'])
def add_bookmark():
    bookmark = request.json
    print(bookmark)
    """
        {
            'name': name,
            'url': url,
            'tags': [tag1, tag2],
            'des': description
        }
    """
    # TODO : add new bookmark
    return jsonify({})


@app.route('/predict/tags', methods=['POST'])
def get_tags():
    tags = request.json
    return jsonify(predict_tag(tags))


@app.route('/history/<int:user_id>', methods=['GET'])
def get_history(user_id):
    return jsonify(user_history(user_id))


