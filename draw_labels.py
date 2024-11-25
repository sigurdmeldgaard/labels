
from math import *
from random import *
from inkex.transforms import *
from inkex.elements import *
import inkex

marginx = 10
marginy = 10
w = 54
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
    for j in [0, d,w,d,w,3*d/4]:
        offsetx += j
        line ((offsetx, offsety), (offsetx,offsety + dash_length), stroke_width= 0.5,stroke="black", stroke_dasharray=[2,1,])


for i in [- dash_length, sum([0, d,w,d,w,3*d/4])]:
    offsetx = i
    offsety = 0

    for j in [h]*(copies+1):
        line ((offsetx, offsety), (offsetx+dash_length,offsety), stroke_width= 0.5,stroke="black", stroke_dasharray=[2,1,])
        offsety += j


offsety = 0
for j in [h]*(copies):
    text("Shampoo bar", (d+w/2,offsety+h/2),font_size="6pt", text_anchor="middle", dominant_baseline='middle')
    re = rect((d+w+d + ingredient_margin_x, offsety+ingredient_margin_y),(d+w+d+w - ingredient_margin_x, offsety+h-ingredient_margin_y), stroke=None)

    #t = TextElement(x="0",y="0")
    #t.text="Ingredients: Oil, water, lye, some more stuff"
    #inkex_object(t, transform=None)
    push_defaults()
    transform(None)
    text("Ingredients: Oil, water, lye, some more stuff",(0,0),font_size="2pt",shape_inside=re)
    pop_defaults()

    """     root = FlowRoot()
    region = FlowRegion()
    region.add(rect((d+w+d, offsety),(d+w+d+w, offsety+h)))
    root.add(region)
    div = FlowDiv()
    para = FlowPara() """
    offsety += j
pop_defaults()
