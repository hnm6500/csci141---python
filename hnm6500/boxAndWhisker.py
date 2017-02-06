"""
Name:Hrishikesh N Moholkar
file:boxAndWhisker.py
this file opens a turtle window and draws
a box and whisker plot.
"""
from wordData import *
import turtle as tt

def boxAndWhisker(small,q1,med,q3,large):
   """
   this function draws the simulation for passed
   values.
   :param small: a no. corresponding to min value of data set
   :param q1: no.first quartile of data set
   :param med: no.correspondin gto median data set
   :param q3: a no.corresponds to third quartile of data set
   :param large: a number corresponding to max value of data set
   :return:none
   """
   tt.left(90)
   tt.forward(20)
   tt.forward(-20)
   tt.right(180)
   tt.forward(20)
   tt.forward(-20)
   tt.left(90)
   tt.forward((q1-small)*5)
   tt.left(90)
   tt.forward(40)
   tt.forward(-40)
   tt.right(180)
   tt.forward(40)
   tt.forward(-40)
   tt.left(90)
   tt.up()
   tt.forward((med-(q1))*5)
   tt.down()
   tt.left(90)
   tt.forward(40)
   tt.forward(-40)
   tt.right(180)
   tt.forward(40)
   tt.forward(-40)
   tt.left(90)
   tt.up()
   tt.forward((q3-med)*5)
   tt.down()
   tt.left(90)
   tt.forward(40)
   tt.forward(-40)
   tt.right(180)
   tt.forward(40)
   tt.forward(-40)
   tt.left(90)
   tt.forward((large-q3)*5)
   tt.left(90)
   tt.forward(20)
   tt.forward(-20)
   tt.right(180)
   tt.forward(20)
   tt.forward(-20)
   tt.right(90)
   tt.forward((large-q3)*5)
   tt.left(90)
   tt.forward(40)
   tt.right(90)
   tt.forward((q3-med)*5)
   tt.forward((med-q1)*5)
   tt.right(90)
   tt.forward(80)
   tt.right(90)
   tt.forward((med-q1)*5)
   tt.forward((q3-med)*5)
   tt.done()

if __name__ == "__main__" :
    """
    standalone execution
    """
    small=int(input("enter the minimum: "))
    q1=int(input("enter  the first quartile:"))
    med=int(input("enter  the median:"))
    q3=int(input("enter  the third quartile:"))
    large=int(input("enter the maximum:"))
    boxAndWhisker(small,q1,med,q3,large)

