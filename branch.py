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

#draws a line segment between two points in 2D
def drawLine(point1,point2):
  bob = turtle.Turtle()
  bob.penup()
  bob.hideturtle()
  bob.goto(point1.x,point1.y)
  bob.pendown()
  bob.goto(point2.x,point2.y)
  bob.penup()
  bob.goto(point1.x,point1.y)

#exploits trigonometry to draw a line starting from a point with a specified angle,
#and moves length steps in that direction. Returns the endPoint after drawing. 
def drawLineAtAngle(startPoint,angle,length):
  endPoint_x = startPoint.x + length * np.cos(degrees_to_radians(angle))
  endPoint_y = startPoint.y + length * np.sin(degrees_to_radians(angle))
  endPoint = Point(endPoint_x,endPoint_y)

  drawLine(startPoint,endPoint)
  return endPoint

def tree(n,point,angle,length): #depth of branches
  """TO DO: Create a branching tree """
  return(0)
 
root = Point(-80,0) #root of the tree

#sys.argv[1] allows the user to specific the depth of branches
#python branch.py 8 draws a tree that is 8 branches deep
#python branch.py 4 draws a tree that is 4 brancbhes deep
tree(int(sys.argv[1]),root,0,150)

turtle.done()