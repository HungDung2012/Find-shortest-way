import heapq

def astar(maze, start, goal):
    rows, cols = len(maze), len(maze[0])

    def h(pos):
        return abs(pos[0]-goal[0]) + abs(pos[1]-goal[1])

    open_set = []
    heapq.heappush(open_set, (h(start), 0, start))
    came_from = {}
    g_score = {start: 0}

    while open_set:
        _, g, current = heapq.heappop(open_set)
        if current == goal:
            path = [current]
            while current in came_from:
                current = came_from[current]
                path.append(current)
            return path[::-1]

        for dr, dc in ((1,0),(-1,0),(0,1),(0,-1)):
            nr, nc = current[0]+dr, current[1]+dc
            if 0 <= nr < rows and 0 <= nc < cols and maze[nr][nc] != '#':
                neigh = (nr, nc)
                tentative_g = g + 1
                if neigh not in g_score or tentative_g < g_score[neigh]:
                    came_from[neigh] = current
                    g_score[neigh] = tentative_g
                    heapq.heappush(open_set, (tentative_g + h(neigh), tentative_g, neigh))
    return None


def solve_and_draw(grid):
    start = goal = None
    for r, row in enumerate(grid):
        for c, ch in enumerate(row):
            if ch == 'S':
                start = (r, c)
            elif ch == 'G':
                goal = (r, c)
    if start is None or goal is None:
        return None, "Maze must contain S and G"

    path = astar(grid, start, goal)
    if path is None:
        return None, "No path found"

    for r, c in path[1:-1]:
        grid[r][c] = '*'
    drawn = '\n'.join(''.join(row) for row in grid)
    return drawn, None
