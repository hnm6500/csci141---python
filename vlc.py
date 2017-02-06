                     # Hrishikesh Moholkar
"""
this file vlc.py describes the functioning of the min heap
of heap data structure.
"""
from array_heap import*
import math




class symbol(struct):
    _slots=((str,"Symbol"),((float),"frequency"),((str,NoneType),"codeword"))
class emptynode(struct):
    _slots=()
class node(struct):
    _slots=((int,"cumfreq"),((list),"symbols"))


def readfile(filename):
    """
    reads the file and stores the input into a dictionary.
    :param filename: input file
    :return:dictionary with filled entries
    """

    map1=dict()
    for line in open(filename):

        line1=line.strip()
        for char in line1:
            if char in map1.keys():
                map1[char].symbols[0].frequency+=1
                map1[char].cumfreq+=1

            else:
                x=symbol(char,1.0,"")
                map1[char]=node(1,[x])


    return map1






def buildheap(map1):
    """
    builds min heap based on map data structure
    :param map1:dictionary
    :return:min heap
    """

    heap1=createEmptyHeap(len(map1.keys()),compareFunc)
    for key in map1.keys():
        add(heap1,map1[key] )
    while heap1.size!=1:
        smallnode=removeMin(heap1)
        smallnode1=removeMin(heap1)
        sum=smallnode.cumfreq+smallnode1.cumfreq
        for each in smallnode.symbols:
            each.codeword = "0" + each.codeword
        for each in smallnode1.symbols:
             each.codeword = "1" + each.codeword
        newNode = node(sum,[])
        """
        newNode = node.symbols.extend(smallnode.symbols)
        newNode = node.symbols.extend(smallnode1.symbols)
        """
        newNode.symbols=smallnode.symbols+smallnode1.symbols
        add(heap1,newNode)
    return heap1




def compareFunc(node1,node2):
    """
    compares the node while sifting up
    :param node1: node of heap
    :param node2: node of heap
    :return:boolean
    """
    if isinstance(node1,node)and isinstance(node2,node):
        if node1.cumfreq<node2.cumfreq:
            return True
        else:
             return False

    else:
        return False
def main():

    filename=input("enter file name:")
    x=readfile(filename)
    var=buildheap(x)
    varnode=removeMin(var)
    top=0
    bottom=0
    for ch in varnode.symbols:
        print("symbol: ",ch.Symbol ,"  codeword is:",ch.codeword,"  frequency is:",ch.frequency)
        top=top+(len(ch.codeword)*ch.frequency)
        bottom=bottom+ch.frequency
    x1=top/bottom
    print("Average VLC codeword length:",x1,"bits per symbol")
    print("Average Fixed codeword length:",math.ceil(math.log(len(varnode.symbols),2)),"bits per symbol")














main()












