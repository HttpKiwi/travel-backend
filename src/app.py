import time
import spacy
from flask import Flask, request, jsonify
#from train import test
app = Flask(__name__)
users_seen = {}
from entity_manager import extract_entities

@app.route('/')
def hello():
    user_agent = request.headers.get('User-Agent')
    return 'Hello! I see you\'re using %s' % user_agent

@app.route('/test/<query>', methods=['GET'])
def check_in(query):
    res = extract_entities(query)
    return jsonify(res)

@app.route('/last-seen/<user>')
def last_seen(user):
    if user in users_seen:
        return jsonify(user=user, date=users_seen[user])
    else:
        return jsonify(error='Who dis?', user=user), 404

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)