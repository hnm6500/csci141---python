"""
Name:Hrishikesh N Moholkar
File:this file letterFreq.py computes
the relative frequency of english characters occuring
in print.
"""
from wordData import*
from string import ascii_lowercase

def letterFreq(words):
    """
    this function calculates the
     he relative frequency of english characters occuring
     in print.
    :param words: dictionary
    :return:a string containing characters in descending order
    of frequency.
    """
    map1=dict()
    lst1=[]

    for i in words.keys():
        for ch in i:
            for j in range(0,len(words[i])):
              if ch in map1.keys():
                map1[ch]+=words[i][j].count
              else:
                  map1[ch]=words[i][j].count

    for i in map1.keys():
       lst1=lst1+[i]
    for j in range(0,len(lst1)):
        for k in range(j,len(lst1)):

            if map1[lst1[j]]>=map1[lst1[k]]:
                pass
            else:
               temp= lst1[j]
               lst1[j]=lst1[k]
               lst1[k]=temp
    return   ''.join(lst1)

if __name__ == "__main__" :
    """
    standalone execution
    """
    filename=input("enter wordfile:")
    words=readWordFile(filename)
    print("letter sorted by decreasing frequency:",letterFreq(words))








