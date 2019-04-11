from collections import defaultdict
class graph:
    def __init__(self):
        self.graph=defaultdict(list)
    def addedge(self,u,v):
        self.graph[u].append(v)
        self.graph[v].append(u)
    def dfs(self):
        visited={}
        for i in self.graph.keys():
            visited[i]=False
        i=list(self.graph.keys())[0]
        print(i)
        visited[i]=True
        stack=[]
        for j in self.graph[i]:
            if visited[j]==False and j not in stack:
                stack.append(j)
        while stack:
            s=stack.pop()
            for j in self.graph[s]:
                if visited[j]==False and j not in stack:
                     stack.append(j)
            print(s)
            visited[s]=True

    def bfs(self):
        visited={}
        for i in self.graph.keys():
            visited[i]=False
        i=list(self.graph.keys())[0]
        print(i)
        visited[i]=True
        stack=[]
        for j in self.graph[i]:
           if visited[j]==False and j not in stack:
                 stack.append(j)
           while stack:
              s=stack.pop(0)
              for j in self.graph[s]:
                 if visited[j]==False and j not in stack:
                        stack.append(j)
              print(s)
              visited[s]=True
                 
                        

    
        
a=graph()
a.addedge(1,2)
a.addedge(1,3)
a.addedge(1,4)
a.addedge(2,5)
a.addedge(4,6)
a.addedge(4,5)

a.dfs()
