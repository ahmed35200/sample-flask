from flask import Flask,request
from flask import render_template

import urllib.request
import ssl
import urllib.request as rq
from cv2 import *
import urllib.request
import requests


def dhash(image, hashSize=8):
	# resize the input image, adding a single column (width) so we
	# can compute the horizontal gradient
	resized = cv2.resize(image, (hashSize + 1, hashSize))

	# compute the (relative) horizontal gradient between adjacent
	# column pixels
	diff = resized[:, 1:] > resized[:, :-1]

	# convert the difference image to a hash
	return sum([2 ** i for (i, v) in enumerate(diff.flatten()) if v])

app = Flask(__name__)


@app.route("/")
def hello_world():
    return "lmao"
@app.route('/hashi', methods=['GET', 'POST'])
def hashing():
    return "lmao"
