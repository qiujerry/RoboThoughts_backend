#!api/bin/python
from flask import Flask, jsonify, request, abort, make_response

app = Flask(__name__)

@app.route('/', methods=['POST'])
def respond():
    if not request.json or not 'request' in request.json:
        abort(400)
    output = []
    for json_input in request.json['request']:
        if json_input['data'] == 'depth':
            output.append({'depth_value' : 50})
        if json_input['data'] == 'velocity':
            output.append({'velocity_value' : 100})
    return jsonify({'data' : output}), 201

@app.errorhandler(400)
def invalid(error):
    return make_response(jsonify({'error':'Invalid JSON Request'}), 400)

if __name__ == '__main__':
    app.run(debug = True)
