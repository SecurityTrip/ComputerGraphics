import math
import numpy as np
from PIL import Image
import OBJParcer as parse
import LineDrawer as drawer

image_matrix_white = np.full((200, 200), 255, dtype=np.uint8)
image_matrix_black = np.full((200, 200), 0, dtype=np.uint8)
image_matrix_red = np.full((200, 200, 3), (255, 0, 0), dtype=np.uint8)

matrix = np.matrix((200, 200))

x0, y0 = 10, 170
x1, y1 = 80, 20

point_count = 100

image_matrix = np.full((200, 200, 3), (0, 0, 0), dtype=np.uint8)

img = Image.new(mode='L', size=[200, 200])
for i in range(len(image_matrix)):
    for j in range(len(image_matrix[i])):
        img.putpixel((i, j), ((i + j) % 256))

image1 = Image.fromarray(image_matrix_white, mode='L')
image2 = Image.fromarray(image_matrix_black, mode='L')
image3 = Image.fromarray(image_matrix_red, mode='RGB')

line_img1 = Image.new(mode='L', size=[200, 200])
line_img2 = Image.new(mode='L', size=[200, 200])
line_img3 = Image.new(mode='L', size=[200, 200])
line_img4 = Image.new(mode='L', size=[200, 200])

model_p = Image.new(mode='L', size=[1000, 1000])
model_v = Image.new(mode='L', size=[1000, 1000])

for a in range(12 + 1):
    drawer.LineDrawer.line1(100, 100, 100 + 95 * math.cos((2 * math.pi * a) / 13),
                            100 + 95 * math.sin((2 * math.pi * a) / 13),
                            line_img1)
    drawer.LineDrawer.line2(100, 100, 100 + 95 * math.cos((2 * math.pi * a) / 13),
                            100 + 95 * math.sin((2 * math.pi * a) / 13),
                            line_img2)
    drawer.LineDrawer.line3(100, 100, 100 + 95 * math.cos((2 * math.pi * a) / 13),
                            100 + 95 * math.sin((2 * math.pi * a) / 13),
                            line_img3)
    drawer.LineDrawer.line4(100, 100, 100 + 95 * math.cos((2 * math.pi * a) / 13),
                            100 + 95 * math.sin((2 * math.pi * a) / 13),
                            line_img4)

obj = parse.Parser('objs/model_1.obj')
print(obj.v_arr)

d = drawer.LineDrawer()
drawer.LineDrawer.DrawObjPoints(obj, model_p)

drawer.LineDrawer.DrawObjModel(obj, model_v)

img.save('img/image.png')
image1.save('img/image1.png')
image2.save('img/image2.png')
image3.save('img/image3.png')

line_img1.save("img/lines1.png")
line_img2.save("img/lines2.png")
line_img3.save("img/lines3.png")
line_img4.save("img/lines4.png")

model_p.save("img/model.png")
model_v.save("img/modelv.png")
