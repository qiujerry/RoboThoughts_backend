#!api/bin/python
from flask import Flask, jsonify, request, abort, make_response

app = Flask(__name__)

@app.route('/', methods=['POST'])
def respond():
    if not request.json or not 'request' in request.json:
        abort(400)
    output = []
    for json_input in request.json['request']:
        if json_input['data'] == 'Controls_Depth':
            output.append({'reference' : 50})
            output.append({'current' : 50})
            output.append({'error' : 1})
        if json_input['data'] == 'State_Depth':
            output.append({'enabled' : 50})
            output.append({'pingFrequency' : 50})
            output.append({'filename' : 'String'})
        if json_input['data'] == 'Bboxes':
            output.append({'enabled' : 50})
            output.append({'pingFrequency' : 50})
            output.append({'filename' : 'String'})
        if json_input['data'] == 'Dvl':
            output.append({'enabled' : 50})
            output.append({'pingFrequency' : 50})
            output.append({'filename' : 'String'})
        if json_input['data'] == 'Imu':
            output.append({'enabled' : 50})
            output.append({'pingFrequency' : 50})
            output.append({'filename' : 'String'})
        if json_input['data'] == 'Object':
            output.append({'enabled' : 50})
            output.append({'pingFrequency' : 50})
            output.append({'filename' : 'String'})
        if json_input['data'] == 'Switches':
            output.append({'enabled' : 50})
            output.append({'pingFrequency' : 50})
            output.append({'filename' : 'String'})
    return jsonify({'data' : output}), 201

@app.errorhandler(400)
def invalid(error):
    return make_response(jsonify({'error':'Invalid JSON Request'}), 400)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
