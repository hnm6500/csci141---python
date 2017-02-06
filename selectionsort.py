

                          #Hrishikesh Moholkar
#Implementation of selection sort


def swap(lst,current,min):
    """

    :param lst:unsorted list
    :param current: index with greater value
    :param min: index with minimum value
    :return:ascending order list
    """

    temp=lst[current]
    lst[current]=lst[min]
    lst[min]=temp

def findMinFrom(lst,mark):
    """

    :param lst: unsorted list
    :param mark: counter moving through list
    :return:var1:index with minimum value
    """

    for var1 in range(mark,len(lst)):

        var=lst[var1]
        while var<=lst[mark]:
            if mark==len(lst)-1:
                return var1

            else:
                mark=mark+1


def selectionSort(lst):
    """

    :param lst: list of integers
    :return:sorted list of integers
    """
    for mark in range( 0,len(lst)-1):
        swap(lst,mark,findMinFrom(lst,mark))
    return lst
def makelst():
    """
    file:stores the input file
    numbers:is a list that stores the positive integers after input file
    is opened and read.
    :return:list of numbers
    """


    file=input("enter filename")
    x=open(file)
    numbers=[]
    for line in x:
      numbers+=[int(line)]
    return numbers
def main():
    """
    numbers:calls the makelst()
    :return:
    """
    number=makelst()
    print(selectionSort(number))




main()
"""
calls main function
"""

#1.insertionsort performs less comparison as compared to selection sort .We can see from above that
#selction sort has to check by going through every element,while insertion sort has to test little because it
#compares n to n+1 while selection sort compares n to every element of the list.
#2.selection sort has to perform n-1 comparison .even if the list is sorted it goes testing every element.














































































