graph = {'a': {'b': 10, 'c': 3}, 'b': {'c': 1, 'd': 2}, 'c': {'b': 4, 'd': 8, 'e': 2}, 'd': {'e': 7}, 'e': {'d': 9}}


def dijkstra(graph, start, goal):
    shortest_distance = {}
    predecessor = {}
    unseenNodes = graph
    infinity = 9999999
    path = []
    for node in unseenNodes:
        shortest_distance[node] = infinity
    shortest_distance[start] = 0
    var = 0
    #unseen node = {'a': {'b': 10, 'c': 3}, 'b': {'c': 1, 'd': 2}, 'c': {'b': 4, 'd': 8, 'e': 2}, 'd': {'e': 7}, 'e': {'d': 9}}
    #{a:0;b=10;c=3;d=9999;e=99999;}
    while unseenNodes:

        minNode = None
        i=0
        for node in unseenNodes:

            i+=1
            if minNode is None:
                minNode = node

            elif shortest_distance[node] < shortest_distance[minNode]:
                minNode = node
            # print(node)
            # print(i)
        for childNode, weight in graph[minNode].items():

            if weight + shortest_distance[minNode] < shortest_distance[childNode]:
                shortest_distance[childNode] = weight + shortest_distance[minNode]
                predecessor[childNode] = minNode
        unseenNodes.pop(minNode)
    print(shortest_distance)


dijkstra(graph,'a','b')