#!api/bin/python
from flask import Flask, jsonify, request, abort, make_response

app = Flask(__name__)

@app.route('/', methods=['POST'])
def respond():
    if not request.json or not 'request' in request.json:
        abort(400)
    output = []
    for json_input in request.json['request']:
        if json_input['data'] == 'AcousticsCommand':
            output.append({'enabled' : 50})
            output.append({'pingFrequency' : 50})
            out.put.append({'filename' : 'String'})
        if json_input['data'] == 'AcousticsStatus':
            output.append({'PFPADiff' : 100})
            output.append({'PFSFDiff' : 100})
            output.append({'Angle' : 100})
        if json_input['data'] == 'AlignmentCommand':
            output.append({'object' : 'String'})
            output.append({'width_ratio' : 100})
        if json_input['data'] == 'AttitudeCommand':
            output.append({'value' : 100})
            output.append({'node' : 100})
        if json_input['data'] == 'CalibrateAlignment':
            output.append({'surge_active' : true})
            output.append({'PFSFDiff' : 100})
            output.append({'Angle' : 100})
    return jsonify({'data' : output}), 201

@app.errorhandler(400)
def invalid(error):
    return make_response(jsonify({'error':'Invalid JSON Request'}), 400)

if __name__ == '__main__':
    app.run(debug = True)
