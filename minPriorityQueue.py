# -*- coding: utf-8 -*-
"""
Created on Sun Apr 22 20:55:15 2018

@author: charan
"""
class minPriority(object):
    def __init__(self):
        self.extractmin
        self.insertintoqueue
        self. Globalarr = []
        self.prioritylist ={}
        self.buildheap
        self.getprio
        self.updateprio
        self.popVertex
        self.minentry=None
    def minheapify(self,arr,nodeindex): # minheapify of the heap
        if nodeindex<len(arr)/2:# check if node is leaf
            leftchild = nodeindex*2+1
            if nodeindex*2+2<len(arr):
                rightchild = nodeindex*2+2
            else:rightchild = None
            #print nodeindex,arr[nodeindex],leftchild, arr[leftchild] , arr[rightchild]
            if arr[leftchild]<arr[nodeindex]:
                smallest = leftchild
            else:
                smallest = nodeindex
            if rightchild!= None and arr[rightchild]<arr[smallest]:
                smallest = rightchild
           # print arr[greatest]
            temp = arr[nodeindex]
            arr[nodeindex]=arr[smallest]
            arr[smallest]=temp
        
            if smallest !=nodeindex:
                self.minheapify(arr,smallest)
    def buildheap(self): # this function builds the min heap
        heapsize = len(self.Globalarr)/2
        for i in range(heapsize):
            i = heapsize-i-1
            self.minheapify(self.Globalarr,i)
        
    def extractmin(self):# this function extracts min from the heap
        if len(self.Globalarr)==1:
            self.minentry =self.Globalarr[0]
            minEntry=self.prioritylist[self.Globalarr[0]]
            return minEntry
        else:
            minElement = self.Globalarr[0]
            minEntry = self.prioritylist[minElement]
            self.buildheap()
            self.minentry =minElement
            return minEntry
    def popVertex(self): # this block returns the poped vertix from the graph
        popreturn1 = self.prioritylist[self.minentry]
        popreturn2 = self.minentry
        if len(self.Globalarr)==1:
            popreturn2 = self.Globalarr.pop()
            popreturn1 = self.prioritylist[popreturn2]
        else:
            self.Globalarr[0] =self.Globalarr.pop()
        del self.prioritylist[self.minentry]
            
        
        self.buildheap()
        return popreturn1, popreturn2
        print 'from popvertex', self.prioritylist , self.Globalarr
            
    def insertintoqueue(self,newentry, priority): # this function inserts elements into the heap
        self.prioritylist[priority] = newentry
        self.Globalarr.append(priority)
        self.buildheap()
        
    def updateprio(self,entry,priority):# this function changes the value of the priority of an element
        del self.Globalarr[:]
        for keys in self.prioritylist.keys():
            if self.prioritylist[keys]==entry :
                self.prioritylist[priority]=self.prioritylist[keys]
                del self.prioritylist[keys]
        for keys in self.prioritylist :
            self.Globalarr.append(keys)
        self.buildheap() 
        
    def getprio(self,entry): # this function returns the priority of an element
        for key in self.prioritylist:
            if self.prioritylist[key]==entry:
                return key
    def checkinheap(self,entry):# this fuciton checks if an element is present in the heap
        for key in self.prioritylist:
            if self.prioritylist[key]==entry:
                return False
        return True


#minPrior = minPriority()
#minPrior.insertintoqueue("a",10)
#minPrior.insertintoqueue("b",15)
#minPrior.insertintoqueue("d",101)
#minPrior.insertintoqueue("c",1)
#print minPrior.Globalarr , minPrior.prioritylist
#print minPrior.getprio("c")
#minPrior.updateprio("b",25)
#print minPrior.Globalarr , minPrior.prioritylist,minPrior.checkinheap('e')

    