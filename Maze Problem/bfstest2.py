import turtle
import time
import sys
from collections import deque

wn = turtle.Screen()  #define the turtle screen
wn.bgcolor("black")   #set the background color
wn.title("A BFS Maze Solving Program")
wn.setup(1300,700)         # setup the dimension of the working window

# this is the class for the Maze
class Maze(turtle.Turtle):    #define a maze class
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.shape("square")  # the turtle shape
        self.color("white")   # color of the turtle
        self.penup()          # lift up the pen so it do not leave trail
        self.speed(0)

# this os the class for the finish line green square in the maze
class Green(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.shape("square")  # the turtle shape
        self.color("green")   # color of the turtle
        self.penup()          # lift up the pen so it do not leave trail
        self.speed(0)

class Blue(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.shape("square")  # the turtle shape
        self.color("blue")   # color of the turtle
        self.penup()          # lift up the pen so it do not leave trail
        self.speed(0)

# this is the class for the yellow or turtle
class Red(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.shape("square")  # the turtle shape
        self.color("red")   # color of the turtle
        self.penup()          # lift up the pen so it do not leave trail
        self.speed(0)

class Yellow(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.shape("square")  # the turtle shape
        self.color("yellow")   # color of the turtle
        self.penup()          # lift up the pen so it do not leave trail
        self.speed(0)

