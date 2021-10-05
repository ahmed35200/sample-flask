from flask import Flask,request
from flask import render_template

import urllib.request
import ssl
import urllib.request as rq
import cv2
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
    return render_template("index.html")
@app.route('/hashi', methods=['GET', 'POST'])
def hashing():
    ssl._create_default_https_context = ssl._create_unverified_context
    urllib.request.urlretrieve(
        'https://dwjz5q0kg4677.cloudfront.net/C3653D2D-B1DD-4311-993F-E4736934AC8D.jpeg',
        "gfg")
    image = cv2.imread("gfg")
    image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    cv2.waitKey(0)

    imageHash = dhash(image)
    return "lol"