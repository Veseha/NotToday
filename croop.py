from PIL import Image
import math
import sys

way = input()
print(sys.argv[1])
way = sys.argv[1]
image = Image.open(way)
width = image.size[0]
height = image.size[1]

alpha = image.getpixel((2, 2))

left = width
right = 0
top = height
bottom = 0
print(str(alpha))
for x in range(width):
    for y in range(height):
        rng = math.sqrt(
            math.pow(image.getpixel((x, y))[0] - alpha[0], 2) + math.pow(image.getpixel((x, y))[1] - alpha[1],
                                                                         2) + math.pow(
                image.getpixel((x, y))[2] - alpha[2], 2))
        # print str(rng)
        if rng > 89:

            if x < left:
                left = x
            if x > right:
                right = x
            if y < top:
                top = y
            if y > bottom:
                bottom = y
print(str(left) + ',' + str(top) + '   ' + str(right) + ',' + str(bottom))


width = right - left
height = bottom - top
img = Image.new("RGBA", (width, height), (0, 0, 0, 0))
for x in range(width):
    for y in range(height):
        img.putpixel((x, y), image.getpixel((x + left, y + top)))

img.save("test1.png", "PNG")

print
"Done!"