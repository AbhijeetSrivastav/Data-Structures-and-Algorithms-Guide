"Graph Implementation using Adjacency Matrix for Unweighted and Weighted Graph"

from pandas import *


"Undirected - Weighted and Unweighted Graph"
class UnDirectedGraph:
    def __init__(self, NumVertices) -> None:
        self.NumVertices = NumVertices
        self.Vertices = []
        self.AdjMatrix = [[-1] * NumVertices for _ in range(NumVertices)]

        
    def AddEdge(self, vertex_1, vertex_2, weight=None):
        # index = vertex - 1 as vertex id start from 1 while index start from 0
        if (1<= vertex_1 <= self.NumVertices) and (1<= vertex_2 <= self.NumVertices):
            # if vertex is valid
            if weight:
                # for weighted graph
                self.AdjMatrix[vertex_1 - 1][vertex_2 - 1] = weight
                self.AdjMatrix[vertex_2 - 1][vertex_1 - 1] = weight
            
            if weight is None:
                self.AdjMatrix[vertex_1 - 1][vertex_2 - 1] = 1
                self.AdjMatrix[vertex_2 - 1][vertex_1 - 1] = 1
        else:
            raise Exception('Invalid Vertex!')
    
    def DeleteEdge(self, vertex_1, vertex_2):
        # if their is no edge then value in the adjacent matrix will be -1 for weighted and unweighted both
        # index = vertex - 1 as vertex id start from 1 while index start from 0
        if (1<= vertex_1 <= self.NumVertices) and (1<= vertex_2 <= self.NumVertices):
            # if vertex is valid
                self.AdjMatrix[vertex_1 - 1][vertex_2 - 1] = -1
                self.AdjMatrix[vertex_2 - 1][vertex_1 - 1] = -1
        else:
            raise Exception('Invalid Vertex!')
    
    def isAdjacent(self, vertex_1, vertex_2):
        # if their is edge between two vertex then they are adjacent
        if (1<= vertex_1 <= self.NumVertices) and (1<= vertex_2 <= self.NumVertices):
            # if vertex is valid
            if (self.AdjMatrix[vertex_1 - 1][vertex_2 - 1] >= 1) and (self.AdjMatrix[vertex_2 - 1][vertex_1 - 1] >=1): 
                 print('Adjacent')
            else:
                print('Not Adjcent')
        else:
            raise Exception('Invalid Vertex!')
    
    def VisualizeGraphMatrix(self):
        print('Index = Vertex + 1')
        return DataFrame(self.AdjMatrix) 




"Directed - Wegihted and Unweighted Graph"
class DirectedGraph:
    def __init__(self, NumVertices) -> None:
        self.NumVertices = NumVertices
        self.Vertices = []
        self.AdjMatrix = [[-1] * NumVertices for _ in range(NumVertices)]

        
    def AddEdge(self, vertex_1, vertex_2, weight=None):
        # index = vertex - 1 as vertex id start from 1 while index start from 0
        if (1<= vertex_1 <= self.NumVertices) and (1<= vertex_2 <= self.NumVertices):
            # if vertex is valid
            if weight:
                # for weighted graph
                self.AdjMatrix[vertex_1 - 1][vertex_2 - 1] = weight
            
            if weight is None:
                self.AdjMatrix[vertex_1 - 1][vertex_2 - 1] = 1
        else:
            raise Exception('Invalid Vertex!')
    
    def DeleteEdge(self, vertex_1, vertex_2):
        # if their is no edge then value in the adjacent matrix will be -1 for weighted and unweighted both
        # index = vertex - 1 as vertex id start from 1 while index start from 0
        if (1<= vertex_1 <= self.NumVertices) and (1<= vertex_2 <= self.NumVertices):
            # if vertex is valid
                self.AdjMatrix[vertex_1 - 1][vertex_2 - 1] = -1
        else:
            raise Exception('Invalid Vertex!')
    
    def isAdjacent(self, vertex_1, vertex_2):
        # if their is edge between two vertex then they are adjacent
        if (1<= vertex_1 <= self.NumVertices) and (1<= vertex_2 <= self.NumVertices):
            # if vertex is valid
            print('Adjcent') if self.AdjMatrix[vertex_1 - 1][vertex_2 - 1] >= 1 else  print('Not Adjcent')
        else:
            raise Exception('Invalid Vertex!')
    
    def VisualizeGraphMatrix(self):
        print('Index = Vertex + 1')
        return DataFrame(self.AdjMatrix) 


