# Graph DFS Qs 12/11

# <---------- Print all the paths from src to target ------------------------> 

# '''

# for this graph -- src = 0, tar = 5

# o/p -- 0 1 3 5, 0 1 3 4 5, 0 2 4 5, 0 2 4 3 5

#    1 ---  3
#  /        |  \\
# 0         |   5 -- 6
#  \        |  /
#   2 ----  4 

# '''

class Edge:         
    def __init__(self, src, dest):
        self.src = src
        self.dest = dest

def create_graph(graph):    
    graph[0].append(Edge(0,1))      
    graph[0].append(Edge(0,2))

    graph[1].append(Edge(1,0))
    graph[1].append(Edge(1,3))

    graph[2].append(Edge(2,0))
    graph[2].append(Edge(2,4))

    graph[3].append(Edge(3,1))
    graph[3].append(Edge(3,4))
    graph[3].append(Edge(3,5))

    graph[4].append(Edge(4,3))
    graph[4].append(Edge(4,2))
    graph[4].append(Edge(4,5))

    graph[5].append(Edge(5,3))
    graph[5].append(Edge(5,4))
    graph[5].append(Edge(5,6))

    graph[6].append(Edge(6,5))


def print_all_paths(graph, visited, curr, path, tar):
    if curr == tar:
        print(path)         # TC: O(V) in worst case, O(V * P) across all paths (P = number of simple paths)
        return

    for edge in graph[curr]:        # TC: O(Ei) for this vertex
        if not visited[edge.dest]:
            visited[edge.dest] = True       # TC: O(1)
            path.append(edge.dest)          # TC: O(1)
            print_all_paths(graph, visited, edge.dest, path, tar)
            path.pop()                      # TC: O(1)
            visited[edge.dest] = False      # TC: O(1)

# <-------------------------- Main fn. ---------------------------------------------->

if __name__ == "__main__":			
    v = 7     
    graph = [[] for _ in range(v)]      # TC - O(V), SC O(V+E)

    create_graph(graph)     # TC - O(E)

    visited = [False]*v         # SC O(V)

    src, tar = 0, 5
    visited[src] = True

    print_all_paths(graph, visited, src, [src], tar)        # SC O(V) for path arr at max

'''
TC -- O(V) + O(E) {for adj list, and graph creation} + O(V*P) {P is exponential in V, k^V} + O(E) 
SC -- O(V+E)   {for adj list, and graph creation} + O(V) + O(V) + O(V) {Recursion stack}
'''