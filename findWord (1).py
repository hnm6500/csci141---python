                                #Hrishikesh N Moholkar



import turtle
def Count_Words(textFileName):
    """
    this function counts the no.of spaces between the words and adds one
    which equals to number of words.
    :param:textFileName
    :return:
    """
    count=0
    """count variable is assigned to count number of spaces.
    no.of words=no.of spaces between words+1.

    """
    """
    s.strip()command removes  white spaces
    and new lines in the string.




    """

    for line2 in open(textFileName):

        line1=line2.strip()


        for char1 in line1:
            """counts only the no.of spaces
            between words.whose var1=0 and it becomes one
            when encountered space character and increases
            count.
            """
            if char1==" ":
                if var1==0:
                    count=count+1
                var1=1
            else:
                var1=0
        if line1 != "" :
            count=count+1
    print("number of words in file",count)


def main():
    textFileName=input("Enter filename:")
    Count_Words(textFileName)
main()
input("press enter to exit")





























