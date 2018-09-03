# -*- coding: utf-8 -*-
"""
Created on Sat Apr 21 01:20:01 2018

@author: charan
"""

class vertex(object):# this is user defined custom vertex object for the facilitation of the adjacency list creation
    def __init__(self, vertexname,vertexflag):
        self.vertexname = vertexname
        self.edges = []
        self.vertexflag =vertexflag
        self.addedge
    def addedge(self,name,flag,weight):
        self.edges.append(edge(name,flag,weight))
class edge (object):
   def __init__(self,name,flag,value):
       self.name = name
       self.flag = flag
       self.value = value