# -*- coding: utf-8 -*-
"""
Created on Sat Jul 18 05:19:45 2020

@author: Owais Raza
"""
#Write a program that uses the turtle module and a for loop to draw something. It doesn’t have to be complicated, but draw something different than we have done in the past. (Hint: if you are drawing something complicated, it could get tedious to watch it draw over and over. Try setting .speed(10) for the turtle to draw fast, or .speed(0) for it to draw super fast with no animation.)



import turtle
star = turtle.Turtle()
for i in range(10):
    star.forward(15)
    star.left(90)
    star.forward(15)
    star.right(45)
    star.forward(15)
    star.left(45)
    star.forward(15)
    star.right(45)
turtle.done()