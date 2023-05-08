from deepfloyd import deepfloydapi

api = deepfloydapi('sst5l') # sst5l - индекс пространства hugging faces
generation = api.generate('green apple covered with honey and sliced', 'red apple, yellow apple, terrible quality, not realistic result') # первый аргумент - prompt, второй - negative prompt(необязателен). возвращает объект типа Generation.
imgbytes = generation.getbytes() # generation.geturls() если нужны ссылки изображений
for i in range(len(imgbytes)):
  with open(f'res{i}.png', 'wb+') as f:
    f.write(imgbytes[i])
with open('upscale_0.png', 'wb+') as f:
  f.write(generation.upscale(0)) # 0 - индекс изображения, которое вы хотите увеличить
