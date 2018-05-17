from flask import Flask, request, render_template, jsonify
from flask_cors import CORS
from textblob import TextBlob

app = Flask(__name__)
CORS(app)
@app.route('/')
def index():
        return "Yo, it's working!"

@app.route('/submit', methods = ['POST'])
def test():
    data = request.values
    text = data['text']
    blob = TextBlob(text)
    res = "0";
    for sentence in blob.sentences:
        res = sentence.sentiment.polarity
        print(res)
    return jsonify(res)
if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=True)
