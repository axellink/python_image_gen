import math
import random
from PIL import Image, ImageDraw

RES_X=1024
RES_Y=1024

INNER_RADIUS = 128
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
    x1, y1 = point_circle(OUTER_RADIUS, i)
    x2, y2 = point_circle(INNER_RADIUS, i*13)
    color = next_color(color, 4)
    print(color)
    draw.line((x1, y1, x2, y2), color, width = 2)
draw.ellipse((RES_X/2 - INNER_RADIUS, 
              RES_Y/2 - INNER_RADIUS, 
              RES_X/2 + INNER_RADIUS,
              RES_Y/2 + INNER_RADIUS),
              (0,0,0,0), (255,255,255,0), 3)
draw.ellipse((RES_X/2 - OUTER_RADIUS, 
              RES_Y/2 - OUTER_RADIUS, 
              RES_X/2 + OUTER_RADIUS,
              RES_Y/2 + OUTER_RADIUS),
              outline = (255,255,255,0), width = 5)
img.save("result.png")
