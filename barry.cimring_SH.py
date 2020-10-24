from vpython import *
#GlowScript 3.0 VPython

scene.caption = """Test Solar System"""
scene.forward = vector(0,-.3,-1)

G = 6.7e-11 # Newton gravitational constant
sunRadius = 6.9634e8
earthRadius = 6.371e6
eDistance = 1.5e6

running = True

def Run(b):
    global running
    running = not running
    if running: b.text = "Pause"
    else: b.text = "Run"
    
button(text="Pause", pos=scene.title_anchor, bind=Run)

bodyList = []

sun = sphere(pos=vector(0,0,0), radius=2e10, color=vector(0.78,0.2,0.05), make_trail=True, trail_type='points', interval=10, retain=100)
sun.mass = 2e30
sun.p = vector(0,0,0) * sun.mass

mercury = sphere(pos=vector(4.3456e10,0,0), radius=4e9, color=vector(0.3,0.1,0), make_trail=True, interval=3, retain=5)
mercury.mass = 3.285e23
mercury.p = mercury.mass*vector(0,4.736e4,0)

venus = sphere(pos=vector(1.086e11,0,0), radius=8e9, color=color.orange, make_trail=True, interval=10, retain=13)
venus.mass = 4.867e24
venus.p = venus.mass*vector(0,3.502e4,0)

earth = sphere(pos=vector(1.5e11,0,0), radius=6.371e6, color=vector(0,0.3,0.7), make_trail=True, interval=10, retain=22)
earth.mass = 5.972e24
earth.p = earth.mass*vector(0,3.002e4,0)

mars = sphere(pos=vector(2.15e11,0,0), radius=9e9, color=color.red, make_trail=True, interval=10, retain=35)
mars.mass = 6.39e23
mars.p = mars.mass*vector(0,2.478e4,0)

jupiter = sphere(pos=vector(766.34e9,0,0), radius=1.4e10, color=color.orange, make_trail=True, interval=10, retain=225)
jupiter.mass = 1.898e27
jupiter.p = jupiter.mass*vector(0,1.307e4,0)

saturn = sphere(pos=vector(1.4928e12,0,0), radius=1.2e10, color=vector(0.4,0.2,0), make_trail=True, interval=10, retain=350)
saturn.mass = 5.683e26
saturn.p = saturn.mass*vector(0,9.68e3,0)

uranus = sphere(pos=vector(2.959e12,0,0), radius=1.0e10, color=vector(0,0.3,0.8), make_trail=True, interval=10, retain=800)
uranus.mass = 8.681e25
uranus.p = uranus.mass*vector(0,6.8e3,0)

neptune = sphere(pos=vector(4.498e12,0,0), radius=1.0e10, color=color.blue, make_trail=True, interval=10, retain=1200)
neptune.mass = 1.024e26
neptune.p = neptune.mass*vector(0,5.43e3,0)

bodyList.append(sun)
bodyList.append(mercury)
bodyList.append(venus)
bodyList.append(earth)
bodyList.append(mars)
bodyList.append(jupiter)
bodyList.append(saturn)
bodyList.append(uranus)
bodyList.append(neptune)

asteroidList = []
 
                # semmajor (au),   eccentricity    , magslopeparam, indlination (deg), longitude of ascending nose, arg of perihelion, perihelion dist (au), aphelion distance, orbital period
