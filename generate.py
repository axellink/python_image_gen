import random

from PIL import Image, ImageDraw
import itertools

RES_X=1024
RES_Y=1024
MARGIN=256
    
points = list(itertools.product([MARGIN, RES_X/2, RES_X-MARGIN], repeat=2))

img = Image.new("RGB",(RES_X,RES_Y))
draw = ImageDraw.Draw(img)
color = (255,255,255)
for points in itertools.combinations(points, 2):
    draw.line(points, color, width = 4)
#for x in range(MARGIN, RES_X-MARGIN):
#    for y in range(MARGIN, RES_Y-MARGIN):
#        if img.getpixel((x,y)) == (0,0,0):
#            ImageDraw.floodfill(img,(x,y),(random.randint(0,255),random.randint(0,255),random.randint(0,255)))
img.save("result.png")
