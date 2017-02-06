"""
Name:Hrishikesh Moholkar
file:trending.py
this file computes the top and bottom
trending words between starting word and ending
word.
"""
from wordData import *
import operator
def trending(words,startYr,endYr):
  """
  :param words:a dictionary mapping words to list of year count objects
  :param startYr: an integer starting year for computing trending words
  :param endYr: an integer ,the ending year for computing trending words
  :return:returns a list containing word trend entry for which qualified
  data exists.the list is sorted in descreasing trend value.
  """
  list1=[]
  for item in words.keys():
      startcount = 0
      endcount = 0
      for curyear in words[item]:
          if curyear.year == startYr:
              startcount = curyear.count
          if curyear.year == endYr:
              endcount=curyear.count

      if startcount >= 1000 and endcount >=1000:
          list1.append(WordTrend(item,startcount/endcount))

  list1.sort(key=operator.attrgetter('trend'),reverse=False)
  return list1

def print1(list1):
    """
    this function pritns the trending words.
    :param list1: list from trending function
    :return:none
    """
    print("the top trending words:")
    if len(list1) > 10:
        for i in list1[0:10]:
            print(i.word)
    else:
        for i in list1:
            print(i.word)
    print()
    print("the bottom 10 trending words from:")
    if  len(list1)>10:
        for j in range(len(list1)-1, len(list1)-11, -1):
            print (list1[j].word)
    else:
        list1.reverse()
        for j in list1:
             print (j.word)

if __name__ == "__main__" :
  """
  standalone function
  """
  file=input("enter  word file:")
  year=int(input("enter starting year:"))
  year1=int(input("enter ending year:"))
  var=readWordFile(file)
  x1=trending(var,year,year1)
  print1(x1)









