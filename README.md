# DeepFloyd.py
Small unofficial DeepFloyd API on Python

# Requirements
Python 3.10+(match case support)

# Installation
fork this repository, install needed libraries with:
```
pip install websockets
```

# Example of use:
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
Result:
![example.png](https://i.imgur.com/yyV3u9s.png)

# Original API in JavaScript by Pozaza:
https://github.com/Pozaza/DeepFloyd-Unofficial-API
