# Detect a cycle in undirected graph 7/12/25


# '''
# for this graph -- cycle is 0 --> 1 --> 4
#    1 ---  2
#  / |      |  
# 0  |      |  
#  \ |      |
#    4      3
#     \
#      \
#       5
# '''

class Edge:         
    def __init__(self, src, dest):
        self.src = src
        self.dest = dest

def create_graph(graph):
    graph[0].append(Edge(0,1))      
    graph[0].append(Edge(0,4))

    graph[1].append(Edge(1,0))
    graph[1].append(Edge(1,2))
    graph[1].append(Edge(1,4))

    graph[2].append(Edge(2,1))
    graph[2].append(Edge(2,3))

    graph[3].append(Edge(3,2))

    graph[4].append(Edge(4,1))
    graph[4].append(Edge(4,0))
    graph[4].append(Edge(4,5))

    graph[5].append(Edge(5,4))


def is_cycle_undirected(graph, visited, curr, par):
    visited[curr] = True

    for edge in graph[curr]:
        # condition 1 vis and not par
        if visited[edge.dest] and edge.dest != par:
            return True
        # condition 2 do nothing 

        # condition 3 not vis
        if not visited[edge.dest]:
            if is_cycle_undirected(graph, visited, edge.dest, curr):
                return True

    return False


# <-------------------------- Main fn. ---------------------------------------------->

if __name__ == "__main__":			
    v = 6     
    graph = [[] for _ in range(v)]    

    create_graph(graph)     

    visited = [False]*v     
    
    print(is_cycle_undirected(graph, visited, 0, -1))

"""

TC - O(V) vis arr + O(V+E) adj. list + (recursion at max fn. called for each node O(V) * work done in each E0+E1+...+Ei = O(E)) O(V+E)

SC - O(V) vis arr + O(V+E) adj. list + O(V) stack space

"""