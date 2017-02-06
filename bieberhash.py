
                                # Hrishikesh Moholkar
"""
this file bieberhash.py is the simulation of hash table.
"""



from hashtable import *



def create_bills(filename,capacity):
    """
    this functions runs the simulation of hash table
    :param filename: name of file
    :param capacity: size of hash table.
    :return:none
    """
    hTable=createHashTable(capacity)
    for line in open(filename):
        line=line.strip().split(' ')


        put(hTable,line[0],int(line[1].strip("$")))

    for name in keys(hTable):
        print(name,"owes $",get(hTable,name),"and is in the seat",indexof(hTable,name))




def main():


    capacity=int(input("How big hash table to use:"))
    y=input("name of input file:")

    create_bills(y,capacity)



main()


