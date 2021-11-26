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

#function for BFS
def bfs(visited, graph, node): 
    visited.append(node)
    queue.append(node)

# Creating loop to visit each node
    while(len(queue) != 0):          
        m = queue.pop(0) 
        print (m, end = " ") 

        for neighbour in graph[m]:
            if(neighbour not in visited):
                visited.append(neighbour)
                queue.append(neighbour)

bfs(visited, graph, '5')   