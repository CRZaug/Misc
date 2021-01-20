#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 19 21:38:12 2021

@author: camillezaug
"""


class LinkedListNode(object):

    def __init__(self, value):
        self.value = value
        self.next  = None
        


def createLinkedList(array):
    if len(array)>1:
        head = LinkedListNode(array[0])
        head.next = LinkedListNode(array[1])
        temp = head.next
        for k in range(2,len(array)):
            temp.next = LinkedListNode(array[k])
            temp = temp.next
    
        return head
    elif len(array)==1:
        head = LinkedListNode(array[0])
        return head
    else:
        print("Need to enter a nonzero array")

def printLinkedList(head): 
    
    temp = head
    
    while temp!=None:
        print(temp.value)
        temp = temp.next
    
    return 1


def advance(placesToAdvance,head):
    k = 0
    temp = head
    while k < placesToAdvance:
        temp = temp.next
        k+=1
    
    return temp

def reverseLinkedList(head):
    
    temp = head
    
    # Find the lenght of the linked list
    counterEnd = 0
    while temp!=None:
        counterEnd+=1
        heldValue = temp.value
        temp = temp.next
        
    # print(heldValue)
        
    if counterEnd ==0 or counterEnd ==1:
        return head
    
    counterEnd -=1
    counterBeg = 0
    
    print(counterEnd)


    # Case 1: the total linked list is odd
    if counterEnd %2 ==0:
        while counterBeg != counterEnd:

        # Starting at the "first" node
            temp = advance(counterBeg,head)
            nodeValue = temp.value
            temp.value = heldValue
            heldValue = nodeValue
            counterBeg+=1
        
        # Then replace what was found at the "last" node
            temp = advance(counterEnd,head)
            nodeValue = temp.value
            temp.value = heldValue
            heldValue = advance(counterEnd-1,head).value
            counterEnd -=1
        
          
    # Case 2: the total linked list is even
    else:
        while counterEnd - counterBeg!= -1:

        # Starting at the "first" node
            temp = advance(counterBeg,head)
            nodeValue = temp.value
            temp.value = heldValue
            heldValue = nodeValue
            counterBeg+=1
        
        # Then replace what was found at the "last" node
            temp = advance(counterEnd,head)
            nodeValue = temp.value
            temp.value = heldValue
            heldValue = advance(counterEnd-1,head).value
            counterEnd -=1
   
    return head
    
    
if __name__ == "__main__":
    
    linkedListHead = createLinkedList([1,2,3,4,5,6,7,8])
    printLinkedList(linkedListHead)
    rLL = reverseLinkedList(linkedListHead)
    
    printLinkedList(rLL)
    
    
    