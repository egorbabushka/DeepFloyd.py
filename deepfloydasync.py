from websockets.client import connect
import os
import json
import math
import random
import secrets
import base64


class ImagesNotGenerated(Exception):
  def __str__(self):
    return 'Generate image first!'


class deepfloydapi:
  def __init__(self, spaceIndex='sst5l'):
    self.url = f'deepfloyd-if--{spaceIndex}.hf.space'
    self.sessionhash = str(secrets.token_hex(16))
    self.temp = None
    self.prompt = None
    self.negative = None
  async def generate(self, prompt, negative=""):
    self.prompt = prompt
    self.negative = negative
    async with connect(f"wss://{self.url}/queue/join", max_size=2**32) as websocket:
      while True:
        message = await websocket.recv()
        out = json.loads(message)
        # print(f"Received: {out['msg']}")
        match out['msg']:
          case 'send_hash':
            await websocket.send(json.dumps({'fn_index': 20, 'session_hash': self.sessionhash}))
          case 'queue_full':
            return {
              'error': 'Service Unavailable'
            }
          case 'send_data':
            await websocket.send(json.dumps({'fn_index': 20, 'data': [prompt, negative, math.floor(random.random() * 100000000), 4, 7, "smart50", 100], 'session_hash': self.sessionhash}))
          case 'process_completed':
            imgurls = [f'https://{self.url}/file={i["name"]}' for i in out["output"]["data"][0]]
            self.temp = out["output"]["data"][2]
            return {'info': out['output'], 'img_urls': imgurls}
  async def upscale(self, index):
    if not self.temp:
      raise ImagesNotGenerated()
    async with connect(f"wss://{self.url}/queue/join", max_size=2**32) as websocket:
      while True:
        message = await websocket.recv()
        out = json.loads(message)
        # print(f"Received: {out['msg']}")
        match out['msg']:
          case 'send_hash':
            await websocket.send(json.dumps({'fn_index': 34, 'session_hash': self.sessionhash}))
          case 'queue_full':
            return {
              'error': 'Service Unavailable'
            }
          case 'send_data':
            await websocket.send(json.dumps({'fn_index': 34, 'data': [self.temp, index, math.floor(random.random() * 100000000), 4, "smart50", 50, self.prompt, self.negative, math.floor(random.random() * 100000000), 9, 40], 'session_hash': self.sessionhash}))
          case 'process_completed':
            return base64.decodebytes(str.encode(out['output']['data'][0].replace('data:image/png;base64,', '')))
