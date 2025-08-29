import numpy as np
from collections import deque as q

class drops_per_bucket:
    # given a matrix, calculate the amount of drops in each bucket
    # a bucket is the accumulation of drops per column that reach the bottom
    # drops are created when hitting an obstacle or if the spot below is simply empty
    # a drop splits to the left and right when hitting an obstacle
    # starts at a given position in the matrix
    # 0 = empty, 1 = obstacle, 2 = added drop on empty slot, 3 = .5 drop

    # starts at [0][2] here
    # [0, 0, 0, 0]
    # [0, 0, 1, 0]
    # [0, 1, 0, 0]
    # [0, 0, 0, 0]

    # becomes

    # [0, 0, 2, 0]
    # [0, 2, 1, 2]
    # [2, 1, 2, 2]
    # [2, 0, 2, 2]
    
    # buckets are
    # [2, 0, 2, 3]
    # as the number of drops in each col that made it are 2, 0, 2, 3 respectively

    def count_drops(self, matrix: np.ndarray, starting_row: int, starting_col: int) -> list:

        matrix[starting_row][starting_col] = 2

        result = []
        valid_drops = q()
        valid_drops.append([starting_row, starting_col])
        
        # Starting from the given valid starting position, spread the drops correctly
        while len(valid_drops) > 0:
            current_indices = valid_drops.popleft()
            row = current_indices[0]
            col = current_indices[1]

            # Obstacle found, applying to left and right if empty.
            if current_indices[0] < matrix.shape[0] - 1 and matrix[row + 1][col] == 1:
                self.apply_to_left_and_right(row + 1, col, matrix, valid_drops)
            # No obstacle found, apply to the spot below if empty.
            elif current_indices[0] < matrix.shape[0] - 1 and matrix[row + 1][col] == 0:
                matrix[row + 1][col] = 2
                valid_drops.append([row + 1, col])
        
        # Count drops in each column (bucket).
        num_rows = matrix.shape[0]
        num_cols = matrix.shape[1]
        for col in range(num_cols):
            running_counter = 0
            for row in range(num_rows):
                if matrix[row][col] == 3:
                    running_counter += 0.5
                elif matrix[row][col] == 2:
                    running_counter += 1
                elif matrix[row][col] == 1:
                    running_counter = 0
            result.append(running_counter)

        return result
    
    # Checks left and right spots on the obstacles row to apply if empty.
    def apply_to_left_and_right(self, row: int, col: int, matrix: np.ndarray, valid_drops: q):
        if col > 0 and matrix[row][col - 1] == 0:
            matrix[row][col - 1] = 3
            valid_drops.append([row, col - 1])
        if col < matrix.shape[1] - 1 and matrix[row][col + 1] == 0:
            matrix[row][col + 1] = 3
            valid_drops.append([row, col + 1])

# Simple test code prior to pytest test file for visualization.
def test_count_drops():
    """Test the count_drops function with the provided test case"""
    # Test case matrix
    matrix = np.array([
        [0, 0, 0, 0],
        [0, 0, 1, 0],
        [0, 1, 0, 0],
        [0, 0, 0, 0]
    ])
    
    # Starting position at [0][2]
    starting_row = 0
    starting_col = 2
    
    # Create instance and run test
    drops_calculator = drops_per_bucket()
    result = drops_calculator.count_drops(matrix, starting_row, starting_col)
    
    print("Original matrix:")
    print(np.array([
        [0, 0, 0, 0],
        [0, 0, 1, 0],
        [0, 1, 0, 0],
        [0, 0, 0, 0]
    ]))
    
    print("\nMatrix after drops simulation:")
    print(matrix)
    
    print(f"\nBucket counts: {result}")
    print("Expected bucket counts: [2, 0, 2, 3]")
    
    return result


if __name__ == "__main__":
    test_count_drops()