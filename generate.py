import math
import random
from PIL import Image, ImageDraw

RES_X=1024
RES_Y=1024

INNER_RADIUS = 50
OUTER_RADIUS = 512

def point_circle(rad, angle):
    _angle = math.radians(angle)
    x = math.floor(RES_X/2) + math.floor(rad * math.sin(_angle))
    y = math.floor(RES_Y/2) + math.floor(rad * math.cos(_angle))
    return (x,y)

def next_color(color, step = 1):
    array = list(color)
    first255 = array.index(255)
    before = (first255 - 1) % 3
    after = (first255 + 1) % 3
    if array[after] == 255:
        array[first255] -= step
    elif array[before] > 0 :
        array[before] -= step
        if array[before] < 0 :
            array[after] = -1 * array[before]
            array[before] = 0
    else:
        array[after] += step
        if array[after] > 255:
            array[first255] -= array[after] % 255
            array[after] = 255
    return (array[0], array[1], array[2])
    

img = Image.new("RGB",(RES_X,RES_Y))
draw = ImageDraw.Draw(img)
color = (255,0,0)
for i in range(0, 360):
    p1 = point_circle(OUTER_RADIUS-(random.random()*OUTER_RADIUS-INNER_RADIUS), i)
    p2 = point_circle(INNER_RADIUS, i)
    color = next_color(color, 4)
    draw.line([p1,p2], color, width = 3)
img.save("result.png")
