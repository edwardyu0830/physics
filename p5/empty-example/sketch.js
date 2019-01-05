function setup() {
  createCanvas(windowWidth-10, windowHeight-10, WEBGL);
  angleMode(DEGREES);
}

function draw() {
  background(50);
  orbitControl();
  fill(color(255,204,0));
  stroke(color(0,0,0));
  translate(150,100); //at(150,100)
  box(200,100);
  fill(color(255,255,255));
  noStroke();
  translate(-30,-250); //(120,-150)
  cylinder(5,400);
  translate(60,0); //(180,-150)
  cylinder(5,400);
  translate(-30,-200); //(150,-350)
  fill(color('rgba(0,255,0, 0.25)'));
  stroke(color(0,0,0));
  box(400,5,200);
  translate(-650,450); //at(-500,0,0)
  rotateZ(90);
  noStroke();
  fill(color(255,255,255));
  cylinder(7,30);
}

function windowResized() {
  resizeCanvas(windowWidth-10, windowHeight-10);
}
