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
let w = 55mm
let wback=56mm
let d = 25mm
let h = 23mm

let dash_length = 5mm
let page_height = 297mm
let page_width = 210mm
let ingredient_margin_x = 4
let ingredient_margin_y = 4
let copies =  calc.floor((page_height / h)-1)
// Holds the full page
rect((0,0),(page_width, page_height), stroke: (thickness: 0pt))

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
  let offsety = 0mm
  for i in (h,)*(copies+1) {
    line((0,page_height - offsety),((0mm, d,w,d,wback,3*d/4).sum(), page_height - offsety),stroke:(thickness: 0.1mm, dash:"dashed"))
    offsety+=i
  }
// Actual labels
let offsety = 0mm
for j in (h,)*copies {
  group({
    translate(y: page_height - offsety)
    // Front
    translate(x:d)
    let image_height = h * 0.7
    let image_y = (h/6*4)-1mm
    content(((w/6),- (h/2 +4mm)),  image("rosemary.png",height: h*0.6))
        // content(((w/2),- image_y),  image("rosemary.png",height: image_height))
               content(((w/6*5),-image_y),  image("nettle.png",height: image_height))
    content((w/2,-(h/5)),text(13.5pt,font: "C059")[Brændenælde])
        content((w/2,-(h/5*2.2)),text(13pt,font: "C059")[Rosmarin])
    content((w/2,-(h/5)*3.7),text(12pt,font: "C059")[Shampoobar])
    // rect((0,0),(w,-h)) // debug
    // Back
    translate(x:w+d)
    // rect((0,0),(w,-h)) // debug
    content((w/2,-h/2),[
      #box(height: h,width: w,
      align(center+horizon)[
      #text(7.5pt,font: "C059")[
        Ingredienser: Olivenolie\*, Sheashmør\*, Kokosolie\*, Abrikoskerneolie\*, Ricinusolie\*, Arganolie\*, Vand, Æbleeddike\*, Brændenælde\*, Essentielle olier (Pebermynte\*, Rosmarin\*, Tea Tree\*)  \*=øko
        ] ])
    ], anchor: "center")
  })
  offsety +=j
}

  })
})),[])