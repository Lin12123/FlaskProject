from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # 允许跨域请求

# 模拟的词语数据
words = [
    {"chinese": "苹果", "english": "apple", "audioUrl": "https://example.com/audio/apple.mp3"},
    {"chinese": "香蕉", "english": "banana", "audioUrl": "https://example.com/audio/banana.mp3"},
    {"chinese": "橙子", "english": "orange", "audioUrl": "https://example.com/audio/orange.mp3"}
]


# 导入词语接口
@app.route('/api/words/import', methods=['POST'])
def import_words():
    data = request.json
    user_words = data.get('words', [])

    # 过滤出在模拟数据中存在的词语
    result = [word for word in words if word['english'] in user_words]

    return jsonify({
        "code": 200,
        "data": result
    })


# 启动应用
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)