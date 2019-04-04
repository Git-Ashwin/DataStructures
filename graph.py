from collections import defaultdict
class graph:
    def __init__(self):
        self.graph=defaultdict(list)
    def addedge(self,u,v):
        self.graph[u].append(v)
    def dfs(self):
        visited={}
        for i in self.graph.keys():
            visited[i]=False
        for i in self.graph.keys():
            if not visited[i]:
                 print(i)
            visited[i]=True
            stack=self.graph[i][:]
            while stack:
                s=stack[-1]
                for j in self.graph[s]:
                    if visited[j]==False and j not in stack:
                        visited[j]=True
                        stack.append(j)
                        print(j)
                        break
                else:
                    stack.pop()
    def bfs(self):
        visited={}
        for i in self.graph.keys():
            visited[i]=False
        for i in self.graph.keys():
            if not visited[i]:
                 print(i)
            visited[i]=True
            queue=self.graph[i][:]
            while queue:
                s=queue[0]
                for j in self.graph[s]:
                    if visited[j]==False and j not in queue:
                        visited[j]=True
                        queue.append(j)
                        print(j)
                        break
                else:
                    queue.pop(0)
                
                        

    
        
a=graph()
a.addedge(1,2)
a.addedge(2,1)
a.addedge(4,5)
a.addedge(5,4)
a.addedge(3,1)
a.dfs()
print(a.graph)