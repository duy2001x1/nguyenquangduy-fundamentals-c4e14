from turtle import *

def is_inside(point, rectangle):
    point_x = point[0]
    point_y = point[1]

    rectangle_x = rectangle[0]
    rectangle_y = rectangle[1]

    width = rectangle[2]
    height = rectangle[3]

    if rectangle_x <= point_x <= (rectangle_x + width) and rectangle_y <= point_y <= (rectangle_y + height):
        return True
    else:
        return False
