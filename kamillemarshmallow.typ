#set page("a4")
#import "@preview/cetz:0.3.0"
#page(background: place(left+top,
cetz.canvas(
  // background: blue,
  {
  import cetz.draw: *
  group({
let marginx = 10mm
let marginy = 10mm
let w = 54mm
let wback=57mm
let d = 21mm
let h = 33mm

let dash_length = 5mm
let page_height = 297mm
let page_width = 210mm
let ingredient_margin_x = 4
let ingredient_margin_y = 4
let copies =  calc.floor((page_height / h)-1)
// Holds the full page
rect((0,0),(page_width, page_height), stroke: (thickness: 0pt))

// Debugs page corners
// let circle_radius = 4mm
// circle((circle_radius, circle_radius), radius: circle_radius)
// circle((circle_radius, page_height - circle_radius), radius: circle_radius)
// circle((page_width - circle_radius, circle_radius), radius: circle_radius)
// circle((page_width - circle_radius, page_height - circle_radius), radius: circle_radius)
translate(x:marginx, y: -marginy)

// | | |
for i in (-dash_length, copies*h) {
  let offsetx = 0mm;
  let offsety = i
  for j in (0mm, d,w,d,wback,3*d/4) {
    offsetx += j;
    line((offsetx, page_height - offsety), (offsetx,page_height -(offsety + dash_length)),stroke:(thickness: 0.5mm,dash:"dashed"))
  }
}
// ---
for i in (-dash_length, (0mm, d,w,d,wback,3*d/4).sum()) {
  let offsetx = i
  let offsety = 0mm
  for j in (h,)*(copies+1) {
    line((offsetx,page_height - offsety),(offsetx + dash_length, page_height - offsety),stroke:(thickness: 0.5mm, dash:"dashed"))
    offsety+=j
  }
}
// Actual labels
let offsety = 0mm
for j in (h,)*copies {
  group({
    translate(y: page_height - offsety)
    // Front
    translate(x:d)
    let image_height = h * 0.5
    let image_y = (h/6*4)
    // content(((w/2),- (h/2 +4mm)),  image("script/wax.jpg",height: h*0.6))
        content(((w/4),- image_y),  image("script/chamomile.jpeg",height: image_height))
                content(((w/4*3),-image_y),  image("script/stokrose.jpg",height: image_height))
    content((w/2,-(h/5)),text(17pt,font: "C059")[Kamille-Stokrose])
    content((w/2,-(h/5)*2),text(13pt,font: "C059")[Shampoobar])
    // rect((0,0),(w,-h)) // debug
    // Back
    translate(x:w+d)
    // rect((0,0),(w,-h)) // debug
    content((w/2,-h/2),[
      #box(height: h,width: w,
      align(center+horizon)[
      #text(7.5pt,font: "C059")[
        Ingredienser: Olivenolie\*, Ricinusolie\*, Solsikke\*, Arganolie\*,  Kokosolie\*, Sheasmør\*, Vand, Lud, Lægestokrose\*, Kamille\*, Essentielle Olier (Kamille, Geranium),  \*=øko
        ] ])
    ], anchor: "center")
  })
  offsety +=j
}

  })
})),[])