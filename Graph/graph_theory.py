# Graph DS Theory 25/10/25

# <---------- 1. Build Graph using Adjacency List for undirected, unweighted graph ------------------------> 

'''

class Edge:         # 2. edge class to store edge info src and dest. for that vertex 
    def __init__(self, src, dest):
        self.src = src
        self.dest = dest

def create_graph(graph):
    graph[0].append(Edge(0,2))      # 4. in py we dont have to create, empty arrlist at every index, empty list is created already at initialisation
    graph[1].append(Edge(1,2))
    graph[1].append(Edge(1,3))
    graph[2].append(Edge(2,0))
    graph[2].append(Edge(2,1))
    graph[2].append(Edge(2,3))
    graph[3].append(Edge(3,1))
    graph[3].append(Edge(3,2))

'''

# <--------------- 7. Build Graph using Adjacency List for undirected, weighted graph ----------------------> 


class Edge:         
    def __init__(self, src, dest, weight):
        self.src = src
        self.dest = dest
        self.weight = weight

def create_graph(graph):        # TC O(E*1)
    graph[0].append(Edge(0,2,2))        # TC O(1)
    graph[1].append(Edge(1,2,10))
    graph[1].append(Edge(1,3,0))
    graph[2].append(Edge(2,0,2))
    graph[2].append(Edge(2,1,10))
    graph[2].append(Edge(2,3,-1))
    graph[3].append(Edge(3,1,0))
    graph[3].append(Edge(3,2,-1))


# <-------------------------- Main fn. ---------------------------------------------->

if __name__ == "__main__":			
    v = 4      
    graph = [[] for _ in range(v)]     # TC O(V), 2. create list of size (v) of lists

    create_graph(graph)     # 3. call create fn and pass list graph

    # 5. for finding and printing neighbours of a vertex

    for i in range(0, len(graph[2])):       # 6. TC is O(no. of neighbours)/ O(Ei), run a loop till vertex/ index 2 and store it in edge which will be of type obj. and will access src and dest.
        edge = graph[2][i]       

        print(f"src: {edge.src} -> dest: {edge.dest} -> weight: {edge.weight}")


'''
TC O(V)+O(E)
SC O(V+E)
'''