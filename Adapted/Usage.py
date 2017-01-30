from __future__ import print_function
from random import sample
from itertools import product
from Grid import Grid
from AStar import a_star_search

def draw_tile(graph, id, style, width):
	r = " "
	if 'closedSet' in style and id in style['closedSet']: r = "-"
	if 'openSet' in style and id in style['openSet']: r = "."
	if 'path' in style and id in style['path']: r = "@"
	if 'start' in style and id == style['start']: r = "A"
	if 'goal' in style and id == style['goal']: r = "Z"	
	if id in graph.walls: r = unichr(0x2588) * width
	return r

def draw_grid(graph, width=2, **style):
	print ("#" * (graph.height * width + 2))
	for y in range(graph.height):
		print ("#", end="")
		for x in range(graph.width):
			print("%%-%ds" % width % draw_tile(graph, (x, y), style, width), end="")
		print("#")
	print ("#" * (graph.height * width + 2))

width = 30
height = 30
wallDensity = 0.3
start = (0, 0)
goal = (width - 1, height - 1)

grid = Grid(width, height)
nodes = list(product(xrange(width), xrange(height)))
nodes.remove(start)
nodes.remove(goal)
numWalls = int(len(nodes) * wallDensity)
grid.walls = sample(nodes, numWalls) 

path, cost, openSet, closedSet = a_star_search(grid, start, goal)
draw_grid(grid, width=1, path=path, openSet=openSet, closedSet=closedSet, start=start, goal=goal)
if len(path) == 1: print ("I explored", len(closedSet), "nodes and could not find a path")
else: print ("I explored", len(closedSet), "nodes and found a path with length:", cost)
