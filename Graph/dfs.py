# Graph DS Traversal 9/11

# <---------- graph DFS Traversal (disconnected componenets) this can also be used in connected comp. too ------------------------> 

# '''
# for this graph -- DFS traversal will be 0 1 3 4 2 5 6 
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


def dfs(graph, visited, curr):
    if visited[curr]:
        return

    print(curr, end=" ")
    visited[curr] = True

    for edge in graph[curr]:
        if not visited[edge.dest]:
            dfs(graph, visited, edge.dest)


# <-------------------------- Main fn. ---------------------------------------------->

if __name__ == "__main__":			
    v = 7     
    graph = [[] for _ in range(v)]    

    create_graph(graph)     

    visited = [False]*v     
    
    for i in range(v):                  
        if not visited[i]:
            dfs(graph, visited, i)

