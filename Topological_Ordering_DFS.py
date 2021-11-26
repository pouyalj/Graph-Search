# This will use DFS

graph = {
  '5' : ['3','7'],
  '3' : ['2', '4'],
  '7' : ['8'],
  '2' : [],
  '4' : ['8'],
  '8' : []
}






visited = []
current_label = len(graph)
order_dict = {}


# function for DFS (Recursive)
def dfs(visited, graph, node): 
    global order_dict
    global current_label
    visited.append(node)

    # Creating loop to visit each node
    for neighbour in graph[node]:
        if(neighbour not in visited):
            dfs(visited, graph, neighbour)
    # label order of the vertecies by closer to sink higher number (sink has highest number = len(graph))
    order_dict[node] = current_label
    current_label -= 1

def topological_ordering(graph, visited):
    # look at each vertex if not visited run dfs
    for vertex in graph:
        if(vertex not in visited):
            dfs(visited, graph, vertex) 

topological_ordering(graph,visited)
# sort by the value orders
order_list = sorted(order_dict.items(), key=lambda x:x[1])
sorted_dict = dict(order_list)
# print in the keys of the sorted dict
print(sorted_dict.keys())