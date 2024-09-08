# BFS-4

## Problem1: Minesweeper (https://leetcode.com/problems/minesweeper/)

from typing import List

class Solution:
    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:
        # The recursive function to reveal the board starting from the clicked cell.
        def reveal(i: int, j: int):
            # Count mines around the current cell
            mine_count = 0
            for x in range(max(i - 1, 0), min(i + 2, rows)):  # Limits the range on the board
                for y in range(max(j - 1, 0), min(j + 2, columns)):  # Limits the range on the board
                    if board[x][y] == "M":
                        mine_count += 1
          
            # If there are mines around the cell, update with mine count
            if mine_count > 0:
                board[i][j] = str(mine_count)
            else:
                # Otherwise, set the cell to "B" for blank and reveal surrounding cells
                board[i][j] = "B"
                for x in range(max(i - 1, 0), min(i + 2, rows)):
                    for y in range(max(j - 1, 0), min(j + 2, columns)):
                        if board[x][y] == "E":
                            reveal(x, y)

        # Get the size of the board
        rows, columns = len(board), len(board[0])
      
        # The clicked position
        click_row, click_col = click
      
        # If the clicked cell contains a mine, game over
        if board[click_row][click_col] == "M":
            board[click_row][click_col] = "X"
        else:
            # Start revealing from the clicked cell
            reveal(click_row, click_col)
      
        # Return the updated board
        return board
# TC = (m * n), SC = (m * n)

## Problem 2 Snakes and ladders (https://leetcode.com/problems/snakes-and-ladders/)

from collections import deque

class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        # Helper function to map the board number to board coordinates (i,j)
        def get_square_coordinates(square_number):
            row, col = (square_number - 1) // board_size, (square_number - 1) % board_size
            if row % 2 == 1:
                # On odd rows, the counting is from right to left.
                col = board_size - 1 - col
            # Transform row to start from bottom of board
            return board_size - 1 - row, col

        board_size = len(board)  # n by n board
        queue = deque([1])  # Start from square 1
        visited = {1}  # Keep track of visited squares
        steps = 0  # Counter for number of moves

        while queue:
            # Process all squares at the current depth.
            for _ in range(len(queue)):
                current_square = queue.popleft()

                # Win condition: reached the last square
                if current_square == board_size * board_size:
                    return steps

                # Check all possible next moves by dice roll (1-6)
                for next_square in range(current_square + 1, min(current_square + 7, board_size * board_size + 1)):
                    i, j = get_square_coordinates(next_square)

                    # If there's a ladder or snake, take it.
                    if board[i][j] != -1:
                        next_square = board[i][j]

                    # If next square has not been visited, add it to the queue
                    if next_square not in visited:
                        queue.append(next_square)
                        visited.add(next_square)

            # Increment the number of moves after expanding all possible moves at current depth.
            steps += 1
      
        # If we have exited the loop without reaching the last square, it's not possible to win.
        return -1
# TC = (n^2), SC = (n^2)