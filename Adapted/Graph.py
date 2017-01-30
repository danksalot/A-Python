class Graph:
	def __init__(self):
		self.edges = {}
	
	def neighbors(self, id):
		return self.edges[id]

	def cost(self, a, b):
		if b in self.edges[a]:
			return self.edges[a].get(b)

	def heuristic(self, a, b):
		return 1
