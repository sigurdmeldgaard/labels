
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
""" 
# Draw the background.
circle((cx, cy), r1, fill='black')
ang1, ang2 = pi*0.75, pi*2.25

# Draw the tick marks.
for tick in range(0, 240 + 4, 4):
    # Compute the outer and inner coordinates of each tick.
    rr = r3
    if tick % 20 == 0:
        rr = r4
    ang = (ang2 - ang1)*tick/240 + ang1
    x1 = r2*cos(ang) + cx
    y1 = r2*sin(ang) + cy
    x2 = rr*cos(ang) + cx
    y2 = rr*sin(ang) + cy

    # Draw the tick with an appropriate thickness and color.
    clr = 'white'
    if ang >= pi*1.74:
        clr = 'red'
    thick = 2
    if tick % 20 == 0:
        thick = 6
    line((x1, y1), (x2, y2),
         stroke_width=thick, stroke=clr, stroke_linecap='round')

# Draw the surrounding edge.
arc((cx, cy), r2, (ang1, ang2),
    stroke_width=15, stroke='white', stroke_linecap='square')

# Draw the needle.
ang = pi*1.3
x = r3*cos(ang) + cx
y = r3*sin(ang) + cy
line((cx, cy), (x, y), stroke_width=8, stroke='orange')
circle((cx, cy), r5, fill='#303030') """