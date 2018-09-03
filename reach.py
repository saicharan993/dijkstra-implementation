# -*- coding: utf-8 -*-
"""
Created on Mon Apr 23 20:10:46 2018

@author: charan
"""

class reachable(object):
    def __init__(self,adja,source):
        self.adja = adja
        self.source =source
    def bfs(self): # breath first search implemetation 
        outputreachable=[]
        vertlist={}
        for key in self.adja :
            vertlist[key]=reachableVert(key,self.adja[key].edges,self.adja[key].vertexflag)
        keylist = vertlist.keys()
        source = vertlist[self.source]
        source.color = 'gray'
        queue = queueVertex()
        queue.pushtoque(source)
        for e in source.edges:
            queue.pushtoque(vertlist[e.name])
        while len(queue.vertex)!=0:
            v =queue.pulloutque()
            for e in v.edges:
                if vertlist[e.name].vertexflag =='up'and e.flag=='up':
                    if vertlist[e.name].color=='white' :
                        vertlist[e.name].color ='gray'
                        outputreachable.append(e.name)
                        queue.pushtoque(vertlist[e.name])
        return outputreachable
    
        
class reachableVert(object):# user object of vertix for convinience in breath first search
        
    def __init__(self,name,edges,vertexflag):
        self.edges = edges
        self.name = name
        self.color = 'white'
        self.vertexflag = vertexflag
class queueVertex(object): # queue used in breath first search
    def __init__(self):
        self.vertex=[]
        self.pushtoque
        self.pulloutque
    def pushtoque(self,vertex):
        self.vertex.insert(0,vertex)
    def pulloutque(self):
        return self.vertex.pop()