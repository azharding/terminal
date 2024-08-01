from flask import Flask, render_template, request, jsonify
import subprocess

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/execute', methods=['POST'])
def execute():
    command = request.json.get('command')
    result = subprocess.run(command, shell=True, capture_output=True, text=True)
    return jsonify(output=result.stdout, error=result.stderr)

if __name__ == '__main__':
    app.run(debug=True)
