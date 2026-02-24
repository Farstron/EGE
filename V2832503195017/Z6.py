'''4746'''
import turtle as t
t.speed(100)
t.left(90)
l = 10
for i in range(20):
    for i in range(4):
        t.forward(15*l)
        t.right(90)
    t.back(20*l)
    t.right(90)
t.up()
for x in range(-20,16):
    for y in range(-30,16): 
        t.goto(x*l,y*l)
        t.dot(5)
t.done()