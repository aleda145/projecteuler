# dijkstra implementation to solve problem 18 and 67. This is not a very good solution.
# a more sensible solution would have been to sum from the bottom up and then compare values.
# but i implemented dijkstra because it sounded like fun! Worked really well for the first problem
# but it ran into some issues for the second one because of recursion limits, it was also not very fast
# it took about 5 min to get the right answer.

# from http://www.gilles-bertrand.com/2014/03/dijkstra-algorithm-python-example-source-code-shortest-path.html
import sys

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
        return path
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
        return dijkstra(graph, x, dest, visited, distances, predecessors)


# the example graph from the problem, all numbers have been 10-x. that way dijkstra kan solve it
small_graph = {'s': {'3a': 7},
         '3a': {'7b': 3, '4c': 6},
         '7b': {'2d': 8, '4e': 6},
         '4c': {'4e': 6, '6f': 4},
         '2d': {'8g': 2, '5h': 5},
         '4e': {'5h': 5, '9i': 1},
         '6f_': {'9i': 1, '3j': 7},
         '8g': {'t': 0},
         '5h': {'t': 0},
         '9i': {'t': 0},
         '3j': {'t': 0},
         't': {'t': 0},

         }
dijkstra(small_graph, 's', 't')

small_triangle_graph = {'end': {'end': 0}}

# the challenging thing will be to make the graph structure, after that dijkstra kan solve it easily

# problem 18
#file = open("triangle.txt", "r")

# problem 67
# for problem 67 the standard python recursion limit has to be exceeded.
sys.setrecursionlimit(10000)

file = open("bigtriangle.txt", "r")
data = file.readlines()
# print(len(data))
matrix = [[0 for x in range(y+1)] for y in range(len(data))]
# print(matrix)
for y_value, line in enumerate(data):
    number_row = line.split()
    # print(number_row)
    # print(y_value)
    for x_value, number in enumerate(number_row):
       matrix[y_value][x_value] = int(number)

# print(matrix)
# print(small_triangle_graph)
seperator="_"
for y in range(len(data)):
    for x in range(y+1):
        # print("y:", y, "x:", x, "value:", matrix[y][x])
        coord = str(y) +seperator + str(x)
        # print(coord)
        if y == 0:

            small_triangle_graph["s"] = {coord: 10-matrix[y][x]}


        if y < len(data)-1:
            coord_first_next = str(y + 1) + seperator + str(x)
            coord_second_next = str(y + 1) + seperator + str(x + 1)
            small_triangle_graph[coord] = {coord_first_next: 100-matrix[y+1][x], coord_second_next:
                                           100-matrix[y+1][x+1]}
        if y == len(data)-1:
            small_triangle_graph[coord] = {'end': 0}
# print(small_triangle_graph)
# print(small_graph)

# for keys, values in small_triangle_graph.items():
    # print(keys)
    # print(values)
print(small_triangle_graph)
shortest = dijkstra(small_triangle_graph, 's', 'end')
print(shortest)
sum_of_path = 0
for i in shortest:
    try:
        y = int(i.split(seperator)[0])
        x = int(i.split(seperator)[1])
        print("numbers are:", matrix[y][x])
        sum_of_path += matrix[y][x]
    except: TypeError
print("sum of the path is:", sum_of_path)
