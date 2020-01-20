import math

def area(radius):
    return math.pi * radius**2


def distance(x1,y1,x2,y2):
    d = math.sqrt((x2-x1)**2+(y2-y1)**2)
    return d

def circle_area(xc,yc,xp,yp):
    return area(distance(xc,yc,xp,yp))

print(circle_area(1,2,4,6))