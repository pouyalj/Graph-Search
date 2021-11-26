# Directed Graph (Doesn't have to be but is for this example)
graph = {
  '5' : ['3','7'],
  '3' : ['2', '4'],
  '7' : ['8'],
  '2' : [],
  '4' : ['8'],
  '8' : []
}

# List for visited nodes.
visited = [] 

#function for DFS (Recursive)
def dfs(visited, graph, node): 
    visited.append(node)
    print (node, end = " ") 

    #Creating loop to visit each node
    for neighbour in graph[node]:
        if(neighbour not in visited):
            dfs(visited, graph, neighbour)

dfs(visited, graph, '5')   