colors = ['red', 'blue', 'brown', 'yellow', 'grey']

from turtle import*

for i in range(5):
    begin_fill()
    color(colors[i])
    for j in range(2):
        forward(100)
        left(90)
        forward(200)
        left(90)

    penup()
    forward(100)
    pendown()

    end_fill()

mainloop()
