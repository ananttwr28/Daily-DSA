# Detect a cycle in directed graph 7/12/25


# '''
# Graph structure (directed):
#
#    
#    1 ----> 0  -----
#            ^       \
#            |        v
#            3 <----- 2
#
# Cycle: 0 → 2 → 3 → 0
# '''


class Edge:         
    def __init__(self, src, dest):
        self.src = src
        self.dest = dest

def create_graph(graph):
    # in directed we don't write for (0,2) and (2,0) just for 0 as dir. goes from 0 to 2
    graph[0].append(Edge(0,2))      # comment and remove this dir. to make it acyclic no cycles

    graph[1].append(Edge(1,0))

    graph[2].append(Edge(2,3))

    graph[3].append(Edge(3,0))


def is_cycle_directed(graph, visited, curr, rec_stack):
    visited[curr] = True
    rec_stack[curr] = True

    for edge in graph[curr]:
        # vis and in rec_stack cycle case return True
        if rec_stack[edge.dest]:
            return True
        # condition 2 do nothing if not in rec_stack and vis = T

        # condition 3 not vis
        elif not visited[edge.dest]:
            if is_cycle_directed(graph, visited, edge.dest, rec_stack):
                return True
    rec_stack[curr] = False
    return False


# <-------------------------- Main fn. ---------------------------------------------->

if __name__ == "__main__":			
    v = 4     
    graph = [[] for _ in range(v)]    

    create_graph(graph)     

    visited = [False]*v     
    rec_stack = [False]*v     
    found = False       # to check if no cycle found

    # as in connected components some components maybe disconnected and won't be checked, similar in directed we won't be possible to check all the nodes so using for loop and for every unvisited will call the check cyclic fn.

    for i in range(0, v):       # TC O(V) in WC if cycle is not found and we have to travel till V nodes
        if not visited[i] and is_cycle_directed(graph, visited, i, rec_stack):
            print("Cycle found")
            found = True
            break       # there can be multiple cycles we are breaking for if first one is found
    
    if not found:       # to check if breaked from break cond. or completion of for loop
        print("Cycle not found")
    

"""

TC - O(V) vis arr + O(V+E) adj. list + (recursion at max fn. called for each node O(V) * work done in each E0+E1+...+Ei = O(E)) O(V+E) + O(V) for rec_stack arr

SC - O(V) vis arr + O(V+E) adj. list + O(V) stack space + O(V) for rec_stack arr

"""