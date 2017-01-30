import heapq
from math import sqrt

class PriorityQueue:
	def __init__(self):
		self.elements = []
	
	def empty(self):
		return len(self.elements) == 0
	
	def put(self, item, priority):
		heapq.heappush(self.elements, (priority, item))
	
	def get(self):
		return heapq.heappop(self.elements)[1]

def heuristic(a, b):
	(x1, y1) = a
	(x2, y2) = b
	hDiff = abs(x1 - x2)
	vDiff = abs(y1 - y2)
	return min(hDiff, vDiff) * sqrt(2) + abs(hDiff - vDiff)

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
	
	return reconstruct_path(came_from, start=start, goal=goal), cost_so_far.get(goal), list(x[1] for x in openSet.elements), cost_so_far.keys()
