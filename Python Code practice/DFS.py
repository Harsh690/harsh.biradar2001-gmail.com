from collections import defaultdict

class Graph:
    def __init__(self):
        self.graph = defaultdict(list)

    def addEdge(self,u,v):
        self.graph[u].append(v)

    def DFS(self,s,visited):
       visited.add(s)
       print(s,end=" ")


       for i in self.graph[s]:
           if i not in visited:
               self.DFS(i,visited)


    def dfs(self,s):

       visited = set()

       return self.DFS(s,visited)
# {0: [1, 2], 1: [2], 2: [0, 3], 3: [3]})

g = Graph()
g.addEdge(0, 1)
g.addEdge(0, 2)
g.addEdge(1, 2)
g.addEdge(2, 0)
g.addEdge(2, 3)
g.addEdge(3, 3)
g.dfs(2)

