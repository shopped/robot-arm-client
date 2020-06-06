from flask import Flask, request, jsonify
from flask_cors import CORS
app = Flask(__name__)
CORS(app)

from adafruit_servokit import ServoKit
kit = ServoKit(channels=16)

@app.route('/', methods=['GET', 'POST'])
def move():
	content = request.json
	for i in range(0, 6):
		kit.servo[i].angle = int(content[i])
	print(content)
	return "ok"
