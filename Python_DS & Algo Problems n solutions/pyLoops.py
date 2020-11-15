# Task
# Read an integer . For all non-negative integers , print . See the sample for details.
# Input Format
# The first and only line contains the integer, .
# Constraints
# Output Format
# Print  lines, one corresponding to each .

def pyLoop(n):
  for i in range(n):
    print(i**2)


def main():
  n = int(raw_input(''))
  pyLoop(n)

if __name__ == '__main__':
  main()