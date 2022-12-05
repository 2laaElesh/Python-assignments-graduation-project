import os
from time import sleep

N = 10
# drawing the arrow 
matrix = [
  [" ", " ", " ", " ", " ", "*", " ", " ", " ", " ", " "],
  [" ", " ", " ", " ", "*", "*", "*", " ", " ", " ", " "],
  [" ", " ", " ", "*", "*", "*", "*", "*", " ", " ", " "],
  [" ", " ", "*", "*", "*", "*", "*", "*", "*", " ", " "],
  [" ", "*", "*", "*", "*", "*", "*", "*", "*", "*", " "],
  ["*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*"],
  [" ", " ", " ", " ", " ", "*", " ", " ", " ", " ", " "],
  [" ", " ", " ", " ", " ", "*", " ", " ", " ", " ", " "],
  [" ", " ", " ", " ", " ", "*", " ", " ", " ", " ", " "],
  [" ", " ", " ", " ", " ", "*", " ", " ", " ", " ", " "],
  [" ", " ", " ", " ", " ", "*", " ", " ", " ", " ", " "]
]

def rotate90_clockwise(matrix):
    size = len(matrix[0])
    for row in range(size // 2):
        for col in range(row, size - row - 1):
            temp = matrix[row][col] # 0, 0
            # replace the current point with the most bottom left point
            matrix[row][col]                       = matrix[size - 1 - col][row]
            # replace the most bottom left point with the most bottom right point
            matrix[size - 1 - col][row]            = matrix[size - 1 - row][size - 1 - col]
            # replace the most bottom right point with the most up right
            matrix[size - 1 - row][size - 1 - col] = matrix[col][size - 1 - row]
            # replace the most up right with the current point
            matrix[col][size - 1 - row] = temp

 
 #printing the arrow before rotation
def printMatrix(A):
  for row in matrix:
    print(*row)
  print("\n"*2)


#printing the arrow after rotation
for i in range(16):
  rotate90_clockwise(matrix)
  printMatrix(matrix)

  # Waiting for 2 seconds before clearing the screen
  sleep(2)

  # Clearing the Screen
  os.system('cls')
