# readability_server.py
from flask import Flask, request, jsonify
from readability import Document
import requests

app = Flask(__name__)


# @app.route('/readability', methods=['GET'])
# def readability():
#     url = request.args.get('url')
#     if not url:
#         return jsonify({'error': 'No URL provided'}), 400

#     res = requests.get(url)
#     res.encoding = 'utf-8'
#     doc = Document(res.text)
#     content = doc.summary()
#     title = doc.title()

#     return f"<html><head><meta charset='utf-8'><title>{title}</title></head><body>{content}</body></html>", 200, {'Content-Type': 'text/html; charset=utf-8'}


@app.route('/readability', methods=['GET', 'POST'])
def readability():
    data = request.json
    url = data.get('url')
    if not url:
        return jsonify({'error': 'No URL provided'}), 400

    res = requests.get(url)
    doc = Document(res.text)
    content = doc.summary()
    title = doc.title()

    return jsonify({
        'title': title,
        'content': content
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
