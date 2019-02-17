from flask import Flask, jsonify, request, abort, make_response
from recognizer import Recognizer

app = Flask(__name__)


###############
# HTTP Errors #
###############

@app.errorhandler(400)
def bad_request(error):
    ''' Return HTTP status code 400 '''
    return make_response(jsonify({'error': 'Bad request'}), 400)


@app.errorhandler(404)
def not_found(error):
    ''' Return HTTP status code 404 '''
    return make_response(jsonify({'error': 'Not found'}), 404)


###############
# API methods #
###############

@app.route('/ner/api/v0.1/', methods=['GET'])
def get_tasks():
    ''' Return information about API service '''
    return jsonify({'name': 'Named-entity recognition', 'version': '0.1'})


@app.route('/ner/api/v0.1/', methods=['POST'])
def create_task():
    ''' Send russian text and return recognized entities '''

    if not request.json or not 'text' in request.json:
        abort(400)

    text = request.json['text']

    if not 'param' in request.json:
        param = tuple()
    else:
        param = tuple(request.json['param'])

    recognizer = Recognizer(text)
    entities = recognizer.get_entities(param)

    return jsonify({'entities': entities, 'text': text})


if __name__ == '__main__':
    app.run(debug=True)
