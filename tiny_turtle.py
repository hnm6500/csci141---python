"""                                                                    #Hrishikesh Moholkar
assignment: TinyTurtle interpreter strings lab
author: ben k steele, bks@cs.rit.edu
date: 9/2015
description: TinyTurtle Interpreter
file: tiny_turtle.py
language: python3
purpose: provided starter code of the tiny turtle interpreter
term: 20151

use: student must complete and test this module.
"""

from turtle import *

####################################################################
# The "tt" names are a specified public interface.
# STUDENT: complete the definitions for the stubbed functions.
####################################################################
import turtle
def ttInterpret( program ):
    """
    interpret program as a TinyTurtle language string.
    program -- a TinyTurtle string, possibly with string manipulation symbols
    """
    # REMOVE THIS LINE AND THE print STATEMENT WHEN YOU IMPLEMENT THIS FUNCTION.

    program=ttExpand(program)
    ttEvaluate(program)
    return

def ttEvaluate( program ) :
    """
    evaluate program as a TinyTurtle language program.
    program -- a TinyTurtle string.
    precondition: program contains only TinyTurtle drawing commands.
    """
    # REMOVE THIS LINE AND THE print STATEMENT WHEN YOU IMPLEMENT THIS FUNCTION.
    for ch in program:
         if ch.isdigit():
            turtle.forward(int(ch))
         elif ch=="<":
            turtle.left(15)
         elif ch=="L":
            turtle.left(90)
         elif ch==">":
            turtle.right(15)
         elif ch=="R":
            turtle.right(90)
         elif ch==" ":
            pass



    return

def ttExpand( program ) :
    """
    expand the string manipulation symbols in program into
    a TinyTurtle language program.
    program -- a TinyTurtle string, possibly with string manipulation symbols
    Returns -- a TinyTurtle string after expansion
    """
    # REMOVE THIS LINE AND THE print STATEMENT WHEN YOU IMPLEMENT THIS FUNCTION.

    end=0
    start=0
    teststring=""
    for ch in program:
        if ch=="@":
             start=len(teststring)
        elif ch=="/":
            teststring=teststring+teststring[start:end]
        elif ch=="!":
            backward=reverseString(teststring[start:end],"")
            test1 = ""
            for ch in backward:
                if ch=="R":
                    test1=test1 + "L"
                elif ch=="L":
                    test1=test1 + "R"
                elif ch=="<":
                    test1=test1 + ">"
                elif ch==">":
                    test1=test1 + "<"
                else:
                    test1=test1+ch
            teststring=teststring+"RR"+test1+"RR"
        elif ch== "=":
            backward=reverseString(teststring[start:end],"")
            test1= ""
            for ch in backward:
                if ch=="R":
                    test1=test1 + "L"
                elif ch=="L":
                    test1=test1 + "R"
                elif ch=="<":
                    test1=test1 + ">"
                elif ch==">":
                    test1=test1 + "<"
                else:
                    test1=test1+ch
            teststring=teststring+"RR"+test1+"RR"+test1
        else:
            teststring=teststring+ch
            end=len(teststring)
    return teststring



def reverseString(string,ac):
    if string=="":
        return ac
    else:
        return reverseString(string[1:],string[0]+ac)


# # # # # #

def main():
    """ main function loops prompting for a string to interpret.
    """
    while True:
        program = input( "Enter a tiny turtle string to interpret: " )
        if program == "":
            break
        print( 'expanded string:', ttExpand( program ) )
        ttInterpret( program )
    return
VAR=input("input tiny turtle string")
print(ttExpand(VAR))


main()
