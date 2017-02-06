"""
Name:Hrishikesh N Moholkar
file:wordLength.py
this file computes the distribution of word length
and the five no.summary of those word length .
"""

from wordData import*
from boxAndWhisker import*

def summaryFromWords(words,year):
    """
    this function computes the distribution of word length
    and the five no.summary of those word length .calculates
    minimum,maximum,median,1stquartile,thirdquartile
    :param words: A dictionary mapping words to list of YearCount objects
    :param year: A natural no.representing the year of interest .
    :return:a five tuple containing five nos representing five number summary.
    """
    lengthMap = {}
    for i in words.keys():
        for i1 in range(0,len(words[i])):
            if words[i][i1].year==year:
                if len(i) in lengthMap:
                    lengthMap[len(i)] += words[i][i1].count
                else:
                    lengthMap[len(i)] = words[i][i1].count
                break
    lengthList = []
    for i in lengthMap.keys():
        lengthList.append([i, lengthMap[i]])
    lengthList = sorted(lengthList, key=lambda x: x[0])

    sumofcount = 0
    for i in lengthList:
        sumofcount += i[1]

    q1Index = sumofcount * 0.25
    medianIndex = sumofcount * 0.50
    q3Index = sumofcount * 0.75
    min1=0
    max1=0
    tuple1=()
    q1=0
    q2medindex=0
    q3index1=0

    for i in lengthList:
        q1Index -= i[1]
        if q1Index <= 0:
            q1 = i[0]
            break
    for i in lengthList:
        medianIndex-=i[1]
        if medianIndex<=0:
            q2medindex=i[0]
            break
    for i in lengthList:
        q3Index-=i[1]
        if q3Index<=0:
            q3index1=i[0]
            break

    min1=lengthList[0][0]
    max1=lengthList[len(lengthList)-1][0]

    tuple1=(min1,q1,q2medindex,q3index1,max1)
    return (tuple1)

if __name__ == "__main__" :
    """
    standalone execution.
    """
    filename=input("enter wordfile:")
    year=int(input("enter year:"))
    x1= summaryFromWords(readWordFile(filename),year)
    #print(x1)
    print("minimum:",x1[0])
    print(" 1st quartile:",x1[1])
    print("median:",float(x1[2]))
    print(" 3rd quartile:",x1[3])
    print("maximum:",x1[4])
    boxAndWhisker(x1[0],x1[1],float(x1[2]),x1[3],x1[4])






















