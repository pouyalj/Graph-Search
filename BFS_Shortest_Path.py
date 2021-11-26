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
#Initialize a queue
queue = []     
# distance initialization (dict)
dist = {}

#function for BFS
def bfs_shortest_path(visited, graph, start_node, end_node): 
    global dist
    dist[start_node] = 0
    visited.append(start_node)
    queue.append(start_node)
    if (start_node == end_node):
        return dist[end_node]

# Creating loop to visit each node
    while(len(queue) != 0):          
        m = queue.pop(0) 
        print (m, end = " ")

        for neighbour in graph[m]:
            if(neighbour not in visited):
                dist[neighbour] = dist[m] + 1
                visited.append(neighbour)
                queue.append(neighbour)
    return dist[end_node]

my_dist = bfs_shortest_path(visited, graph, '5', '8')
print("\n" + str(my_dist))