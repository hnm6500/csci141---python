"""
file: mobiles.py
language: python3
author: ben k steele, bks@cs.rit.edu
author: Hrishikesh Nitin Moholkar
description: Build mobiles using a tree data structure.
date: 11/2015
purpose: starter code for the tree mobiles lab
"""

from rit_lib import *

############################################################
# structure definitions
############################################################

class Ball(struct):
    """
    class Ball represents a ball of some weight hanging from a cord.
    field description:
    cord: length of the hanging cord in inches
    weight: weight of the ball in ounces (diameter of ball in a drawing)
    """

    _slots = ((str,"name"),((int,float),"cord"),((int,float),"weight"))

class Rod(struct):
    """
    class Rod represents a horizontal rod part of a mobile with
    a left-side mobile on the end of a left arm of some length,
    and a right-side mobile on the end of a right arm of some length.
    In the middle between the two arms is a cord of some length
    from which the rod instance hangs.
    field description:
    leftmobile: subordinate mobile is a mobile type.
    leftarm: length of the right arm in inches
    cord: length of the hanging cord in inches
    rightarm: length of the right arm in inches
    rightmobile: subordinate mobile is a mobile type.

    An assembled mobile has valid left and right subordinate mobiles;
    an unassembled mobile does not have valid subordinate mobiles.
    """

    _slots = ((str,"name"),((Ball,"Rod",str),"leftmobile"),((int,float),"leftarm"),((int,float),"cord"),((int,float),"rightarm"),((Ball,"Rod",str),"rightmobile"))



#########################################################
# Create mobiles from mobile files
#########################################################

def readMobile( file ):
    """
    readMobile : OpenFileObject -> Map( Ball | Rod )
    readMobile reads the open file's content and
    builds a mobile 'parts map' from the specification in the file.
    The parts map returned has components for assembling the mobile.
    If the mobile is a simple mobile, the returned value is
    a parts map containing a Ball instance.
    If the mobile is complex, the returned value is a parts list of
    the Rod instance representing the top-most mobile component and
    the other parts.
    The connection point for each part is a string that identifies
    the key name of the part to be attached at that point.

    If there is an error in the mobile specification, then
    return an empty parts map.

    # an example of the file format. 'B10' is key for the 10 oz ball.
    # blank lines and '#' comment lines are permitted.
    B10 40 10

    top B10 240 66 80 B30
    B30 55 30
    """
    map1=dict()

    for line in file:
        line1=line.strip().split()
        if line[0] =='#':
            print(line)

        elif len(line1)==3:

           map1[line1[0]]=line1[1:]

        else:
            if len(line1)==6:

                map1[line1[0]]=line1[1:]





    return map1


def constructMobile( partsmap ) :
    """
    constructMobile : Map( Rod | Ball ) -> Ball | Rod | NoneType

    constructMobile reads the partsmap to put together the
    mobile's components and return a completed mobile object.
    The constructMobile operation 'patches entries' in the partsmap.

    The parts map has the components for assembling the mobile.
    Each Rod in partsmap has a key name of its left and right
    subordinate mobiles.  constructMobile reads the key to
    get the subordinate part and attach it at the slot where
    the key was located within the component.

    The top mounting point of the mobile has key 'top' in partsmap.

    If the completed mobile object is a simple mobile, then
    the top returned value is a Ball instance.
    If the completed mobile is a complex mobile, then
    the top returned value is a Rod instance.

    If the parts map contains no recognizable mobile specification,
    or there is an error in the mobile specification, then 
    return None.
    """


    return helper(partsmap,"top")

############################################################
# mobile analysis functions
############################################################
def helper(map,key):
    """
    helper function to construct the mobile
    by joining parts of mobile
    :param map: a dictionary
    :param key: key of dictionary
    :return:constructed mobile
    """
    var=map[key]
    if len(var)==5:
        left=helper(map,var[0])
        right=helper(map,var[4])
        return Rod(key,left,float(var[1]),float(var[2]),float(var[3]),right)
    elif len(var)==2:
        return Ball(key,float(var[0]),float(var[1]))
    else:
        raise Exception("no element present")

