# Let's learn about list comprehensions! You are given three integers  and  representing the dimensions of a cuboid
# along with an integer N. You have to print a list of all possible coordinates given by  (i, j, k)on a 3D grid where
# the sum of   i + j + k is not equal to N. Here, i : 0 - X, j : 0 - Y, k : 0 - Z
#
# Input Format
#
# Four integers  X,Y,Z & N and  each on four separate lines, respectively.
#
# Constraints
#
# Print the list in lexicographic increasing order.
#
# Sample Input
#
# 1
# 1
# 1
# 2
# Sample Output
#
# [[0, 0, 0], [0, 0, 1], [0, 1, 0], [1, 0, 0], [1, 1, 1]]

import time
def main():
  x = int(raw_input())
  y = int(raw_input())
  z = int(raw_input())
  n = int(raw_input())
  start = time.time()
  print [[i,j, k] for i in range(x + 1) for j in range(y + 1) for k in range(z + 1) if( i + j + k != n)]
  end = time.time()
  print(end - start)

if __name__ == '__main__':
  main()