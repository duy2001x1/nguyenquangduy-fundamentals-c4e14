# from turtle import*
#
# width(6)
# color('pink')
# n = int(input("Enter a number of dashes:"))
#
# for i in range(n):
#     if (i + 1) % 3 == 0:
#         color('red')
#     else:
#         color('blue')
#     forward(50)
#     penup()
#     forward(50)
#     pendown()
#
# mainloop()



from turtle import*

width(6)
color('pink')
n = int(input("Enter a number of dashes:"))

for i in range(n):
    if i % 6 >= 3:
        color('red')
    else:
        color('blue')
    forward(50)
    penup()
    forward(50)
    pendown()

mainloop()
