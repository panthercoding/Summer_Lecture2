"""
Assignment File: sierpinski.py
"""

import turtle 
import numpy as np
import sys

#a new data type to store a 2D coordinate (x,y)
class Point():
  def __init__(self,x,y):
    self.x = x
    self.y = y 

#calculates the midpoint of two coordinates by averaging their x and y coordinates
def midpoint(point1,point2):
  new_point_x = (point1.x + point2.x)/2
  new_point_y = (point1.y + point2.y)/2
  return Point(new_point_x,new_point_y)

#helper functions to convert radians <-> degrees
def radians_to_degrees(radian):
  return(radian * 180/np.pi)
def degrees_to_radians(degrees):
  return(degrees * np.pi/180.0)

#draws a triangle given three Point data objects and colors it green
def drawTrianglePoints(point1,point2,point3):
  bob = turtle.Turtle()
  bob.penup()
  bob.hideturtle()
  bob.goto(point1.x,point1.y)
  bob.pendown()
  bob.fillcolor("light green")
  bob.begin_fill()

  bob.goto(point2.x,point2.y)
  bob.goto(point3.x,point3.y)
  bob.goto(point1.x,point1.y)
  bob.end_fill()

"""TO DO (complete the function)"""
def drawSierpinski(point1,point2,point3,order):
  """
  Complete this function, which should draw a Sierpinski triangle
  with the vertices at the three points of the provided order 

  for the base case order = 1, the function should just draw a
  triangle at the three points (use the provided drawTrianglePoints functions above)

  for the recursive case, consider how you can decompose/break down the image of
  a Sierpinski triangle of order n into Sierpinski triangles of order n-1

  also, remove return(0) below when starting (the function shouldn't return anything)
  """
  return(0)

def main():
  p1 = Point(-150,-130)
  p2 = Point(150,-130)
  p3 = Point(0,130)
  """"
  sys.argv[1] allows the user to specify the order of the triangle when runnning sierpinski.py
  
  python sierpinski.py 5 draws a Sierpinski triangle of order 5
  
  python sierpinski.py 3 draws a Sierpinski triangle of order 3
  """
  drawSierpinski(p1,p2,p3,int(sys.argv[1]))
  turtle.done()

main()

