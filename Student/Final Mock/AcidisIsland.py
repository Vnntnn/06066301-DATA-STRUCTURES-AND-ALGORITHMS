"""Find 4x4 island : (1) -> 1 island""" 


def count_square_islands(rows: int, cols: int, grid: list) -> int:
    """Find the number of square-shaped islands in the grid."""
    square_island_count = 0

    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == "1":
                size = get_square_size(i, j, grid, rows, cols)
                if size > 0:  
                    square_island_count += 1
                    mark_island_as_visited(i, j, size, grid)

    return square_island_count


def get_square_size(start_row, start_col, grid, max_rows, max_cols):
    """Determine the size of the square island, or return 0 if it's not a square."""
    size = 0

    while (
        start_row + size < max_rows and start_col + size < max_cols and
        all(grid[start_row + k][start_col + size] == "1" for k in range(size + 1)) and
        all(grid[start_row + size][start_col + k] == "1" for k in range(size + 1))
    ):
        size += 1

    if is_perfect_square(start_row, start_col, size, grid):
        return size
    return 0


def is_perfect_square(start_row, start_col, size, grid):
    """Check if the selected area forms a perfect square filled with '1'."""
    for i in range(start_row, start_row + size):
        for j in range(start_col, start_col + size):
            if grid[i][j] != "1":
                return False
    return True


def mark_island_as_visited(start_row, start_col, size, grid):
    """Replace the square island with '0' to mark it as visited."""
    for i in range(start_row, start_row + size):
        for j in range(start_col, start_col + size):
            grid[i][j] = "0"


def main():
    """Read input and execute the island counting function."""
    rows, cols = map(int, input().split())
    grid = [input().split() for _ in range(rows)]
    
    result = count_square_islands(rows, cols, grid)
    print(result)


main()
