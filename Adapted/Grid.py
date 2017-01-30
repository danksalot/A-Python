from math import sqrt

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
			return 1				# Straight path
		else:
			return sqrt(2)			# Diagonal path
