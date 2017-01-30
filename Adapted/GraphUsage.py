from Graph import Graph
from AStar import a_star_search

start = ('F')
goal = ('D')

graph = Graph()
graph.edges = {
	'A': {'B': 2, 'D': 2, 'G': 4},
	'B': {'A': 2, 'C': 2, 'F': 3},
	'C': {'B': 2, 'D': 2, 'E': 4},
	'D': {'A': 2, 'C': 2},
	'E': {'C': 4, 'F': 4},
	'F': {'B': 3, 'E': 4},
	'G': {'A': 4}
}

path, cost, openSet, closedSet = a_star_search(graph, start, goal)
print "Found a path with length", cost
print '-'.join(path)
