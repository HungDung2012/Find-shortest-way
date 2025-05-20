import astar

def parse_maze(text):
    return [list(line.rstrip('\n')) for line in text.splitlines() if line.strip()]

def main():
    print("=== Maze Bot CLI ===")
    print("Paste the maze. End with an empty line:")
    lines = []
    while True:
        try:
            line = input()
        except EOFError:
            break
        if line == "":
            break
        lines.append(line)
    raw = "\n".join(lines)
    grid = parse_maze(raw)

    solved, err = astar.solve_and_draw(grid)
    if err:
        print("Error:", err)
    else:
        print("\nSolved maze:")
        print(solved)

if __name__ == "__main__":
    main()
