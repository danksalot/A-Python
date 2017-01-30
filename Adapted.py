# adapted from http://www.redblobgames.com/pathfinding/a-star/introduction.html

from __future__ import print_function
import heapq
import math

class PriorityQueue:
	def __init__(self):
		self.elements = []
	
	def empty(self):
		return len(self.elements) == 0
	
	def put(self, item, priority):
		heapq.heappush(self.elements, (priority, item))
	
	def get(self):
		return heapq.heappop(self.elements)[1]

class Grid:
	def __init__(self, width, height):
		self.width = width
		self.height = height
		self.walls = []

	def in_bounds(self, id):
		(x, y) = id
		return 0 <= x < self.width and 0 <= y < self.height

	def passable(self, id):
		return id not in self.walls

	def diagonalRule(self, a, b):
		(x1, y1) = a
		(x2, y2) = b
		return self.passable((x1, y2)) or self.passable((x2, y1))

	def neighbors(self, id):
		(x, y) = id
		results = [(x+1, y), (x, y-1), (x-1, y), (x, y+1), (x+1, y+1), (x-1, y-1), (x+1, y-1), (x-1, y+1)]
		if (x + y) % 2 == 0: results.reverse()
		results = filter(self.in_bounds, results)
		results = filter(self.passable, results)
		results = filter(lambda d: self.diagonalRule(id, d), results)
		return results

	def cost(self, a, b):
		(x1, y1) = a
		(x2, y2) = b
		if x1 == x2 or y1 == y2:
			return 1
		else:
			return math.sqrt(2)

def heuristic(a, b):
	(x1, y1) = a
	(x2, y2) = b
	hDiff = abs(x1 - x2)
	vDiff = abs(y1 - y2)
	return min(hDiff, vDiff) * math.sqrt(2) + abs(hDiff - vDiff)

def draw_tile(graph, id, style, width):
	r = " "
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

def reconstruct_path(came_from, start, goal):
	current = goal
	path = [current]
	if goal not in came_from:
		return [start]
	while current != start:
		current = came_from[current]
		path.append(current)
	path.append(start) # optional
	path.reverse() # optional
	return path

def a_star_search(graph, start, goal):
	openSet = PriorityQueue()
	openSet.put(start, 0)
	came_from = {}
	cost_so_far = {}
	came_from[start] = None
	cost_so_far[start] = 0
	
	while not openSet.empty():
		current = openSet.get()
		
		if current == goal:
			break
		
		for next in graph.neighbors(current):
			new_cost = cost_so_far[current] + graph.cost(current, next)
			if next not in cost_so_far or new_cost < cost_so_far[next]:
				cost_so_far[next] = new_cost
				priority = new_cost + heuristic(goal, next)
				openSet.put(next, priority)
				came_from[next] = current
	
	return reconstruct_path(came_from, start=start, goal=goal), cost_so_far.get(goal)

# from implementation import *
import random
import math
from itertools import product

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
grid.walls = random.sample(nodes, numWalls) 

path, cost = a_star_search(grid, start, goal)
draw_grid(grid, width=1, path=path, start=start, goal=goal)
if len(path) == 1: print ("Could not find a path")
else: print ("Found a path that is length:", cost)
