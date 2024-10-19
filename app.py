from flask import Flask, request, jsonify
import subprocess

app = Flask(__name__)

def run_python_script(keyword):
    result = subprocess.run(['python3', 'your_script.py', keyword], capture_output=True, text=True)
    return result.stdout

@app.route('/')
def index():
    return app.send_static_file('index.html')  # Serve the HTML file

@app.route('/search', methods=['POST'])
def search():
    data = request.get_json()
    keyword = data['keyword']
    result = run_python_script(keyword)
    return jsonify({"result": result})

if __name__ == '__main__':
    app.run(debug=True)
