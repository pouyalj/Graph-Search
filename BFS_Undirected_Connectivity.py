graph = {
  '1' : ['3','5'],
  '3' : ['1', '5'],
  '5' : ['1', '3', '7', '9'],
  '7' : ['5'],
  '9' : ['5'],
  '2' : ['4'],
  '4' : ['2'],
  '6' : ['8', '10'],
  '8' : ['6', '10'],
  '10' : ['6', '8']
}

# List for visited nodes.
visited = [] 
#Initialize a queue
queue = []     

#function for BFS
def bfs(visited, graph):
    pieaces = 0
    for node in graph:
        if (node not in visited):
            visited.append(node)
            queue.append(node)
            pieaces += 1

        # Creating loop to visit each node
            while(len(queue) != 0):          
                m = queue.pop(0) 
                print (m, end = " ") 

                for neighbour in graph[m]:
                    if(neighbour not in visited):
                        visited.append(neighbour)
                        queue.append(neighbour)
            print(" | ")
    return pieaces

graph_pieaces = bfs(visited, graph)
print('\n' + str(graph_pieaces))