# -*- coding: utf-8 -*-
"""
Created on Wed Mar 14 00:55:23 2018

@author: charan
"""
from minPriorityQueue import minPriority
class path(object):
    def __init__(self):
        self.dijstra
    def dijstra(self,source,desti,adja):# dijstra implementations
        heap = minPriority()
        predecessor ={}
        incre =100000
        seen =[]
        path={}
        pathseqlist=[]

        for key in adja :
            heap.insertintoqueue(key,incre)
            predecessor[key] =None
            incre = incre+1
        def Adjacent(currentVert): # this function updates the distance of the adjacent vertices of the vertix that had
            #been poped from from the graph
            #print 'this is current vertex',currentVert
            for e in adja[currentVert].edges:
                if adja[e.name].vertexflag=='up' and e.flag=='up' :
                    if heap.getprio(e.name)>heap.getprio(currentVert)+float(e.value):
                        heap.updateprio(e.name,heap.getprio(currentVert)+float(e.value)) 
                        predecessor[e.name]=currentVert
            seen.append(currentVert)
        heap.updateprio(source,0)
        Adjacent(source)
        heap.extractmin()
        a,b=heap.popVertex()
        path[a]=b
        
        
        for i in range(len(adja)-1):
            Adjacent(heap.extractmin())
            a ,b =heap.popVertex()
            path[a]=round(b,1)
        
        print predecessor,path
        def pathseq(source,tail):# this adds the shortest path between two vertices to the pathseqlist
            for i in range(len(predecessor)):
                if source != tail:
                    source = check(source)
                    print source
                    pathseqlist.append(source)
        def check(a):
            key=[]
           for k in predecessor:
               if predecessor[k]==a:
                   key.append(k)
            return key
            
        pathseq(source,desti)
        totalpath = []
        totalpath.append(source)
        for e in pathseqlist:
            totalpath.append(e)
        totalpath.append(path[pathseqlist[len(pathseqlist)-1]])
        return totalpath
                
            
      
        
        

        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
     
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
