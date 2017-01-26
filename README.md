# AStar-Python

This is a super simple implementation of the AStar Search algorithm in Python.  It generates a maze and tries to solve it.
The maze is not guaranteed to be solvable, but if the algorithm finds a path it is guaranteed to be a shortest path between the Start and End spaces.

The grid is setup with all horizontal and vertical spaces having a distance of 1 unit apart, but the algorithm calculates the distance between two spaces so that diagonal moves are more costly.

This is a key to the display when the algorithm is finished:

* `'█'` = Wall in the maze
* `'0'` = Space included in a shortest path
* `'+'` = Space included in the OpenSet - path found before this one was evaluated though
* `'-'` = Space included in the ClosedSet - evaluated and not included in any shortest path
* `' '` = Space not evaluated

Two walls that meet at a corner, like a wall at (2,2) and a wall at (3,3) are considered connected so that the path cannot squeeze between these barriers.  For example: 
```
0██
█0
```
is an illegal diagonal move, but if the walls do not meet at the corner it would be allowed:
```
0 █
█0
```

In the future, these would be good values to have the user pass in as parameters when running the program:
* Wall density
* Heuristic (Manhattan vs. Euclidean)
* Are Diagonal moves allowed?
* Start space
* End space

Here is an example output of the algorithm:
```
0+█     █ █   █  ███   █  █ █
█0+█+               █  █   █
 █00+█ ██  ██ ████  █  █ █   █
  ██0██   █     ███  █ █ ██  █
   +0-█+██    █  █  █     █ █
   █0---██ ███   ███ ███    █
   +0███ █  █       █  █ █
   ++0+███ █    █ █ ██     █
    ++0++  █      █        ███
    █+█0+█     █     █ ██
██    ++0++  ██    █  █      █
█ ██   ++0█+  ██  █      ███
    █  █++0+██    ██  █    █
         ++0+█  ██       █
  █ ██    ++0++████ █   █    █
 █ ██   █  █+0█    █  █      █
  █   █   █ ++0█+        ███
 █ █  ██     ++0++███  █    █
            █ +█0000++ █    ██
    █   █  █   █---█0++█ █ █ █
█  █      █  █ ██-██+0+█  █ █
  █    ██     █ +--█++0████ █
   ██  █ ██ █ █ ███ ██0-█
 █  █ █  █   ██ ██   +0█   ███
        ███     █  █ +0█++██ █
  █  █     █ █   ██  ++0-█  █
█████    █ █ █ █      █0-██  █
 █     █ █     █   ██ +0██ █ █
█     █       ██      ++0█++++
   █    █  █ █     █   ++00000
Found a path that is 38 nodes long!
```
