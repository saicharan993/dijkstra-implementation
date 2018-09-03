Program Overview : 
Implementing Open Shortest Path First protocol using dijistras algorithm , manipulation of the network nodes and network connections. 

My programme uses minimum binary heap for dijstras and reachability (i have used breath first search for reachability)

the complexity of reachability is O(V+E) where v is vertices of the graph and E is edges in the graph

Files : main.py , minPriorityQueue.py , path.py , reach.py , adjacencylist.py

Programming Language : Python 2

Programming Language : Python 2.7

IDE used -Spyder 2.0

how to run ?

python main.py inputgraphfilename.txt QueriesFileName.txt OutputFilename.txt

Limitations: 
Progamme breaks if the input format in the input and graph files is not consistent with specified format

Programme breaks if user tries to find the shortest path between two vertices which are not reachable with repective to each other.