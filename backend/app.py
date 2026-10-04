from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return jsonify({"message": "MAD2 Project is working fine"})

if __name__ == '__main__':
    app.run(debug=True)