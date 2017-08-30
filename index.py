import os
from flask import Flask, request, render_template
import traceback
import requests
import json

token = os.environ.get('FB_ACCESS_TOKEN')
app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def webhook():
    if request.method == 'POST':
        try:
            data = json.loads(request.data.decode())
            text = data['entry'][0]['messaging'][0]['message']['text']
            sender = data['entry'][0]['messaging'][0]['sender']['id']
            payload = {'recipient': {'id': sender}, 'message': {'text': "olá, tudo bem?"}}
            r = requests.post('https://graph.facebook.com/v2.6/me/messages/?access_token=' + token, json=payload)
        except Exception as e:
            print(traceback.format_exc())
    elif request.method == 'GET': # Para a verificação inicial
        if request.args.get('hub.verify_token') == os.environ.get('FB_VERIFY_TOKEN'):
            return request.args.get('hub.challenge')
        return "Hi, i am a robot!"
    return "Nothing"


@app.route('/privacy')
def privacy():
    return render_template('privacy.html')

if __name__ == '__main__':
    app.run(debug=True)
