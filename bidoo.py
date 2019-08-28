#coding: utf-8
from PIL import Image, ImageDraw
from sys import exit

N = 15
# N = 5

img = Image.open("picon.jpg")
img = img.resize((500,750), Image.BILINEAR)

out = Image.new("RGB", img.size)
draw = ImageDraw.Draw(out)


for x in range(0, img.size[0]-N, N):
    for y in range(0, img.size[1]-N, N):

        # print(x, y)

        r, g, b = 0, 0, 0

        for i in range(x, x+N):
            for j in range(y, y+N):

                color = img.getpixel((i, j))

                # print(i, j, color)
                r += color[0]
                g += color[1]
                b += color[2]

        r = r//N**2 ; g = g//N**2 ; b = b//N**2 ;

        # print(r, g, b)

        draw.ellipse((x, y, x+N, y+N), fill=(r, g, b))

#        break
#    break
print("%i x %i = %i" % (int(img.size[0] / N), int(img.size[1] / N),\
                       int(img.size[0] / N) * int(img.size[1] / N)))

img.show()
out.show()
