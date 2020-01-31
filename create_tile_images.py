a = {}

for i in range(20):
    b = input()
    a['wall' + b] = "load_image(wall{}.png)".format(b)
print(a)