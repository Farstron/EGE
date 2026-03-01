'''19555'''
import turtle as t
t.speed(100)
t.left(90)
l = 10
for i in range(3):
    t.forward(11*l)
    t.right(90)
    t.forward(24*l)
    t.right(90)
t.up()
t.forward(2*l)
t.right(90)
t.forward(5*l)
t.left(90)
t.down()
for i in range(3):
    t.forward(6*l)
    t.left(90)
    t.forward(9*l)
    t.left(90)
t.up()
for x in range(0,30):
    for y in range(0,15):
        t.goto(x*l,y*l)
        t.dot(5)
t.done()
