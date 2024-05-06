class Graph:
    def __init__(self,gdict = None):
        if gdict is None:
            gdict = {}
        self.gdict = gdict
    
    def addEdge(self, vertex, edge):
        self.gdict[vertex].append(edge)
    
    def bfs(self, vertex): #Breadth First Sort -->uses Queue method
        visited = [vertex]
        queue = [vertex]
        while queue:
            deqVertex = queue.pop(0)
            print(deqVertex)
            for adjacentVertex in self.gdict[deqVertex]:
                if adjacentVertex not in visited:
                    visited.append(adjacentVertex)
                    queue.append(adjacentVertex)
    
    def dfs(self,vertex): # Depth first search uses - Stack method
        visited = [vertex]
        stack = [vertex]
        while stack:
            popVertex = stack.pop()
            print(popVertex)
            for adjacentVertex in self.gdict[popVertex]:
                if adjacentVertex not in visited:
                    visited.append(adjacentVertex)
                    stack.append(adjacentVertex)



customDict = { "a" : ["b","c"],
            "b" : ["a", "d", "e"],
            "c" : ["a", "e"],
            "d" : ["b", "e", "f"],
            "e" : ["d", "f"],
            "f" : ["d", "e"]
               }

graph = Graph(customDict)
# graph.addEdge("e","c")
# print(graph.gdict["e"])
# print(graph.gdict)
# graph.bfs("a")
graph.dfs("a")