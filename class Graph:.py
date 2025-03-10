class Graph:
    def __init__(self,vertices,edges):
        self.vertices = set(vertices)
        self.edges = set(edges)
        self.adjacency_list = {}

        for vertex in vertices:
            self.adjacency_list[vertex] = []

            for edge in edges:
                if vertex in edge:
                    for v in edge:
                        if v != vertex:
                            self.adjacency_list[vertex].append(v)
                            break

g = Graph(
    ["a","b","c"],
    [("a","b"),("b","c"),("a","c")]
    
    
    )

print(g.adjacency_list)

#adjacency_list = {
    #"a": ["b","c"]
    #...
#} 

# adjacency_matrix = [
#     [0,1,1],
#     [1,0,1],
#     [1,1,0]
# ]

# adjacency_matrix = {
#     "a":{
#          "a":0
#          "b":1
#          "c":1
#     }
#     "b":{
#          "a":0
#          "b":1
#          "c":1
#     }
#     "c":{
#         "a":0
#          "b":1
#          "c":1
#     }

# }