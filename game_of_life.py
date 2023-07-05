def get_next_cell(grid: list[str], i: int, j: int) -> str:
    count = count_neighbors(grid, i, j)
    match count:
        case 2:
            return grid[i][j]
        case 3:
            return '*'
        case other:
            return '.'


def count_neighbors(grid, i, j):
    count = 0
    for x in range(max(0, i - 1), min(i + 2, len(grid))):
        for y in range(max(0, j - 1), min(j + 2, len(grid[0]))):
            if x == i and y == j:
                continue
            if grid[x][y] == '*':
                count += 1
    return count


def get_next_generation(input_grid: str) -> str:
    lines = input_grid.splitlines()
    # first_line = lines[0].split()
    # n = int(first_line[0])
    # m = int(first_line[1])
    first_line = lines[0]
    output_grid = [first_line]
    grid = lines[1:]
    for i, line in enumerate(grid):
        output_line = ""
        for j, cell in enumerate(line):
            new_cell = get_next_cell(grid, i, j)
            output_line += new_cell

        output_grid.append(output_line)
    return "\n".join(output_grid)
