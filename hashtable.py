                                                                #Hrishikesh Moholkar
"""
this file hashtable.py describes the
working of hashtable based on open addressing based on simulation bieberhash .
"""


"""
description: open addressing Hash Table for CS 141 Lecture
file: hashtable.py
language: python3
author: sps@cs.rit.edu Sean Strout
author: jeh@cs.rit.edu James Heliotis
author: anh@cs.rit.edu Arthur Nunes-Harwitt
author: jsb@cs.rit.edu Jeremy Brown
author: as@cs.rit.edu Amar Saric
"""

from rit_lib import *

class HashTable(struct):
    """
           The HashTable data structure contains a collection of values
       where each value is located by a hashable key.
       No two values may have the same key, but more than one
       key may have the same value.
       table is the list holding the hash table
       size is the number of elements in occupying the hashtable

    """
    _slots = ((list, 'table'), (int, 'size'))


def createHashTable(capacity=100):
    """
    createHashTable: NatNum? -> HashTable
    """
    if capacity < 2:
        capacity = 2
    aHashTable = HashTable([None for _ in range(capacity)], 0)
    return aHashTable   


def HashTableToStr(hashtable):
    """
    HashTableToStr: HashTable -> String
    """
    result = ""
    for i in range(len(hashtable.table)):
        e = hashtable.table[i]
        if not e == None:
            result += str(i) + ": "
            result += EntryToStr(e) + "\n"
    return result


class Entry(struct):
    """
       A class used to hold key/value pairs.
    """

    _slots = ((object, "key"), (object, "value"))


def EntryToStr(entry):
    """
    EntryToStr: Entry -> String
    return the string representation of the entry.
    """
    return "(" + str(entry.key) + ", " + str(entry.value) + ")"


def hash_function(val, n):
    """
    hash_function: K NatNum -> NatNum
    Compute a hash of the val string that is in [0 ... n).
    """
    hashcode = hash(val) % n
    # hashcode = 0
    # hashcode = len(val) % n
    return hashcode

def keys(hTable):
    """
    keys: HashTable(K, V) -> List(K)
    Return a list of keys in the given hashTable.
    """
    result = []
    for entry in hTable.table:
        if entry != None:
            result.append(entry.key)
    return result

def has(hTable, key):
    """
    has: HashTable(K, V) K -> Boolean
    Return True iff hTable has an entry with the given key.
    """
    index =primary(key, len(hTable.table))
    if hTable.table[index] != None and key==hTable.table[index].key:
        return True
    else:
        index=secondary(key,len(hTable.table))
        if hTable.table[index] != None and key==hTable.table[index].key:
            return True

    return False


def put(hTable, key, value):
    """
    put: HashTable(K, V) K V -> Boolean

    Using the given hash table, set the given key to the
    given value. If the key already exists, the given value
    will replace the previous one already in the table.
    If the table is full, an Exception is raised.
    """
    c=primary(key,len(hTable.table))
    rec(hTable,key,value,c)



def rec(hTable,key,value,number):
      if has(hTable,key)==True:
        location = indexof(hTable,key)
        val = get(hTable,key)
        hTable.table[location].value += value

      else:
        index=primary(key,len(hTable.table))
        if hTable.table[number] == None:
            hTable.table[number] = Entry(key, value)
            hTable.size+=1
            return;
        else:
            if primary(hTable.table[number].key,len(hTable.table))==number:
                oldPerson = hTable.table[number].key
                oldPersonVal = hTable.table[number].value
                oPprimary= primary(oldPerson, len(hTable.table))
                oldsecondary1=secondary(oldPerson,len(hTable.table))


                if indexof(hTable,oldPerson)==oPprimary:
                    hTable.table[number]=Entry(key,value)
                    rec(hTable,oldPerson,oldPersonVal,oldsecondary1)

            else:
                raise Exception('Could not seat everyone.')














def get(hTable, key):
    """
    get: HashTable(K, V) K -> V

    Return the value associated with the given key in
    the given hash table.

    Precondition: has(hTable, key)
    """
    if has(hTable,key)==True:

        index = primary(key, len(hTable.table))
        if hTable.table[index].key==key:
            return hTable.table[index].value
        else:
            index=secondary(key,len(hTable.table))

            return hTable.table[index].value

    else:
        raise Exception("Hash table does not contain key:", key)

def primary(str1,sizeoftable):
    """
    returns secondary index of the key
    :param str1: key
    :param sizeoftable:hash table size
    :return:index of key
    """
    temp=1
    for i in str1:
        temp=temp*((ord(i.upper())-ord("A"))+1)
        temp1=temp%sizeoftable
    return temp1

def secondary(str1,sizeoftable):
    """
    returns primary index of the key
    :param str1: key
    :param sizeoftable: hash table size
    :return:index (location)
    """
    temp=0
    for i in str1:
        temp=temp+((ord(i.upper())-ord("A"))+1)
        temp1=temp%sizeoftable
    return temp1


def indexof(hTable,key):
    """
    returns the index of the string(key)
    :param hTable:hash table
    :param key: key in dictionary
    :return:index of key (location)
    """
    index=primary(key,len(hTable.table))
    if hTable.table[index] != None:
        if hTable.table[index].key == key:
            return index

    if hTable.table[secondary(key, len(hTable.table))] != None:
        if hTable.table[secondary(key, len(hTable.table))].key == key:
            return secondary(key,len(hTable.table))

    else:
        return None


