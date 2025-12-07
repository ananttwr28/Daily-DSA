# Topological Sort 7/12/25


# '''
# Graph structure (DAG):
#
#    
#      5 ---------> 0 <--------- 4
#       \                        \
#        \                        \
#         v                        v
#          2 -------> 3 ----------->1
# #
# Top sort: 5 4 0 2 3 1 
# '''


class Edge:         
    def __init__(self, src, dest):
        self.src = src
        self.dest = dest

def create_graph(graph):
    graph[2].append(Edge(2,3))

    graph[3].append(Edge(3,1))

    graph[4].append(Edge(4,0))
    graph[4].append(Edge(4,1))

    graph[5].append(Edge(5,0))
    graph[5].append(Edge(5,2))


def topological_sort_util(graph, visited, curr, stack):     # utility fn. adding in stack and visiting logic is here
    visited[curr] = True

    for edge in graph[curr]:
        if not visited[edge.dest]:
            topological_sort_util(graph, visited, edge.dest, stack)
    stack.append(curr)


def topological_sort(graph):     # fn. for using for loop and calling util for non visited nodes, instead of writing in main
    v = len(graph)
    visited = [False]*v     
    stack = []    

    for i in range(0, v):       
        if not visited[i]:
            topological_sort_util(graph, visited, i, stack)

    while stack:
        print(stack.pop(), end= " ")


# <-------------------------- Main fn. ---------------------------------------------->

if __name__ == "__main__":			
    v = 6     
    graph = [[] for _ in range(v)]    

    create_graph(graph)     

    topological_sort(graph)     

"""

TC - O(V) vis arr + O(V+E) adj. list + (recursion at max fn. called for each node O(V) * work done in each E0+E1+...+Ei = O(E)) O(V+E) + O(V) for stack pop print

SC - O(V) vis arr + O(V+E) adj. list + O(V) rec. stack space + O(V) for stack arr

"""