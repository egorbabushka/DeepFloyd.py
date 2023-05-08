from websockets.sync.client import connect
import json
import math
import random
import secrets
import base64
import requests


class Generation:
  def __init__(self, url, sessionhash, temp, prompt, negative, imgurls):
    self.url = url
    self.sessionhash = sessionhash
    self.temp = temp
    self.prompt = prompt
    self.negative = negative
    self.imgurls = imgurls
  
  def geturls(self):
    return self.imgurls
  
  def getbytes(self):
    return [requests.get(i).content for i in self.imgurls]

  def upscale(self, index):
    with connect(f"wss://{self.url}/queue/join", max_size=2**32) as websocket:
      while True:
        message = websocket.recv()
        out = json.loads(message)
        match out['msg']:
          case 'send_hash':
            websocket.send(json.dumps({'fn_index': 34, 'session_hash': self.sessionhash}))
          case 'queue_full':
            return 'Service Unavailable'
          case 'send_data':
            websocket.send(json.dumps({'fn_index': 34, 'data': [self.temp, index, math.floor(random.random() * 100000000), 4, "smart50", 50, self.prompt, self.negative, math.floor(random.random() * 100000000), 9, 40], 'session_hash': self.sessionhash}))
          case 'process_completed':
            return base64.decodebytes(str.encode(out['output']['data'][0].replace('data:image/png;base64,', '')))

class deepfloydapi:
  def __init__(self, spaceIndex='sst5l'):
    self.url = f'deepfloyd-if--{spaceIndex}.hf.space'
    self.sessionhash = str(secrets.token_hex(16))

  def generate(self, prompt, negative=""):
    with connect(f"wss://{self.url}/queue/join", max_size=2**32) as websocket:
      while True:
        message = websocket.recv()
        out = json.loads(message)
        match out['msg']:
          case 'send_hash':
            websocket.send(json.dumps({'fn_index': 20, 'session_hash': self.sessionhash}))
          case 'queue_full':
            return 'Service Unavailable'
          case 'send_data':
            websocket.send(json.dumps({'fn_index': 20, 'data': [prompt, negative, math.floor(random.random() * 100000000), 4, 7, "smart50", 100], 'session_hash': self.sessionhash}))
          case 'process_completed':
            imgurls = [f'https://{self.url}/file={i["name"]}' for i in out["output"]["data"][0]]
            #self.temp = out["output"]["data"][2]
            gen = Generation(self.url, self.sessionhash, out["output"]["data"][2], prompt, negative, imgurls)
            self.sessionhash = str(secrets.token_hex(16))
            return gen
