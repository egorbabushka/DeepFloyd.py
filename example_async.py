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