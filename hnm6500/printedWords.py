"""
Name:Hrishikesh Nitin Moholkar
File:printedWords.py
this file computes the total
printed words for each year
"""
from wordData import*
import simplePlot

def printedWords(words):
   """
   this function makes a list of
   yearcount entry for each year for which
   data exist.
   :param words: A dictionary mapping words to list
   of yearcount objects.
   :return:a list containing yearcount object sorted in
   ascending order of year
   """
   list1=[]
   map1=dict()
   for each in words:
       for Yearcount1 in words[each]:
           if Yearcount1.year in map1:
              map1[Yearcount1.year].count+=Yearcount1.count
           else:
               map1[Yearcount1.year]=YearCount(Yearcount1.year,Yearcount1.count)
   for key11 in map1.keys():
       list1.append(map1[key11])
   return list1

def wordsForYear(year,yearList):
    """
    this function returns the count representing total no. of
    printed words for the particular year.if no entry then returns 0
    :param year: an integer representing the year being queried
    :param yearList: list of yearcount object
    :return:an integer count representing the total no.of printed words
    for that year.if no entry in yearlist then return 0
    """
    for i in yearList:
        if i.year==year:
            return i.count
    return 0

if __name__ == "__main__" :
    """
    standalone execution.
    """
    x=input("enter word file:")
    words=readWordFile(x)
    var1=printedWords(words)
    year=int(input("Enter year:"))
    Totalwords=wordsForYear(year, var1)
    print("Total printed words in",year,":",Totalwords)
    import simplePlot
    labels='year','Totalwords'
    plot=simplePlot.plot2D('Number of Printed words over time',labels)
    wordsByYearList=var1
    for yc in wordsByYearList:
        point=yc.year,yc.count
        plot.addPoint(point)
    plot.display()

