# This will not use DFS

graph = {
  '5' : ['3','7'],
  '3' : ['2', '4'],
  '7' : ['8'],
  '2' : [],
  '4' : ['8'],
  '8' : []
}

order_dict = {}


def topological_ordering(graph, order_dict):
    # Base recursion case
    if(len(graph) >= 1):
        # Find a sink vertex and set it to be order_dict[sink] = n
        for key in graph:
            if(graph[key] == []):
                order_dict[str(len(graph))] = key
                for second_key in graph:
                    if(key in graph[second_key]):
                        i = graph[second_key].index(key)
                        graph[second_key].pop(i)
                graph.pop(key)
                break

        # Remove sink vertex from graph and recurse
        topological_ordering(graph, order_dict)

topological_ordering(graph, order_dict)
for i in range(len(order_dict)):
    print(order_dict[str(i+1)])
