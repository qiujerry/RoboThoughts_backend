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
            arr = []
            arr.append({'reference' : 50})
            arr.append({'current' : 50})
            arr.append({'error' : 1})
            output.append({'Controls_Depth' : arr})

        if json_input['data'] == 'State_Depth':
            arr = []
            arr.append({'enabled' : 50})
            arr.append({'pingFrequency' : 50})
            arr.append({'filename' : 'String'})
            output.append({'State_Depth' : arr})

        if json_input['data'] == 'Bboxes':
            arr = []
            arr.append({'enabled' : 50})
            arr.append({'pingFrequency' : 50})
            arr.append({'filename' : 'String'})
            output.append({'Bboxes' : arr})
            
        if json_input['data'] == 'Dvl':
            arr = []
            arr.append({'enabled' : 50})
            arr.append({'pingFrequency' : 50})
            arr.append({'filename' : 'String'})
            output.append({'Dvl' : arr})

        if json_input['data'] == 'Imu':
            arr = []
            arr.append({'enabled' : 50})
            arr.append({'pingFrequency' : 50})
            arr.append({'filename' : 'String'})
            output.append({'Imu' : arr})

        if json_input['data'] == 'Object':
            arr = []
            arr.append({'enabled' : 50})
            arr.append({'pingFrequency' : 50})
            arr.append({'filename' : 'String'})
            output.append({'Object' : arr})

        if json_input['data'] == 'Switches':
            arr = []
            arr.append({'enabled' : 50})
            arr.append({'pingFrequency' : 50})
            arr.append({'filename' : 'String'})
            output.append({'Switches' : arr})

    return jsonify({'data' : arr}), 201

@app.errorhandler(400)
def invalid(error):
    return make_response(jsonify({'error':'Invalid JSON Request'}), 400)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