def is_balanced( theMobile ) :
    """
    is_balanced : theMobile -> Boolean

    is_balanced is trivially True if theMobile is a simple ball. 

    Otherwise theMobile is balanced if the product of the left side
    arm length and the left side is approximately equal to the 
    product of the right side arm length and the right side, AND
    both the right and left subordinate mobiles are also balanced.

    The approximation of balance is measured by checking
    that the absolute value of the difference between
    the two products is less than 1.0.

    If theMobile is not valid, then produce an exception
    with the message 'Error: Not a valid mobile\n\t{mobile}',

    pre-conditions: theMobile is a proper mobile instance.
    """
    if isinstance(theMobile,Ball):
        return True

    elif isinstance(theMobile,Rod):
        if  abs( (weight(theMobile.leftmobile)*theMobile.leftarm) - (weight(theMobile.rightmobile)*theMobile.rightarm))<0.1:
            return True
        else:
            return False
    else:
        raise Exception( "Error: Not a valid mobile\n\t" + str( theMobile ) )


def weight( theMobile ) :
    """
    weight : theMobile -> Number
    weight of the theMobile is the total weight of all its Balls.

    If theMobile is not valid, then produce an exception
    with the message 'Error: Not a valid mobile\n\t{mobile}',

    pre-conditions: theMobile is a proper mobile instance.
    """

    if isinstance(theMobile,Rod):
        return (weight(theMobile.leftmobile)+weight(theMobile.rightmobile))
    elif isinstance(theMobile,Ball):
        return theMobile.weight

    else:
        raise Exception( "Error: Not a valid mobile\n\t" + str( theMobile ) )

 
def height( theMobile ) :
    """
    height : theMobile -> Number
    height of the theMobile is the height of all tallest side.

    If theMobile is not valid, then produce an exception
    with the message 'Error: Not a valid mobile\n\t{mobile}',

    pre-conditions: theMobile is a proper mobile instance.
    """
    if isinstance(theMobile,Ball):
        return theMobile.cord+theMobile.weight
    elif isinstance(theMobile,Rod):
        left=height(theMobile.leftmobile)
        right=height(theMobile.rightmobile)
        if left>right:
            return left+theMobile.cord
        else:
            return right+theMobile.cord

    raise Exception( "Error: Not a valid mobile\n\t" + str( theMobile ) )


def width( theMobile ) :
    """
    width : theMobile -> Number
    return the rotational diameter width of the theMobile.

    The width of its widest point must take into account 
    the rotation of complex mobiles.

    If theMobile is a Rod with submobiles, then
    the width has special issues because the mobile may spin.
    The possible spin rotation may cause the widest side
    to shift from one side of the hanging point to another.

    To account for this spinning, this function needs help to
    calculate the width of the widest single side.
    Then it takes the widest side width and 
    doubles the widest side to use as the width of whole mobile.

    If theMobile is a only simple Ball,
    then the width of the 'widest side' of the ball is the radius,
    and doubling the radius is the width of the whole mobile.
    (Remember that the ball's weight also represents its diameter.)
    """
    """
    if isinstance(theMobile,Ball):
        return (2*theMobile.weight)

    elif isinstance(theMobile,Rod):
           if width(theMobile.leftarm)>width(theMobile.rightarm):
               return  2*(theMobile.leftarm + width(theMobile.leftmobile))
           if width(theMobile.leftarm)<width(theMobile.rightarm):
               return 2*(theMobile.rightarm + width(theMobile.rightmobile))
    else:
        raise Exception("not present in the file")
    """
    return 2*helper1(theMobile)

def helper1(theMobile):
      """
       helper function to calculate the width
       of the mobile

        :param theMobile: the constructed mobile
        :return:width of mobile
      """


      if isinstance(theMobile,Ball):
        return 0.5*theMobile.weight
      elif isinstance(theMobile,Rod):
        left=helper1(theMobile.leftmobile)+theMobile.leftarm
        right=helper1(theMobile.rightmobile)+theMobile.rightarm
        if left>right:
            return left
        else:
            return right












 
