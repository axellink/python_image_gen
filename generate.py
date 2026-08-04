import math
import random
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

    return (math.floor(red), math.floor(green), math.floor(blue))

def in_image(p):
    x = p[0]
    y = p[1]
    return 0 <= x < RES_X and 0 <= y < RES_Y

def brush(img, position, radius, color):
    x,y = position
    for i in range(x-radius, x+radius+1):
        for j in range(y-radius, y+radius +1):
            if math.sqrt((x-i)**2 + (y-j)**2) <= radius and in_image((i,j)):
                img.putpixel((i,j),color(i,j))
    return img

img = Image.new("RGB",(RES_X,RES_Y))
for x in range(RES_X):
    for y in range(RES_Y):
        if random.random() > 0.9999:
            radius = random.randint(10,50)
            img = brush(img,(x,y),radius, pixel)
img.save("result.png")
