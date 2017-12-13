from random import *
from function import *

shapes = [
    {
        'text': 'blue',
        'color': '#3F51B5',
        'rect': [20, 60, 100, 100]
    },
    {
        'text': 'red',
        'color': '#C62828',
        'rect': [140, 60, 100, 100]
    },
    {
        'text': 'yellow',
        'color': '#FFD600',
        'rect': [20, 180, 100, 100]
    },
    {
        'text': 'green',
        'color': '#4CAF50',
        'rect': [140, 180, 100, 100]
    }
]


def get_shapes():
    return shapes


def generate_quiz():
    text_shown = ['BLUE', 'RED', 'YELLOW', 'GREEN']
    color_shown = ['#3F51B5', '#C62828', '#FFD600', '#4CAF50']
    text = choice(text_shown)
    color = choice(color_shown)
    return [
                text,
                color,
                randint(0, 1) # 0 : meaning, 1: color
            ]

def mouse_press(x, y, text, color, quiz_type):
    print(quiz_type)

    click_coordinates = [x, y]

    for dictionary in shapes:
        rect_coordinates = dictionary['rect']
        if is_inside(click_coordinates, rect_coordinates):
            color_clicked = dictionary['color']
            text_clicked = dictionary['text'].upper()
    if quiz_type == 0:
        if text_clicked == text: #text from above
            return True
        else:
            return False
    if quiz_type == 1:
        if color_clicked == color: #color from above
            return True
        else:
            return False

    return True
