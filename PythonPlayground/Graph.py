#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 25 16:03:28 2021

@author: camillezaug
"""

from collections import defaultdict
from collections import deque



class Graph:
    
    def __init__(self, vert):
        
        self.graph = defaultdict(list)
        self.V = vert
    
    def addEdge(self,u,v):
        self.graph[u].append(v)
    
    def BFS(self,source):
        
        # a list that is currently false for all nodes in the graph
        visited = [False]*(max(self.graph)+1)
        
        queue = deque([])
        
        # visit the root and mark it as visitied
        queue.append(source)
        visited[source] = True
        
        while queue:
            source = queue.popleft()
            print(source, end = " ")
            
            
            for i in self.graph[source]:
                if visited[i] == False:
                    queue.append(i)
                    visited[i]= True
    
    def DFS_recurse(self,source,visited):
        
        root = self.graph[source]
        visited.add(source)
        print(source)
        
        for child in root:
            
            
            if child not in visited:
                visited.add(child)
                self.DFS_recurse(child,visited)

    
    
    def DFS(self,source):
     
        visited = set()
        
        self.DFS_recurse(source,visited)
        
    
    def cycle_recurse(self,v,visited,recStack):
        
        visited[v] = True
        recStack[v] = True
        

        
        for neighbour in self.graph[v]: 
            if visited[neighbour] == False: 
                if self.cycle_recurse(neighbour, visited, recStack) == True: 
                    return True
            elif recStack[neighbour] == True: 
                return True
        
        recStack[v] = False
        return False
      
    
    def detectCycle(self):
        # print(self.V,max(self.graph)+1 )
        visited = [False] * self.V 
        recStack = [False] * self.V 
    
        for node in range(self.V): 
            
            if visited[node] == False: 
                # visited[i]=True
                if self.cycle_recurse(node,visited,recStack) == True: 
                    return True
        return False
        
     
        
        
    
graph = Graph(4)
graph.addEdge(0,1)
graph.addEdge(0,2)
graph.addEdge(1,2)
graph.addEdge(2,0)
graph.addEdge(2,3)
graph.addEdge(3,3)

# graph.BFS(3)
graph.DFS(2)

print("True" if graph.detectCycle() ==True else "False")

