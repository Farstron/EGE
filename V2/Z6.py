'''25345'''
import turtle as t
t.speed(100)
t.left(90)
l = 13
for i in range(6):
    t.forward(33*l)
    t.right(90)
    t.forward(20*l)
    t.right(90)
t.up()
t.forward(3*l)
t.right(90)
t.forward(9*l)
t.left(90)
t.down()
for i in range(6):
    t.forward(24*l)
    t.right(90)
    t.forward(25*l)
    t.right(90)
t.up()
for x in range(0,22):
    for y in range(0,34):
        t.goto(x*l,y*l)
        t.dot(5)
t.done()