asteroid_data = [[2.76916515450648,.07600902910070946,0.12,10.59406704424526,80.30553156826473,73.597694115971,2.558683599692926,2.979646709320033,4.60820180153985],
[2.772465921978979,.2303368211958249,0.11,34.8362344173523,173.0800627473217,310.0488574270735,2.133864934636589,3.41106690932137,4.61644352793619],
[2.669149516961171,.2569423201751032,0.32,12.98891912630602,169.8527598113392,248.1386261811234,1.983332047178912,3.354966986743431,4.36081392268951],
[2.361417895877277,.08872145950956178,0.32,7.141770811873426,103.810804427096,150.7285412870121,2.151909453643047,2.570926338111508,3.62883713822373],
[2.574248919201488,.1910945189312088,0,5.366987944360959,141.5766042141307,358.6876077891718,2.082324060377496,3.066173778025481,4.13032295382172],
[2.425159989654524,.2030071093939073,0.24,14.73790110045524,138.6402027591858,239.8074902310437,1.932835270337001,2.917484708972046,3.77675483787179],
[2.385333813853889,.231205791651457,0,5.523651386735914,259.5632306889722,145.2651058349183,1.833830821068811,2.936836806638967,3.68410457424173],
[2.20176418937401,.1564992508158695,0.28,5.88695455961114,110.8893298901322,285.2874622174554,1.857189743263767,2.546338635484252,3.26711489815842],
[2.385636535575458,.1231142722068342,0.17,5.576815510839905,68.9085766994347,6.417369231417859,2.091930629748052,2.679342441402864,3.68480591875975],
[3.14153917911499,.1124606576702566,0,3.831560034123068,283.2021668627339,312.3152062465516,2.78823961693484,3.49483874129514,5.56829098991105],
[2.453109376165724,.1004722717813071,0,4.629885837761471,125.5465867729847,195.5503937824099,2.206639904214328,2.699578848117119,3.84223187780065],
[2.334315086443524,.2201715811331393,0.22,8.373074237387534,235.410168307321,69.64182011278218,1.820365242998313,2.848264929888735,3.56654261464241],
[2.575981091157315,.08512141533046512,0,16.5361229486575,43.22191706153441,80.54483096060058,2.356709934813488,2.795252247501142,4.13449249989407],
[2.585567305207669,.1665823104724761,0,9.121643598892886,86.12266132527178,97.85899132751493,2.154857529624082,3.016277080791256,4.15759300760529],
[2.644100304490733,.1860843620330185,0.23,11.75242982472844,292.9343386609643,98.49868083964806,2.152074586178265,3.136126022803201,4.29957066894305],
[2.923813680217348,.1335684148335463,0.20,3.096005208804772,150.0456663982905,228.8230713564875,2.53328452168208,3.314342838752617,4.99957103079139],
[2.470354085250579,.1330315975326713,0,5.591204766084532,125.5529436748931,136.2082516830372,2.141718934818333,2.798989235682824,3.88281780512896],
[2.29665350984091,.2176743622521839,0.25,10.12873129564968,150.3838618286583,227.9508469405316,1.79673092177205,2.79657609790977,3.48057840367947],
[2.442710697047048,.1580468510700675,0.10,1.573782207412067,211.1440435363498,182.0650176105087,2.056647963303592,2.828773430790503,3.81782707610074],
[2.409781791609093,.1420667051541423,0.25,.7087512033102101,206.1089108591462,256.7731963771298,2.067432032334743,2.752131550883443,3.74088863881228]]

for i in range( len( asteroid_data) ):
    theta = i*2*pi/len( asteroid_data )
    p = (asteroid_data[i][6] + asteroid_data[i][7])/2
    e = asteroid_data[i][1]
    r = p/(1+e*cos(theta))
    rr = p/(1+asteroid_data[i][1]*cos(theta-pi/2))
    r_p = p*e*sin(theta)/(1+e*cos(theta))^2
    
    y_p = (r_p*sin(theta) + r*cos(theta))/(r_p*cos(theta) - r*sin(theta))
    
    th = atan(y_p)
    
        
    v = (2*p*pi*1.5e11/(365*24*60*60*asteroid_data[i][8]))
        
    print(p, asteroid_data[i][8], v, th, sin(th), cos(th))
    x1 = r*cos(theta)
    y1 = r*sin(theta)
    z1 = 0
    
    if y1 >= 0:
        th += pi
        
    vx = v*cos(th)
    vy = v*sin(th)

    
    w = asteroid_data[i][5]*pi/180
    x2 = x1*cos(w) - y1*sin(w) 
    y2 = x1*sin(w) + y1*cos(w)
    z2 = z1
    
    vx1 = vx*cos(w) - vy*sin(w) 
    vy1 = vx*sin(w) + vy*cos(w)
    vz1 = 0

    om = asteroid_data[i][4]*pi/180

    i = asteroid_data[i][3]*pi/180
    x3 = x2
    y3 = y2*cos(i)
    z3 = y2*sin(i)
    
    vx2 = vx1
    vy2 = vy1*cos(i)
    vz2 = vy1*sin(i)

    x4 = x3*cos(om) - y3*sin(om) 
    y4 = x3*sin(om) + y3*cos(om)
    z4 = z3

    vx3 = vx2*cos(om) - vy2*sin(om) 
    vy3 = vx2*sin(om) + vy2*cos(om)
    vz3 = vz2

    ast = sphere(pos=vector(x4*1.495978707e11,y4*1.495978707e11,z4*1.495978707e11), radius=5e9, color=color.white, make_trail=True, interval=10, retain=10)
    ast.mass = 2e20
   
    ast.p = ast.mass*vector( vx3, vy3, vz3)
    asteroidList.append(ast)


dt = 8.64e4
scene.autoscale = False

while True:
    rate(10000)
    for i in range(len(bodyList)):
        F = vector(0,0,0)
        for j in range(len(bodyList)):
            if i != j:
                r = bodyList[i].pos - bodyList[j].pos
                F += G * bodyList[i].mass * bodyList[j].mass * r.hat / mag(r)**2
        bodyList[i].p = bodyList[i].p - F*dt
        bodyList[i].pos = bodyList[i].pos + (bodyList[i].p/bodyList[i].mass) * dt
        
    for i in range(len(asteroidList)):
        F = vector(0,0,0)
        for j in range(len(bodyList)):
            r = asteroidList[i].pos - bodyList[j].pos
            F += G * asteroidList[i].mass * bodyList[j].mass * r.hat / mag(r)**2
        
        asteroidList[i].p = asteroidList[i].p - F*dt
        asteroidList[i].pos = asteroidList[i].pos + (asteroidList[i].p/asteroidList[i].mass) * dt




