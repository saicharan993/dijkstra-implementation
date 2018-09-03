# -*- coding: utf-8 -*-
"""
Created on Wed Apr 18 15:51:06 2018

@author: charan
"""
from adjacencylist import vertex
from path import path
from reach import reachable
import sys
#adjatest = vertex('belk',1)
#adjatest.addedge('grigg',0,1.2)
#adjatest.addedge('grigg2',0,1.2)
#adjatest.edges[1].flag = 1
#print adjatest.edges
#print adjatest.vertexflag  
inputgraph ='network.txt' #sys.argv[1]
inputquery = 'input.txt' #sys.argv[2]
outputfile ='output.txt'# sys.argv[3]
output = open(outputfile,'w')
globalAdjacencyList ={}
def makeAdjacencylist(inputfilename):# creating adjacency list from the given graph
    inputnetwork = open(inputfilename,"r")
    adjacencylist ={}
    for line in inputnetwork:
        words = line.split()#problem if input file is not in correct format whole code breaks
        if len(words)==3:
            if words[0] in adjacencylist: # check if vertex is in adjacencylist
                adjacencylist[words[0]].addedge(words[1],"up",words[2])
                if words[1] in adjacencylist:  # adding a undirected edge ; checking if the other edge is in adjacencylist
                    adjacencylist[words[1]].addedge(words[0],"up",words[2])
                else:
                    adjacencylist[words[1]] = vertex(words[0],"up")
                    adjacencylist[words[1]].addedge(words[0],"up",words[2])                    
            else :
                adjacencylist[words[0]] = vertex(words[0],"up")
                adjacencylist[words[0]].addedge(words[1],"up",words[2])
                if words[1] in adjacencylist:  # adding a undirected edge ; checking if the other edge is in adjacencylist
                    adjacencylist[words[1]].addedge(words[0],"up",words[2])
                else:
                    adjacencylist[words[1]] = vertex(words[0],"up")
                    adjacencylist[words[1]].addedge(words[0],"up",words[2])
                
    return adjacencylist
    
def printingAdjacencylist(adjalist):# printing of the graph
    for key in adjalist:
        print >>output, 'Vertex :' ,key , adjalist[key].vertexflag ,'\nVertex egdes : \n'
        for s in adjalist[key].edges:
            print >>output, s.name, s.flag,s.value
        print >>output,'\n'


globalAdjacencyList = makeAdjacencylist(inputgraph)

def addedge(tailvertex , headvertex ,value):# adding edge to edges list of the vertex .Problem it will overwrite old edge
    if headvertex not in globalAdjacencyList.keys() :
        globalAdjacencyList[headvertex]= vertex(headvertex,'up')
    
    globalAdjacencyList[tailvertex].addedge(headvertex,"up",value)
    globalAdjacencyList[headvertex].addedge(tailvertex,"up",value)
    
    
    
def deleteedge(tailvertex,headvertex):# running through list take o(edges)
    edgelist = globalAdjacencyList[tailvertex].edges
    edgelist = filter(lambda x: x.name!= headvertex, edgelist)# use of lambda function
    globalAdjacencyList[tailvertex].edges =edgelist

def edgedown(tailvertex,headvertex):# edge down
    edgelist = globalAdjacencyList[tailvertex].edges
    for ed in edgelist:
        if ed.name == headvertex:
            ed.flag = "down"
    globalAdjacencyList[tailvertex].edges =edgelist

def edgeup(tailvertex,headvertex):# edge up 
    edgelist = globalAdjacencyList[tailvertex].edges
    for ed in edgelist:
        if ed.name == headvertex:
            ed.flag = "up"
    globalAdjacencyList[tailvertex].edges =edgelist

def vertexdown(vertexname):# vertex down
    globalAdjacencyList[vertexname].vertexflag = "down"

def vertexup(vertexname):# vertex up
    globalAdjacencyList[vertexname].vertexflag = "up"

def reachablefunc():# this code handles the reachability 
    vertexlist = globalAdjacencyList.keys()
    for v in vertexlist :
        if globalAdjacencyList[v].vertexflag=='up':
            print >>output, '\n',v ,'\n'
            for i in reachable(globalAdjacencyList,v).bfs():
                print >>output ,i

def shortpath(tail,head):# this returns the shortest path between two vertices
    for i in path().dijstra(tail,head,globalAdjacencyList):
        print >>output, i#incorrect source and destination can break the code
    print >>output,'\n'
inputqueryfile = open(inputquery,'r')    # this code is responsible for routing to various code blocks based of the 
#input in the input query file
for line in inputqueryfile:
        words = line.split()
        if words[0]=='print' :
            printingAdjacencylist(globalAdjacencyList)
        elif words[0]=='reachable' :
            reachablefunc()
        elif words[0]=='path' :
            shortpath(words[1],words[2])
        elif words[0]=='edgeup' :
            edgeup(words[1],words[2])
        elif words[0]=='addedge' :
            addedge(words[1],words[2],words[3])
        elif words[0]=='edgedown' :
            edgedown(words[1],words[2])
        elif words[0]=='vertexup' :
            vertexup(words[1])
        elif words[0]=='vertexdown' :
            vertexdown(words[1])
        elif words[0]=='deleteedge' :
            deleteedge(words[1],words[2])
        
        

            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
        