def setup():
    global ellipse_x, ellipse_y
    ellipse_x= 0
    ellipse_y= 0
    size(500,500)
    
def draw():
    global ellipse_x
    global ellipse_y
    global speed
    background(0)
    ellipse(ellipse_x,ellipse_y, 20, 20)
    if ellipse_x > 500:
        speed = -5
    elif ellipse_x == 0:
        speed = 7
    ellipse_x = ellipse_x + speed
    if ellipse_y > 500:
         speed + -5
         
    elif ellipse_y == 0:
        speed = 5
    ellipse_y = ellipse_y + speed
