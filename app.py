# webhook.py
from flask import Flask, request
import subprocess

app = Flask(__name__)

@app.route('/webhook', methods=['POST'])
def webhook():
    subprocess.run(['git', '-C', '/home/ramoj745/test_repo', 'pull'])
    subprocess.run(['sudo', 'systemctl', 'restart', 'your-flask-app'])
    return 'Webhook received!', 200

if __name__ == '__main__':
    app.run(port=5001)  # or any unused port