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
#Initialize a stack
stack = []     

#function for DFS
def dfs(visited, graph, node): 
    visited.append(node)
    stack.append(node)

# Creating loop to visit each node
    while(len(stack) != 0):          
        m = stack.pop() 
        print (m, end = " ") 

        for neighbour in graph[m]:
            if(neighbour not in visited):
                visited.append(neighbour)
                stack.append(neighbour)

dfs(visited, graph, '5')   