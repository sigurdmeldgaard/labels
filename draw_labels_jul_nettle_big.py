
from math import *
from random import *
from inkex.transforms import *
from inkex.elements import *
import inkex

marginx = 10
marginy = 10
w = 54
wback=57
d = 21
h = 23
dash_length = 5
page_height = 297

ingredient_margin_x = 4
ingredient_margin_y = 4

copies = floor( (page_height / h)-1)

push_defaults()
tr = Transform()
tr.add_translate(marginx, marginy)
transform(tr)
for i in [- dash_length, copies*h]:
    offsety = i
    offsetx = 0
    for j in [0, d,w,d,wback,3*d/4]:
        offsetx += j
        line ((offsetx, offsety), (offsetx,offsety + dash_length), stroke_width= 0.5,stroke="black", stroke_dasharray=[2,1,])


for i in [- dash_length, sum([0, d,w,d,w,3*d/4])]:
    offsetx = i
    offsety = 0

    for j in [h]*(copies+1):
        line ((offsetx, offsety), (offsetx+dash_length,offsety), stroke_width= 0.5,stroke="black", stroke_dasharray=[2,1,])
        offsety += j


push_defaults()
transform(None)
g=group()

tr = inkex.Transform()
tr.add_translate(d+(w-13)/2-17, 1.5*h/3-2)
tr.add_scale(0.025)
push_defaults()
transform(tr)
im = image('file:///home/yogurth/script/nettle.png', (0,0), True)
g.append(im)
pop_defaults()

tr = inkex.Transform()
tr.add_translate(d+(w-13)/2+24, 1.5*h/3-2)
tr.add_scale(0.028)
push_defaults()
transform(tr)
im2 = image('file:///home/yogurth/script/rosemary.jpg', (0,0), True)
pop_defaults()
g.append(im2)

g.append(text("Brændenælde", (d+w/2,h/4),font_size="5pt", text_anchor="middle", dominant_baseline='middle',font_family="C059"))
g.append(text("Rosmarin", (d+w/2,h/4*2+0.2),font_size="4pt", text_anchor="middle", dominant_baseline='middle',font_family="C059"))
g.append(text("Shampoobar", (d+w/2,h/4*3+0.2),font_size="3pt", text_anchor="middle", dominant_baseline='middle',font_family="C059"))
re = rect((d+w+d + ingredient_margin_x, ingredient_margin_y),(d+w+d+wback - ingredient_margin_x, h-ingredient_margin_y), stroke=None)
g.append(re)
g.append(text("Ingredienser: Olivenolie*, Sheashmør*, Kokosolie*, Abrikoskerneolie*, Ricinusolie*, Arganolie*, Vand, Æbleeddike*, Brændenælde*, Essentiel olie (Pebermynte*)  *=øko",(0,0),
        font_size="1.8pt",
        text_anchor="middle",
        shape_inside=re))
g.to_def()
pop_defaults()

guides.clear()
offsety = 0
for j in [h]*(copies):
    tr = inkex.Transform()
    tr.add_translate(0, offsety)

    clone(g, transform=tr)
    offsety += j
    g1 = guide((0, offsety+marginy), 0)
    guides.extend([g1])
offsetx = marginx
for i in [0,d,w,d,wback,3*d/4]:
    offsetx+=i
    guides.extend([guide((offsetx, 0), 90)])
pop_defaults()
