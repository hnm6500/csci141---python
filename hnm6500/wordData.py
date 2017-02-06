"""
Name:Hrishikesh Moholkar
file:wordData.py
This file is the main file for
all other working files
"""

from rit_lib import*

class YearCount(struct):
    """
    slots for class:
    year: integer representing particular year
    count:an integer representing count for that year
    return:none
    """
    _slots=((int,"year"),(int,"count"))

class WordTrend(struct):
    """
    slots for class:
    word: string representing word
    trend:an integer representing count for that year
    return:none

    """
    _slots=((str,"word"),(float,"trend"))

def readWordFile(filename):
    """
    this function reads the file and returns dictionary
    containing keys as words and values as list of yearcount objects.
    :param filename: input file
    :return:dictionary
    """
    words=dict()
    list1=[]
    for line in open("data"+ '/' + filename):
        if "," not in line:
          word=line.strip()
          words[word]=""

        else:
          x1= [append(line)]

          if words.get(word)!= "":
             words[word] = words.get(word) + x1;
          else:
            words[word] = x1;
    return (words)

def append(value):
    """
    this helper function returns yearcount object
    and appends to list
    :param value:
    :return:yearcount object
    """
    temp=[]
    temp=value.split(",")
    x=YearCount(int(temp[0]),int(temp[1]))
    return x

def totalOccurrences(word,words):
   """
   this function counts the total occurences of
    a word
   :param word:desired word entered
   :param words:dictionary containing keys
   :return:total number of times that word has appeared in print
   """
   x=words[word]
   count2=0
   if word in words.keys():
       for i in range(0,len(x)):
           count1=x[i].count
           count2=count2+count1
   else:
       print("no key")
   return count2

if __name__ == "__main__" :
    """
    standalone execution
    """
    filename=input("enter word file:")
    word=input("enter word:")
    words=readWordFile(filename)
    #print(words)
    v=totalOccurrences(word,words)
    print("total occurences of",word,":",v)










