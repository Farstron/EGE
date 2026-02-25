'''7808'''
import turtle as t
t.speed(100)
t.left(90)
l = 20
for i in range(120):
    for i in range(8):
        t.forward(4*l)
        t.right(60)
t.up()
for x in range(0,10):
    for y in range(-5,10):
        t.goto(x*l,y*l)
        t.dot(5)
t.done()