from flask import Flask, jsonify, send_from_directory

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello, World! Flask is running on your server!"

@app.route('/api/info')
def api_info():
    return jsonify({
        "service": "flask-demo",
        "status": "running",
        "proxy": "nginx -> flask"
    })

@app.route('/static/<path:filename>')
def static_files(filename):
    return send_from_directory('static', filename)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
