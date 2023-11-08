from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/api/resource', methods=['GET'])
def get_resource():
    data = {
        'message': 'Hello, this is a JSON response!',
        'status': 'success',
    }
    return jsonify(data)

@app.route('/api/resource', methods=['POST'])
def create_resource():
    return 'This is a POST request for /api/resource'

if __name__ == '__main__':
    app.run(debug=True)
