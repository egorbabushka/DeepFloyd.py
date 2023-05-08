# DeepFloyd.py
Small unofficial DeepFloyd API in Python

# Requirements
Python 3.10+(match case support)

# Installation
Fork this repository, install needed libraries with:
```
pip install websockets
```

# Example of use

Synchronous API(example.py):
```py
from deepfloyd import deepfloydapi

api = deepfloydapi('sst5l') # sst5l - индекс пространства hugging faces
generation = api.generate('green apple covered with honey and sliced', 'red apple, yellow apple, terrible quality, not realistic result') # первый аргумент - prompt, второй - negative prompt(необязателен). возвращает объект типа Generation.
imgbytes = generation.getbytes() # generation.geturls() если нужны ссылки изображений
for i in range(len(imgbytes)):
  with open(f'res{i}.png', 'wb+') as f:
    f.write(imgbytes[i])
with open('upscale_0.png', 'wb+') as f:
  f.write(generation.upscale(0)) # 0 - индекс изображения, которое вы хотите увеличить
```

Asynchronous API(example_async.py):
```py
from deepfloydasync import deepfloydapi
import asyncio

async def main():
  api = deepfloydapi('sst5l') # sst5l - индекс пространства hugging faces
  generation = await api.generate('green apple covered with honey and sliced', 'red apple, yellow apple, terrible quality, not realistic result') # первый аргумент - prompt, второй - negative prompt(необязателен). возвращает объект типа Generation.
  imgbytes = await generation.getbytes() # await generation.geturls() если нужны ссылки изображений или просто лень ждать, когда библиотека закончит фетчить байты из url-ов
  for i in range(len(imgbytes)):
    with open(f'res{i}.png', 'wb+') as f:
      f.write(imgbytes[i])
  with open('upscale_0.png', 'wb+') as f:
    f.write(await generation.upscale(0)) # 1 аргумент - индекс изображения, которое вы хотите увеличить

asyncio.run(main())
```

Results(upscaled):

![example.png](https://i.imgur.com/yyV3u9s.png)


Not upscaled:

![example.png](https://i.imgur.com/PLpLdYO.png)


# Original API in JavaScript by Pozaza:
https://github.com/Pozaza/DeepFloyd-Unofficial-API
