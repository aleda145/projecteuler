# dijkstra implemenation
# from http://www.gilles-bertrand.com/2014/03/dijkstra-algorithm-python-example-source-code-shortest-path.html


def dijkstra(graph, src, dest, visited=[], distances={}, predecessors={}):
    """ calculates a shortest path tree routed in src
    """
    # a few sanity checks
    if src not in graph:
        raise TypeError('The root of the shortest path tree cannot be found')
    if dest not in graph:
        raise TypeError('The target of the shortest path cannot be found')
        # ending condition
    if src == dest:
        # We build the shortest path and display it
        path = []
        pred = dest
        while pred != None:
            path.append(pred)
            pred = predecessors.get(pred, None)
        print('shortest path: ' + str(path) + " cost=" + str(distances[dest]))
    else:
        # if it is the initial  run, initializes the cost
        if not visited:
            distances[src] = 0
        # visit the neighbors
        for neighbor in graph[src]:
            if neighbor not in visited:
                new_distance = distances[src] + graph[src][neighbor]
                if new_distance < distances.get(neighbor, float('inf')):
                    distances[neighbor] = new_distance
                    predecessors[neighbor] = src
        # mark as visited
        visited.append(src)
        # now that all neighbors have been visited: recurse                         
        # select the non visited node with lowest distance 'x'
        # run Dijskstra with src='x'
        unvisited = {}
        for k in graph:
            if k not in visited:
                unvisited[k] = distances.get(k, float('inf'))
        x = min(unvisited, key=unvisited.get)
        dijkstra(graph, x, dest, visited, distances, predecessors)


# the example graph from the problem, all numbers have been 10-x. that way dijkstra kan solve it
small_graph = {'s': {'3a': 7},
         '3a': {'7b': 3, '4c': 6},
         '7b': {'2d': 8, '4e': 6},
         '4c': {'4e': 6, '6f': 4},
         '2d': {'8g': 2, '5h': 5},
         '4e': {'5h': 5, '9i': 1},
         '6f': {'9i': 1, '3j': 7},
         '8g': {'t': 0},
         '5h': {'t': 0},
         '9i': {'t': 0},
         '3j': {'t': 0},
         't': {'t': 0},

         }
dijkstra(small_graph, 's', 't')

# the challenging thing will be to make the graph structure, after that dijkstra kan solve it easily


# putting all the rows in corresponding arrays, this will not work for a big dataset!

row1 = [75]
row2 = [95, 64]
row3 = [17, 47, 82]
row4 = [18, 35, 87, 10]
row5 = [20, 4, 82, 47, 65]
row6 = [19, 1, 23, 75, 3, 34]
row7 = [88, 2, 77, 73, 7, 63, 67]
row8 = [99, 65, 4, 28, 6, 16, 70, 92]
row9 = [41, 41, 26, 56, 83, 40, 80, 70, 33]
row10 = [41, 48, 72, 33, 47, 32, 37, 16, 94, 29]
row11 = [53, 71, 44, 65, 25, 43, 91, 52, 97, 51, 14]
row12 = [70, 11, 33, 28, 77, 73, 17, 78, 39, 68, 17, 57]
row13 = [91, 71, 52, 38, 17, 14, 91, 43, 58, 50, 27, 29, 48]
row14 = [63, 66, 4, 68, 89, 53, 67, 30, 73, 16, 69, 87, 40, 31]
row15 = [4, 62, 98, 27, 23, 9, 70, 98, 73, 93, 38, 53, 60, 4, 23]
for i in range(1,15):
    for j in range(1, i):
        print(j)
