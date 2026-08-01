import math
from PIL import Image

RES_X=1024
RES_Y=1024

def pixel(x,y):
    if math.floor(x/256)%2 == 0:
        red = x % 256
    else:
        red = 256 - (x%256)

    if math.floor(y/256)%2 == 0:
        blue = y % 256
    else:
        blue = 256 - (y%256)

    green = 0

    if y-100 < x < y + 100 :
        blue -= 50
        red -= 50

    if y-100 < RES_X-x < y + 100 :
        blue += 50
        red += 50

    rl = y-150
    ll = y+150
    func = ((-64+x/8)**2)
    if not rl < func < ll:
        red = 0
        blue = 0

    return (math.floor(red), math.floor(green), math.floor(blue))

def in_image(p):
    x = p[0]
    y = p[1]
    return 0 <= x < RES_X and 0 <= y < RES_Y

def around(img, x, y):
    positions = [(x+i, y+j) for i in range(-1,2) for j in range(-1,2)]
    pixels = [img.getpixel(p) if in_image(p) else (0,0,0) for p in positions]
    return pixels

def post_treat(img):
    for x in range(RES_X):
        for y in range(RES_Y):
            arounds = around(img, x, y)
            red = math.floor(sum([p[0] for p in arounds])/8)
            green = math.floor(sum([p[1] for p in arounds])/8)
            blue = math.floor(sum([p[2] for p in arounds])/8)
            img.putpixel((x,y),(red,green,blue))
    return img


img = Image.new("RGB",(RES_X,RES_Y))
for x in range(RES_X):
    for y in range(RES_Y):
        img.putpixel((x,y),pixel(x,y))
img = post_treat(img)

img.save("result.png")
