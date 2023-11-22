from flask import Flask, request, Response
import json

app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False

messages = []

@app.route('/', methods=['POST'])
def index():
    data = request.json
    user_message = data['all_messages']
    messages.append(user_message)
    for i in messages:
        print(i)
    return Response(status=200)


@app.route('/json', methods=['GET'])
def index1():
    return messages

if __name__ == '__main__':
    app.run(debug=True, port=5555)