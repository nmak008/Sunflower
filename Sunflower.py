"""
This is the Template Repl for Python with Turtle.

Python with Turtle lets you make graphics easily in Python.

Check out the official docs here: https://docs.python.org/3/library/turtle.html
"""

import turtle

t = turtle.Turtle()
t.speed(0)

x = ['yellow']
for shape in range(31):
  t.color('yellow')
  t.penup()
  t.goto(0, 30)
  t.pendown()
  t.circle(150, 50)
  t.left(130)
  t.circle(150, 50)
  for c in x:
    t.color(c)
    t.fillcolor('yellow')
    t.begin_fill()
    t.circle(120, 50)
    t.left(130)
    t.circle(120, 50)
    t.end_fill()

t.penup()
t.goto(-39, 76)
t.pendown()
t.fillcolor('#663300')
t.begin_fill()
t.circle(60)
t.end_fill()

colors = ["#944C00"]

for shape in range(20):
  t.color('#944C00')
  t.penup()
  t.goto(0, 30)
  t.pendown()
  t.circle(30)
  for c in colors:
    t.color(c)
    t.forward(50)
    t.left(130)
  t.left(7)

y = ['#CC6600']
for shape in range(30):
  t.penup()
  t.goto(0, 30)
  t.pendown()
  t.circle(10)
  print(shape)
  for c in y:
    t.color(c)
    t.forward(5)
    t.left(180)
  t.left(6)
