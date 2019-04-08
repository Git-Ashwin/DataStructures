from collections import defaultdict
import sys
class graph:
    def __init__(self):
        self.graph=defaultdict(list)
    def addedge(self,u,v):
        self.graph[u].append(v)
        self.length=len(self.graph)
        self.keys=list(self.graph.keys())
        for i in (self.graph.values()):
          for j in i:
            if j[0] not in self.keys:
                self.keys.append(j[0])
    def mindist(self,dist,visited):
        minm=sys.maxsize
        s=None
        for i in self.keys:
            if dist[i]<minm and visited[i]==False:
                s=i
                minm=dist[i]
        return s
        
    def dijkstra(self,src):
        visited={}
        dist={}
        for i in self.keys:
            visited[i]=False
        for i in self.keys:
            dist[i]=sys.maxsize
        dist[src]=0
        visited[src]=True
        while False in visited.values():
            visited[src]=True
            for i in self.graph[src]:
                if visited[i[0]]==False and dist[i[0]]>(i[1]+dist[src]):
                    dist[i[0]]=(i[1]+dist[src])
            src=self.mindist(dist,visited)
        print(dist)
        
        
a=graph()
a.addedge(1,[2,3])
a.addedge(1,[3,6])
a.addedge(2,[3,4])
a.addedge(2,[1,3])
a.addedge(2,[5,10])
a.addedge(3,[5,20])
a.dijkstra(2)
