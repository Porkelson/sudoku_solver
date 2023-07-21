import pygame
import copy

# Define some colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (192, 192, 192)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
N = 9

# Define the screen dimensions
SCREEN_WIDTH, SCREEN_HEIGHT = 500, 600

# Define the Sudoku grid dimensions
GRID_SIZE = 9
CELL_SIZE = SCREEN_WIDTH // GRID_SIZE

# Define the initial Sudoku puzzle
# Replace the zeros with your Sudoku puzzle
initial_grid = [
    [0, 0, 0, 2, 6, 0, 7, 0, 1],
    [6, 8, 0, 0, 7, 0, 0, 9, 0],
    [1, 9, 0, 0, 0, 4, 5, 0, 0],
    [8, 2, 0, 1, 0, 0, 0, 4, 0],
    [0, 0, 4, 6, 0, 2, 9, 0, 0],
    [0, 5, 0, 0, 0, 3, 0, 2, 8],
    [0, 0, 9, 3, 0, 0, 0, 7, 4],
    [0, 4, 0, 0, 5, 0, 0, 3, 6],
    [7, 0, 3, 0, 1, 8, 0, 0, 0],
]

# Initialize Pygame
pygame.init()

# Set up the screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Sudoku Solver")


# Function to draw the Sudoku grid
def draw_grid():
    for i in range(GRID_SIZE + 1):
        if i % 3 == 0:
            line_thickness = 4
        else:
            line_thickness = 1

        pygame.draw.line(screen, BLACK, (0, i * CELL_SIZE), (SCREEN_WIDTH, i * CELL_SIZE), line_thickness)
        pygame.draw.line(screen, BLACK, (i * CELL_SIZE, 0), (i * CELL_SIZE, SCREEN_HEIGHT - CELL_SIZE), line_thickness)


# Function to draw the Sudoku numbers
def draw_numbers(grid, user_input):
    font = pygame.font.Font(None, 36)
    for row in range(GRID_SIZE):
        for col in range(GRID_SIZE):
            number = grid[row][col]
            color = BLACK if user_input[row][col] else GRAY
            if number != 0:
                text = font.render(str(number), True, color)
                text_rect = text.get_rect(center=(col * CELL_SIZE + CELL_SIZE / 2, row * CELL_SIZE + CELL_SIZE / 2))
                screen.blit(text, text_rect)


# Function to reset the Sudoku grid to the initial state
def reset_grid():
    return copy.deepcopy(initial_grid)


# Functions to solve the Sudoku grid
def check_col(board, row, col, val):
    x = row
    y = col
    if val == 0:
        return True

    for i in range(9):
        if board[i][y] == val and (i, y) != (x, y):
            # print("check_col x")
            return False
    return True


def check_row(board, row, col, val):
    x = row
    y = col
    if val == 0:
        return True

    for i in range(9):
        if board[x][i] == val and (x, i) != (x, y):
            # print("check_row x")
            return False
    return True


def check_box(board, row, col, val):
    x = row
    y = col
    if val == 0:
        return True

    startRow = x - x % 3
    startCol = y - y % 3

    for i in range(3):
        for j in range(3):
            if board[i + startRow][j + startCol] == val and (i + startRow, j + startCol) != (x, y):
                return False
    return True


def isSafe(board, row, col, num):
    if check_row(board, row, col, num) and check_col(board, row, col, num) and check_box(board, row, col, num):
        return True
    return False


def check_original_board(board):
    for i in range(9):
        for j in range(9):
            if not isSafe(board, i, j, board[i][j]):
                return False
    return True


def solve_board(board, row, col):
    # Implement your Sudoku solver function here (not provided in this example)
    # Make sure the function takes a 2D list representing the grid as input and returns the solved grid.

    # Check if we have reached the 8th
    # row and 9th column (0
    # indexed matrix) , we are
    # returning true to avoid
    # further backtracking
    if row == N - 1 and col == N:
        return True

    # Check if column value  becomes 9 ,
    # we move to next row and
    # column start from 0
    if col == N:
        row += 1
        col = 0

    # Check if the current position of
    # the grid already contains
    # value >0, we iterate for next column
    if board[row][col] > 0:
        return solve_board(board, row, col + 1)
    for num in range(1, N + 1, 1):

        # Check if it is safe to place
        # the num (1-9)  in the
        # given row ,col  ->we
        # move to next column
        if isSafe(board, row, col, num):

            # Assigning the num in
            # the current (row,col)
            # position of the grid
            # and assuming our assigned
            # num in the position
            # is correct
            board[row][col] = num

            # Checking for next possibility with next
            # column
            if solve_board(board, row, col + 1):
                return True

        # Removing the assigned num ,
        # since our assumption
        # was wrong , and we go for
        # next assumption with
        # diff num value
        board[row][col] = 0
    return False

# Function to check if the entered number is valid
def is_valid_input(board, row, col, num):
    if num == 0:
        return True

    return isSafe(board, row, col, num)
# Main loop
def main():
    running = True
    selected_square = None
    sudoku_grid = reset_grid()
    user_input = [[True if num == 0 else False for num in row] for row in sudoku_grid]

    while running:
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False

                if event.key == pygame.K_r:  # Reset the Sudoku grid
                    sudoku_grid = reset_grid()
                    user_input = [[True if num == 0 else False for num in row] for row in sudoku_grid]

                if event.key == pygame.K_d:  # Use the default Sudoku puzzle
                    sudoku_grid = copy.deepcopy(initial_grid)
                    user_input = [[True if num == 0 else False for num in row] for row in sudoku_grid]

                if event.key == pygame.K_s:  # Solve the Sudoku puzzle
                    solve_board(sudoku_grid, 0, 0)
                    # user_input = [[False for _ in range(GRID_SIZE)] for _ in range(GRID_SIZE)]

                if selected_square is not None and user_input[selected_square[0]][selected_square[1]]:
                    if event.key == pygame.K_BACKSPACE:  # Clear the square
                        sudoku_grid[selected_square[0]][selected_square[1]] = 0

            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:  # Left mouse button
                    mouse_x, mouse_y = pygame.mouse.get_pos()
                    clicked_row = mouse_y // CELL_SIZE
                    clicked_col = mouse_x // CELL_SIZE

                    if user_input[clicked_row][clicked_col]:
                        selected_square = (clicked_row, clicked_col)



            if event.type == pygame.KEYDOWN:
                if selected_square is not None and user_input[selected_square[0]][selected_square[1]]:
                    if event.unicode.isnumeric():
                        num = int(event.unicode)
                        if is_valid_input(sudoku_grid, selected_square[0], selected_square[1], num):
                            sudoku_grid[selected_square[0]][selected_square[1]] = num
                        else:
                            # Signal that the entered number is invalid
                            print("Invalid number!")

        screen.fill(WHITE)
        draw_grid()
        draw_numbers(sudoku_grid, user_input)

        # Highlight the selected square
        if selected_square is not None:
            selected_x, selected_y = selected_square
            pygame.draw.rect(screen, BLUE, (selected_y * CELL_SIZE, selected_x * CELL_SIZE, CELL_SIZE, CELL_SIZE), 3)


        pygame.display.update()

    pygame.quit()


if __name__ == "__main__":
    main()
