                                #Hrishikesh Moholkar
"""
This python file exptrees applies the concept of binary tree to show
the solving of following expression.
"""






from rit_lib import*

class Num(struct):
    """
    num class which stores the number
    it is a part of binary tree.
    """
    _slots=((int),"number")



class Add(struct):
  """
  a class which is an indicator to perform addition operation

  """
  _slots=()



class Mult(struct):
    """
    a class which is an indicator to perform multiplication operation.
    """
    _slots=()



class binarytree(struct):
    """
    the class binary tree is a representation of a tree.
    """
    _slots=((('binarytree',Num),"left"),((Add, Mult),"operator"),(('binarytree',Num),"right"))






def createSum(left, right):
    """

    :param left: left part of binary tree from root
    :param right: right part from root of binary tree
    :return:a binary tree structure with middle part as add operator
    """
    return binarytree(left,Add(),right )



def interp(tree1):
    """

    :param tree1: a tree with expression to
    be evaluated
    :return:the solution for the expression.
    """
    if (isinstance(tree1,Num)):
        return tree1.number

    else:


        if isinstance(tree1.operator, Add):
            return interp(tree1.left)+interp(tree1.right)

        elif isinstance(tree1.operator,Mult):
            return interp(tree1.left)*interp(tree1.right)




def createProd(left,right):
    """

    :param left: left side of root
    :param right: right branch of root
    :return:binary tree with multiplication operator
    as the root
    """
    return binarytree(left,Mult(),right)




def expToString(tree1):
    """

    :param tree1: the binary tree
    :return:string format of binary tree.
    """
    if isinstance(tree1,Num):
        return str(tree1.number)


    if isinstance(tree1.operator,Add):
        return "("+expToString(tree1.left)+"+"+expToString(tree1.right)+")"

    if isinstance(tree1.operator,Mult):
        return "("+(expToString(tree1.left)) +"*"+ (expToString(tree1.right))+")"



def test_interp():
    """
    test case for the binary tree (expression)
    :return:boolean
    """
    test1=createSum(Num(4), Num(6))
    if(interp(test1))==10:

        print(True,":value is 10")

    test2=createProd(createSum(Num(4),Num(6)),Num(7))
    if(interp(test2))==70:
        print(True,":value is 70")

    test3=createSum(createProd(Num(2),Num(2)),Num(3))
    if(interp(test3))==7:
        print(True,":value is 7")

    test4=createSum(Num(2),createProd(Num(2),Num(3)))
    if (interp(test4))==8:
        print(True,":value is 8")

def test_expToString():
    """
    test for displaying the correct expression of binary tree
    :return:boolean
    """
    test1=createSum(Num(4),Num(6))

    print ((expToString(test1)),":exp True")
    test2=createProd(createSum(Num(4),Num(6)),Num(7))
    print(expToString(test2),":exp True")
    test3=createSum(createProd(Num(2),Num(2)),Num(3))
    print(expToString(test3),":exp True")

    test4=createSum(Num(2),createProd(Num(2),Num(3)))
    print(expToString(test4),":exp True")



if __name__ == "__main__" :#
# this line of code prevents running the test functions
# opened in other file

    test_expToString()
    test_interp()










