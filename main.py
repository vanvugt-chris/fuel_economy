from flask import Flask, request

app = Flask(__name__)

@app.route('/sms', methods=['POST'])
def sms():
    number = request.form['From']
    message_body = request.form['Body']
    with open('text.txt', 'w') as f:
        f.write(f'From: {number} \n{message_body}')
    
if __name__ == '__main__':
    app.run()