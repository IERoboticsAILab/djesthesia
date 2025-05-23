# Python program for A* Search Algorithm
import math
import heapq
import numpy as np
import time

# Define the Cell class
class Cell:
    def __init__(self):
      # Parent cell's row index
        self.parent_i = 0
    # Parent cell's column index
        self.parent_j = 0
    # Total cost of the cell (g + h)
        self.f = float('inf')
    # Cost from start to this cell
        self.g = float('inf')
    # Heuristic cost from this cell to destination
        self.h = 0

class astar():
    
    daemon_path = None
    
    def __init__(self, grid):
        # Define the grid
        self.grid = grid

        # Define the size of the grid
        self.ROW = grid.shape[0]
        self.COL = grid.shape[1]

        self.daemon_destination = [0,0]
        self.daemon_origin = [0,0]

    # Check if a cell is valid (within the grid)
    def is_valid(self, row, col):
        return (row >= 0) and (row < self.ROW) and (col >= 0) and (col < self.COL)

    # Check if a cell is unblocked
    def is_unblocked(self, grid, row, col):
        return grid[row][col] == 1

    # Check if a cell is the destination
    def is_destination(self, row, col, dest):
        return row == dest[0] and col == dest[1]

    # Calculate the heuristic value of a cell (Euclidean distance to destination)
    def calculate_h_value(self, row, col, dest):
        return ((row - dest[0]) ** 2 + (col - dest[1]) ** 2) ** 0.5

    # Trace the path from source to destination
    def trace_path(self, cell_details, dest):
        path = []
        row = dest[0]
        col = dest[1]

        # Trace the path from destination to source using parent cells
        while not (cell_details[row][col].parent_i == row and cell_details[row][col].parent_j == col):
            path.append((row, col))
            temp_row = cell_details[row][col].parent_i
            temp_col = cell_details[row][col].parent_j
            row = temp_row
            col = temp_col

        # Add the source cell to the path
        path.append((row, col))
        # Reverse the path to get the path from source to destination
        path.reverse()
        # Return path
        return path

    # Implement the A* search algorithm
    def search(self, src, dest):
        # Check if the source and destination are valid
        if not self.is_valid(src[0], src[1]) or not self.is_valid(dest[0], dest[1]):
            print("Source or destination is invalid")
            return

        # Check if the source and destination are unblocked
        if not self.is_unblocked(self.grid, src[0], src[1]) or not self.is_unblocked(self.grid, dest[0], dest[1]):
            print("Source or the destination is blocked")
            return

        # Check if we are already at the destination
        if self.is_destination(src[0], src[1], dest):
            print("We are already at the destination")
            return

        # Initialize the closed list (visited cells)
        closed_list = [[False for _ in range(self.COL)] for _ in range(self.ROW)]
        # Initialize the details of each cell
        cell_details = [[Cell() for _ in range(self.COL)] for _ in range(self.ROW)]

        # Initialize the start cell details
        i = src[0]
        j = src[1]
        cell_details[i][j].f = 0
        cell_details[i][j].g = 0
        cell_details[i][j].h = 0
        cell_details[i][j].parent_i = i
        cell_details[i][j].parent_j = j

        # Initialize the open list (cells to be visited) with the start cell
        open_list = []
        heapq.heappush(open_list, (0.0, i, j))

        # Initialize the flag for whether destination is found
        found_dest = False

        # Main loop of A* search algorithm
        while len(open_list) > 0:
            # Pop the cell with the smallest f value from the open list
            p = heapq.heappop(open_list)

            # Mark the cell as visited
            i = p[1]
            j = p[2]
            closed_list[i][j] = True

            # For each direction, check the successors
            directions = [(0, 1), (0, -1), (1, 0), (-1, 0),
                        (1, 1), (1, -1), (-1, 1), (-1, -1)]
            
            for dir in directions:
                new_i = i + dir[0]
                new_j = j + dir[1]

                # If the successor is valid, unblocked, and not visited
                if self.is_valid(new_i, new_j) and self.is_unblocked(self.grid, new_i, new_j) and not closed_list[new_i][new_j]:
                    # If the successor is the destination
                    if self.is_destination(new_i, new_j, dest):
                        # Set the parent of the destination cell
                        cell_details[new_i][new_j].parent_i = i
                        cell_details[new_i][new_j].parent_j = j
                        # print("The destination cell is found")
                        # Trace and print the path from source to destination
                        found_dest = True
                        return self.trace_path(cell_details, dest)
                    else:
                        # Calculate the new f, g, and h values
                        g_new = cell_details[i][j].g + 1.0
                        h_new = self.calculate_h_value(new_i, new_j, dest)
                        f_new = g_new + h_new

                        # If the cell is not in the open list or the new f value is smaller
                        if cell_details[new_i][new_j].f == float('inf') or cell_details[new_i][new_j].f > f_new:
                            # Add the cell to the open list
                            heapq.heappush(open_list, (f_new, new_i, new_j))
                            # Update the cell details
                            cell_details[new_i][new_j].f = f_new
                            cell_details[new_i][new_j].g = g_new
                            cell_details[new_i][new_j].h = h_new
                            cell_details[new_i][new_j].parent_i = i
                            cell_details[new_i][new_j].parent_j = j

        # If the destination is not found after visiting all cells
        if not found_dest:
            print("Failed to find the destination cell")
    
    def set_daemon_destination(self, destination):
        self.daemon_destination = destination

    def set_daemon_origin(self, origin):
        self.daemon_origin = origin    

    def get_daemon_destination(self):
        return self.daemon_destination

    def get_daemon_origin(self):
        return self.daemon_origin    

    def daemon_search(self):
        while True:
            destination = self.get_daemon_destination()
            origin = self.get_daemon_origin()
            astar.daemon_path = self.search(origin, destination)
            time.sleep(0.1)