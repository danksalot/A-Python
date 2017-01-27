import random
import sys
import os
import math

class Node:
	def __init__(self, x, y):
		self.x = x
		self.y = y
	x = 0
	y = 0
	fScore = 0
	gScore = sys.maxint
	passable = True
	fromNode = None
	def findNeighbors(self):
		neighbors = []
		if self.y > 0 and grid[self.x][self.y - 1].passable == True:
			neighbors.append(grid[self.x][self.y - 1])
		if self.y < size - 1 and grid[self.x][self.y + 1].passable == True:
			neighbors.append(grid[self.x][self.y + 1])
		if self.x > 0 and grid[self.x - 1][self.y].passable == True:
			neighbors.append(grid[self.x - 1][self.y])
		if self.x < size - 1 and grid[self.x + 1][self.y].passable == True:
			neighbors.append(grid[self.x + 1][self.y])
		# Diagonals
		if self.x > 0 and self.y > 0 and grid[self.x - 1][self.y - 1].passable == True \
			and (grid[self.x][self.y - 1].passable == True or grid[self.x - 1][self.y].passable == True):
			neighbors.append(grid[self.x - 1][self.y - 1])
		if self.x < size - 1 and self.y > 0 and grid[self.x + 1][self.y - 1].passable == True \
			and (grid[self.x][self.y - 1].passable == True or grid[self.x + 1][self.y].passable == True):
			neighbors.append(grid[self.x + 1][self.y - 1])
		if self.x > 0 and self.y < size - 1 and grid[self.x - 1][self.y + 1].passable == True \
			and (grid[self.x][self.y + 1].passable == True or grid[self.x - 1][self.y].passable == True):
			neighbors.append(grid[self.x - 1][self.y + 1])
		if self.x < size - 1 and self.y < size - 1 and grid[self.x + 1][self.y + 1].passable == True \
			and (grid[self.x][self.y + 1].passable == True or grid[self.x + 1][self.y].passable == True):
			neighbors.append(grid[self.x + 1][self.y + 1])
		return neighbors
	def explore(self, fromNode):
		if self.gScore > fromNode.gScore + getDistance(self, fromNode):
			grid[self.x][self.y].gScore = fromNode.gScore + getDistance(self, fromNode)
			grid[self.x][self.y].fScore = grid[self.x][self.y].gScore + heuristic(self, end)
			grid[self.x][self.y].fromNode = grid[fromNode.x][fromNode.y]

def getDistance(toNode, fromNode):
	return math.sqrt((abs(toNode.x - fromNode.x) ** 2) + (abs(toNode.y - fromNode.y) ** 2))

def heuristic(current, end):
	hDiff = abs(end.x - current.x)
	vDiff = abs(end.y - current.y)
	# Chebyshev's distance
	return max(hDiff, vDiff)
	# Diagonal then straight
	# return min(hDiff, vDiff) * math.sqrt(2) + abs(hDiff - vDiff)

def getPath(current):
	current = grid[current.x][current.y]
	path = [grid[current.x][current.y]]
	while current.fromNode != None:
		current = grid[current.fromNode.x][current.fromNode.y]
		path.append(current)
	return path

def printPath(current):
	path = getPath(current)
	print '\n'.join(''.join('0' if node in path else unichr(0x2588) if not node.passable else '+' if node in openSet else '-' if node in closedSet else ' ' for node in row) for row in grid)
	return len(path)

# Declare Variables
size = 30
wallRate = 0.3
grid = [[Node(x, y) for y in range(size)] for x in range(size)]
start = grid[0][0]
start.gScore = 0
end = grid[size-1][size-1]
openSet = [start]
closedSet = []

# Add walls to grid
for x in range(size):
	for y in range(size):
		if random.random() < wallRate:
			grid[x][y].passable = False
grid[start.x][start.y].passable = True
grid[end.x][end.y].passable = True

# Loop through
while len(openSet) > 0:
	openSet.sort(key = lambda x: x.fScore, reverse=True)
	current = openSet.pop()
	closedSet.append(current)
	printPath(current)
	if current == end:
		length = printPath(current)
		print "Evaluated", len(closedSet), "nodes and found a path that is", length, "nodes long!"
		exit()
	for neighbor in current.findNeighbors():
		if neighbor not in closedSet:
			neighbor.explore(current)
			if neighbor not in openSet:
				openSet.append(neighbor)

printPath(start)
print "Evaluated", len(closedSet), "nodes and could not find a path"
exit()
