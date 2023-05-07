# DeepFloyd.py
Small unofficial DeepFloyd API in Python

# Requirements
Python 3.10+(match case support)

# Installation
Fork this repository, install needed libraries with:
```
pip install websockets
```

# Example of use:

Synchronous API:
```py
import requests
from deepfloyd import deepfloydapi


api = deepfloydapi('sst5l') # sst5l - индекс пространства hugging faces
urls = api.generate('apple', 'red color')['img_urls'] # apple - prompt, red color - negative prompt(необязателен)
for i in range(len(urls)):
  resource = requests.get(urls[i]) # получаем байты изображения из итогового url
  with open(f'res{i}.png', 'wb+') as f:
    f.write(resource.content)
with open('upscale_0.png', 'wb+') as f:
  f.write(api.upscale(0)) # 0 - индекс изображения, которое вы хотите увеличить
```

Asynchronous API:
```py
import asyncio
from deepfloydasync import deepfloydapi
import requests


async def main():
  api = deepfloydapi('sst5l') # sst5l - индекс пространства hugging faces
  urls = (await api.generate('apple', 'red color'))['img_urls'] # apple - prompt, red color - negative prompt(он необязателен)
  for i in range(len(urls)):
    resource = requests.get(urls[i]) # получаем байты изображения и итогового url
    with open(f'res{i}.png', 'wb+') as f:
      f.write(resource.content)
  with open('upscale_0.png', 'wb+') as f:
    f.write(await api.upscale(0)) # 0 - индекс изображения, которое вы хотите увеличить


asyncio.run(main())
```

Result(upscaled):

![example.png](https://i.imgur.com/yyV3u9s.png)


Not upscaled:

![example.png](https://i.imgur.com/PLpLdYO.png)


# Original API in JavaScript by Pozaza:
https://github.com/Pozaza/DeepFloyd-Unofficial-API
