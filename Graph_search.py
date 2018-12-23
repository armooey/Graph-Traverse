from collections import defaultdict
from graphviz import Digraph
import math


#################
# Vertex class
#################
class Vertex:
    color = "white"
    dTime = 0
    fTime = 0
    pi = None
    distance = math.inf

    def __init__(self, tag):
        self.name = tag


################################
# graph class
################################
class graph:
    time = 0

    def __init__(self):
        self.graph = defaultdict(list)

    # following function adds edge to graph
    def connect(self, v1, v2):
        self.graph[v1].append(v2)
        if not self.find(v2):
            self.graph[v2].append(v1)
            self.graph[v2].pop()

    # visualizing BFS
    def bfs_show(self):
        g = Digraph('G', engine='sfdp')
        for u in self.graph:
            g.node(str(u.name), str(u.distance), xlabel= str(u.name))
        for u in self.graph:
            for v in self.graph[u]:
                g.edge(str(u.name), str(v.name))
        g.view()

    # Visualizing DFS
    def dfs_show(self):
        g = Digraph('G', engine='sfdp')
        for u in self.graph:
            label = str(u.dTime)+"/"+str(u.fTime)
            g.node(str(u.name), label, xlabel=str(u.name))
        for u in self.graph:
            for v in self.graph[u]:
                g.edge(str(u.name), str(v.name))
        g.view()

    # BFS Function
    def bfs(self, s):
        for u in self.graph:
            u.color = "white"
            u.distance = math.inf
            u.pi = None
        s.color = "gray"
        s.distance = 0
        s.pi = None
        queue = list()
        queue.append(s)
        while queue:
            u = queue.pop(0)
            for v in self.graph[u]:
                if v.color == "white":
                    v.color = "gray"
                    v.distance = u.distance + 1
                    v.pi = u
                    queue.append(v)
            u.color = "black"
        self.bfs_show()

    def find(self,u):
        for v in self.graph:
            if v.name == u:
                return True
        return False

    def dfs_visit(self, u):
        self.time = self.time + 1
        u.dTime = self.time
        u.color = "gray"
        for v in self.graph[u]:
            if v.color == "white":
                v.pi = u
                self.dfs_visit(v)
        u.color = "black"
        self.time = self.time + 1
        u.fTime = self.time

    def dfs(self):
        self.time = 0
        for u in self.graph:
            u.color = "white"
            u.pi = None
        for u in self.graph:
            if u.color == "white":
                self.dfs_visit(u)
        self.dfs_show()

    def draw(self):
        g = Digraph('G', engine='sfdp')
        for u in self.graph:
            g.node(str(u.name))
        for u in self.graph:
            for v in self.graph[u]:
                g.edge(str(u.name), str(v.name))
        g.view()


##############################
# ########Main################
##############################
g = graph()
v = [Vertex("a"),Vertex("b"),Vertex("c"),Vertex("d"),Vertex("e"),Vertex("f"),Vertex("e"),Vertex("f"),Vertex("g"),Vertex("h"),Vertex("i"),Vertex("j"),Vertex("k"),Vertex("l")]

print("#####################################################"),
print("#############Graph Searching Algorithms##############"),
print("#####################################################"),
print("Use 'add' command to add edge to graph!"),
print("Use 'draw' command to draw graph!"),
print("Use 'bfs' command to run BFS"),
print("Use 'dfs' command to run DFS"),
print("Use 'exit' to terminate the program!"),
cmd = ""
while cmd != "exit":
    cmd = input()
    if cmd == "add":
        a = input("Enter the 1st node: ")
        b = input("Enter the 2nd node: ")
        g.connect(v[ord(a[0])-ord('a')], v[ord(b[0])-ord('a')])
    if cmd == "draw":
        g.draw()
    if cmd == "bfs":
        c = input("Enter The start node: ")
        g.bfs(v[ord(c[0])-ord('a')])
    if cmd == "dfs":
        g.dfs()
