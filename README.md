# AStar-Python

This is a super simple implementation of the AStar Search algorithm in Python.  It generates a maze and tries to solve it.
The maze is not guaranteed to be solvable, but if the algorithm finds a path it is guaranteed to be a shortest path between the Start and End spaces.

This is a key to the display when the algorithm is finished:

* `'|'` = Wall in the maze
* `'0'` = Space included in a shortest path
* `'+'` = Space included in the OpenSet - path found before this one was evaluated though
* `'-'` = Space included in the ClosedSet - evaluated and not included in any shortest path
* `' '` = Space not evaluated

In the future, these would be good values to have the user pass in as parameters when running the program:
* Wall density
* Heuristic (Manhattan vs. Euclidean)
* Are Diagonal moves allowed?
* Start space
* End space
