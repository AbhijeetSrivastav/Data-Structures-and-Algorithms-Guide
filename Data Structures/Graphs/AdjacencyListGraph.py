"Graph Implementation using Adjacency List for Unweighted and Wegihted Graphs (Using Dictionary and Lists)"



"Directed - Weighted and Unweighted Graph"
class DirectedGraph:
    def __init__(self, NumVertices:int, weighted:bool) -> object:
        self.vertices = {}
        self.weighted = weighted
        
        # initializes a dictionary with vertices as key and adjacent vertices list as values
        for vertex in range(1, NumVertices + 1):
            self.vertices[vertex] = []


    def AddEdges(self, vertex_1, vertex_2, weight=0):
        if vertex_1 and vertex_2 in self.vertices:
            # if vertex are valid
            if self.weighted is True:
                # if weighted graph
                # adjacent vertices list contains tuple of adjacent vertex and wegight of that edge
                self.vertices[vertex_1].append((vertex_2, weight))
            
            if self.weighted is False:
                # if unweighted edge
                # adds vertex to the adjacent vertex list of a specific vertex
                self.vertices[vertex_1].append(vertex_2)
        else:
            raise Exception('Invalid Vertex!')
        
    def DeleteEdge(self, vertex_1, vertex_2):
        if vertex_1 and vertex_2 in self.vertices:
            # if vertex is valid
            if self.weighted is True:
                # if weighted graph
                try:
                    pairPosition = 0
                    for (vertex, weight) in self.vertices[vertex_1]:
                        if vertex == vertex_2:
                            self.vertices[vertex_1].pop(pairPosition) 
                        pairPosition += 1
                except ValueError:
                    raise Exception('No Such Edge Present!')       

            if self.weighted is False:
                # if unweighted graph
                try:
                    self.vertices[vertex_1].remove(vertex_2)
                except ValueError:
                    raise Exception('No Such Edge Present!')
        else:
            raise Exception('Invalid Vertex!')
    
    def isAdjacent(self, vertex_1, vertex_2):
        if vertex_1 and vertex_2 in self.vertices:
            # if vertex is valid
            if self.weighted is True:
                # if weighted graph
                for (vertex, weight) in self.vertices[vertex_1]:
                    if vertex == vertex_2:
                        print('Adjacent')
                        break
                    else:                
                        print('Not Adjacent')
                        break
                    
            if self.weighted is False:
                # if unweigheted graph
                if vertex_2 in self.vertices[vertex_1]:
                    print('Adjacent')
                else:
                    print('Not Adjacent')
        else:
            raise Exception('Invalid Vertex!')

    def visualizeGraph(self):
        return self.vertices

"Undirected - Weighted and Unweighted Graph"
class UnDirectedGraph:
    def __init__(self, NumVertices:int, weighted:bool) -> object:
        self.vertices = {}
        self.weighted = weighted
        
        # initializes a dictionary with vertices as key and adjacent vertices list as values
        for vertex in range(1, NumVertices + 1):
            self.vertices[vertex] = []


    def AddEdges(self, vertex_1, vertex_2, weight=0):
        if vertex_1 and vertex_2 in self.vertices:
            # if vertex are valid
            if self.weighted is True:
                # if weighted graph
                # adjacent vertices list contains tuple of adjacent vertex and wegight of that edge
                self.vertices[vertex_1].append((vertex_2, weight))
                self.vertices[vertex_2].append((vertex_1, weight))
            
            if self.weighted is False:
                # if unweighted edge
                # adds vertex to the adjacent vertex list of a specific vertex
                self.vertices[vertex_1].append(vertex_2)
                self.vertices[vertex_2].append(vertex_1)
        else:
            raise Exception('Invalid Vertex!')
        
    def DeleteEdge(self, vertex_1, vertex_2):
        if vertex_1 and vertex_2 in self.vertices:
            # if vertex is valid
            if self.weighted is True:
                # if weighted graph
                try:
                    pairPosition = 0
                    for (vertex, weight) in self.vertices[vertex_1]:
                        if vertex == vertex_2:
                            self.vertices[vertex_1].pop(pairPosition)
                        pairPosition += 1
                    
                    pairPosition = 0
                    for (vertex, weight) in self.vertices[vertex_2]:
                        if vertex == vertex_1:
                            self.vertices[vertex_2].pop(pairPosition)
                        pairPosition += 1

                except ValueError:
                    raise Exception('No Such Edge Present!')
                    
            if self.weighted is False:
                # if unweighted graph
                try:
                    self.vertices[vertex_1].remove(vertex_2)
                    self.vertices[vertex_2].remove(vertex_1)
                except ValueError:
                    raise Exception('No Such Edge Present!')
        else:
            raise Exception('Invalid Vertex!')
    
    def isAdjacent(self, vertex_1, vertex_2):
        if vertex_1 and vertex_2 in self.vertices:
            # if vertex is valid
            if self.weighted is True:
                # if weighted graph
                for (vertex, weight) in self.vertices[vertex_1]:
                    if vertex == vertex_2:
                        print('Adjacent')
                        break
                    else:                
                        print('Not Adjacent')
                        break
                    
            if self.weighted is False:
                # if unweigheted graph
                if vertex_2 in self.vertices[vertex_1]:
                    print('Adjacent')
                else:
                    print('Not Adjacent')
        else:
            raise Exception('Invalid Vertex!')

    def visualizeGraph(self):
        return self.vertices

