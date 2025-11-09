# Graph DS Theory 8/11/25

# <---------- graph BFS Traversal (connected componenets) ------------------------> 

'''
for this graph -- BFS traversal will be 0 1 2 3 4 5 6 
   1 ---  3
 /        |  \\
0         |   5 -- 6
 \        |  /
  2 ----  4 
'''

'''

from collections import deque 

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


def bfs(graph, v):
    q, visited = deque(), [False]*v

    q.append(0)
    visited[0] = True

    while q:
        curr = q.popleft()
        print(curr, end=" ")

        for edge in graph[curr]:
            if not visited[edge.dest]:
                visited[edge.dest] = True
                q.append(edge.dest)


# <-------------------------- Main fn. ---------------------------------------------->

if __name__ == "__main__":			
    v = 7      
    graph = [[] for _ in range(v)]    

    create_graph(graph)     

    bfs(graph, v)

# <----------------------------------------------------------------------->

'''


# <---------- graph BFS Traversal (disconnected componenets) this can also be used in connected comp. too ------------------------> 

'''
for this graph -- BFS traversal will be 0 1 2 3 4
   0 -- 1 -- 2
   3 --  4 
'''

from collections import deque 

class Edge:         
    def __init__(self, src, dest):
        self.src = src
        self.dest = dest

def create_graph(graph):
    graph[0].append(Edge(0,1))

    graph[1].append(Edge(1,2))
    graph[1].append(Edge(1,0))

    graph[2].append(Edge(1,2))

    graph[3].append(Edge(3,4))

    graph[4].append(Edge(4,3))


def bfs(graph, visited, start):
    q = deque()

    q.append(start)
    visited[start] = True

    while q:
        curr = q.popleft()
        print(curr, end=" ")

        for edge in graph[curr]:
            if not visited[edge.dest]:
                visited[edge.dest] = True
                q.append(edge.dest)


# <-------------------------- Main fn. ---------------------------------------------->

if __name__ == "__main__":			
    v = 5     
    graph = [[] for _ in range(v)]    

    create_graph(graph)     

    visited = [False]*v     # for disconnected comp. will create arr in main and for each vertex false will call bfs, with vis arr and start as i. 
    
    for i in range(v):                  # TC will be (V1​+E1​)+(V2​+E2​)+(V3​+E3​)=V+E (visiting each vertex and edge only once) and not no. of disconnected comp. * (V+E)
        if not visited[i]:
            bfs(graph, visited, i)

