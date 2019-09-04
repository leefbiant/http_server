#!/bin/python3

# coding: utf8

from flask import Flask
from flask import request  
from flask import make_response,Response  
import json



app = Flask(__name__)

def Response_headers(content):  
    resp = Response(content)  
    resp.headers['Access-Control-Allow-Origin'] = '*'  
    return resp  

def handle(inputpath, outpath):
	dress = cv2.imread(inputpath)
	h = dress.shape[0]
	w = dress.shape[1]
	dress = cv2.resize(dress, (512,512), interpolation=cv2.INTER_CUBIC)
	watermark = process(dress)
	watermark = cv2.resize(watermark, (w,h), interpolation=cv2.INTER_CUBIC)
	cv2.imwrite(outpath, watermark)


@app.route('/')
def hello():
    return 'hello docker&flask'

@app.route('/youme_audio_green', methods=['POST'])
def api():
  if request.method != 'POST' or not request.json:
    content = json.dumps({"error_code":"1001"})  
    resp = Response_headers(content)  
  else:  
    data = request.data
    print("data:", data);
    resp = Response_headers(content)  
  return resp


def main():
    app.run(host='0.0.0.0', debug=True, port=80)

if __name__ == '__main__':
  main()
