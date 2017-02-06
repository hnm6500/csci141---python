                                        #Hrishikesh Moholkar


                    #search .py(searchchar,searchstring,matchstring,matchpat,searchpat)
def searchChar(x,y):#the function searches for a character in string.if found return true else if empty string given returns false.
                    #if character given doesn't match returns false.



  if x=="":
    return False
  elif x==y[0]:
    return True
  

  else:

    return searchChar(x,y[1:len(y)])



def searchString(x,y):#if substring given ,it checks in the string whether it is present.if present returns true.
                      #if not present returns false.

    if x in y:
        return(True)
    else:
        return(False)







def matchString(x,y):#checks whether the given substring is a prefix of the string.if the substring is a prefix of string ,
                     #returns true else if the substring is not prefix of string it returns false.
    if x==" " and y==" ":
        print("no string")
    else:
        for ch in x:
            for ch1 in y:
                if ch==ch1:
                    return (True)
                else:
                    return (False)



def matchPat(patx,y):      #if the given pattern matches the initial portion of string it returns true else,
                           #it returns false.
   if patx=="":
       return True
   elif y=="":
       return False
   elif patx[0]=="*":
       return matchPat(patx[1:],y)
   elif patx[0]==y[0]:
       return matchPat(patx[1:],y[1:])
   else:
       return matchPat(patx,y[1:])
def matchpatrec(patx,y):
    if patx[0]==y[0]:
        return matchPat(patx,y)
    else:
        return False

def searchPat(patx,y):                 #if the given pattern matches some portion of string it returns true else
                                       #it returns false.
    if patx[0]==y[0]:
        return matchPat(patx[1:],y[1:])
    return searchPat(patx,y[1:])
#def test():


                                        #print(searchChar(input("enter character"),input("enter string")))
                                        #print(searchChar("b""abc"))
                                        #print(searchChar("d","abc"))
                                        #print(searchChar("a",""))
                                        #print(matchString(input("enter the prefix"),input("enter string")))
                                        #print(matchString("a","abc"))
                                        #print(matchString("ab","abc"))
                                        #print(matchString("bc","abc"))
                                        #print(matchString("ab",""))
                                        #print(searchString(input("enter characters"),input("enter the string")))
                                        #print(searchString("ab","abc"))
                                        #print(searchString("bc","abc"))
                                        #print(searchString("ac","abc"))
                                        #print(searchString("ab","abc"))
                                        #print(matchPat(input("enter the characters"),input("enter the string")))
                                        #print(matchPat("a*t*r", "anteaters"))
                                        #print(matchPat("a*t*r","artist"))
                                        #print(matchPat("a*t*r", "albatross"))
                                        #print(searchPat(input("enter characters"),input("enter string")))







def main():
    x=input("enter substring:")                #x=a y=abc output=true
    y=input("enter main string:")
    searchChar(x,y)
    print(searchChar(x,y))
    input("press enter to continue")


    x=input("enter substring:")                #x=ab y=abc output=true
    y=input("enter main string:")
    matchString(x,y)
    print(matchString(x,y))
    input("press enter to continue")
    x=input("enter substring:")                 #x=ac y=abc output=false
    y=input("enter main string:")
    searchString(x,y)
    print(searchString(x,y))
    input("press enter to continue")
    patx=input("enter pattern string:")         #patx=a*t*r   y=artist output=false
    y=input("enter String:")
    matchpatrec(patx,y)
    print(matchpatrec(patx,y))
    input("press enter to continue")
    patx=input("enter pattern string:")         #patx=a*t*r y=The artist painted output=false
    y=input("enter String:")
    searchPat(patx,y)
    print(searchPat(patx,y))
main()
#test()