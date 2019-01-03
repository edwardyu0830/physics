from vpython import *

g = 9.8
box_m = 0.5
bullet_m = 0.02
isStart = 0
isCollided = 0
v_b = 100
v0 = vector(v_b,0,0)
dt = 0.0001
k = 100000
v = vector(0,0,0)
maxy = 0.

def start(start_btn):
	global isStart
	isStart = 1
	mainfunc()
def reset(reset_btn):
	global isStart
	global g
	global box_m
	global bullet_m
	global v0
	global isCollided
	isCollided = 0
	isStart = 0
	g = 9.8
	box_m = 1
	bullet_m = 0.02
	bullet.pos = vector(-100,0,0)
	v0 = vector(50,0,0)
	box1.pos = vector(0,0,0)
	line1.axis = line2.axis = vector(0,-8,0)
	box1.clear_trail()
	bullet.clear_trail()
	time.sleep(0.3)
	bullet.make_trail = True
	f1.delete()
	f2.delete()
	f3.delete()
def chVelocity(velocity_slider):
	global v0
	if isStart == 0:
		v_b = velocity_slider.value
		velocity_txt.text = "  子彈速度為 %d m/s"%(v_b)
		v0 = vector(v_b,0,0)
	else:
		velocity_txt.text = "  請先按重設再修改"
def chbmass():
	global bullet_m
	if isStart == 0:
		bullet_m = b_mass_slider.value
		b_mass.text = "  子彈質量:%.3f"%(bullet_m)
	else:
		b_mass.text = "  請先按重設再修改"
def chboxmass():
	global box_m
	if isStart == 0:
		box_m = box_mass_slider.value
		box_mass.text = "  木塊質量:%.3f"%(box_m)
	else:
		box_mass.text = "  請先按重設再修改"

scene = canvas(width=800,height=400,center=vector(-2,4,0))
celling = box(pos=vector(0,8,0),size=vector(10,0.2,5))
box1 = box(pos=vector(0,0,0),size=vector(6,2,2),texture=textures.wood,make_trail=True,trail_color=color.orange) 
line1 = cylinder(pos=vector(2,8,0),axis=vector(0,-7,0),radius=0.05)
line2 = cylinder(pos=vector(-2,8,0),axis=vector(0,-7,0),radius=0.05)
height = cylinder(pos=vector(10,0,0),axis=vector(0,0,0))
scene.autoscale = False
bullet = cylinder(pos=vector(-100,0,0),axis=vector(1.5,0,0),radius=0.3,make_trail=True)
bullet.pos.x = -100
start_btn = button(text="開始",bind=start)
reset_btn = button(text="重設",bind=reset)
scene.append_to_caption("\n")
velocity_slider = slider(min=10,max=500,step=10,value=50,bind=chVelocity)
velocity_txt = wtext(text="  子彈速度為 %d m/s"%(v_b))
scene.append_to_caption("\n")
b_mass_slider = slider(min=0.01,max=0.1,step=0.01,value=0.02,bind=chbmass)
b_mass = wtext(text="  子彈質量:%.3f"%(bullet_m))
scene.append_to_caption("\n")
box_mass_slider = slider(min=0.1,max=5,step=0.1,value=0.5,bind=chboxmass)
box_mass = wtext(text="  木塊質量:%.3f"%(box_m))
scene.append_to_caption("\n")
result = wtext(text="")
scene.append_to_caption('\n\n下圖<h3 style="color:MediumSeaGreen">綠線為動能</h3><h3 style="color:DodgerBlue">藍線為位能</h3><h3 style="color:Orange">橘線為總能</h3>\n')
f1 = gcurve(color=color.green)
f2 = gcurve(color=color.blue)
f3 = gcurve(color=color.orange)

def mainfunc():
	global v0
	global dt
	global isCollided
	global isStart
	global v
	global maxy
	global box_m
	global bullet_m
	v = vector(0,0,0)
	maxy = 0.
	t = 0.
	rate(1000)
	bullet.make_trail = True
	while isStart:
		bullet.pos += v0*dt
		if mag(bullet.pos-box1.pos) <= 0.1 and isCollided == 0:
			v = bullet_m*v0/(box_m+bullet_m)
			v0 = vector(0,0,0)
			isCollided = 1
			time.sleep(0.1)
			bullet.make_trail = False
		elif isCollided:
			bullet.pos = box1.pos
			ek = 1/2*(bullet_m+box_m)*mag(v)**2
			eu = (bullet_m+box_m)*g*box1.pos.y
			f1.plot(t,ek)
			f2.plot(t,eu)
			f3.plot(t,ek+eu)
		a = vector(0,-g,0) - k*(mag(box1.pos+vector(2,0,0)-line1.pos)-8)*line1.axis/mag(line1.axis)/box_m - k*(mag(box1.pos+vector(-2,0,0)-line2.pos)-8)*line2.axis/mag(line2.axis)/box_m
		v += a*dt
		box1.pos += v*dt
		line1.axis = box1.pos + vector(2,0,0) - line1.pos
		line2.axis = box1.pos + vector(-2,0,0) - line2.pos
		if box1.pos.y > maxy:
			maxy = box1.pos.y
		height.axis = vector(0,maxy,0)
		result.text = "撞後木塊最高高度為:%.3fm\n估算子彈速度為:%.3lfm/s"%(maxy,sqrt(2*g*maxy)*(bullet_m+box_m)/(bullet_m))
		t += dt