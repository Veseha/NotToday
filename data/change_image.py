import random
from PIL import Image, ImageDraw #Подключим необходимые библиотеки.

mode = 0
for i in range(6):
    ab = 'plank' + str(i + 1)
    image = Image.open(ab + '.png') #Открываем изображение.
    draw = ImageDraw.Draw(image) #Создаем инструмент для рисования.
    width = image.size[0] #Определяем ширину.
    height = image.size[1] #Определяем высоту.
    pix = image.load() #Выгружаем значения пикселей.
    if (mode == 0):
        for i in range(width):
            for j in range(height):
                a = pix[i, j][0] + 30
                b = pix[i, j][1] + 20
                c = pix[i, j][2] + 0
                draw.point((i, j), (a, b, c))
    image.save(ab + "1.png", "PNG")
    del draw