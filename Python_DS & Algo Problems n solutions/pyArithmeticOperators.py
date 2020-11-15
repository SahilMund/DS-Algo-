# Task
# Read two integers from STDIN and print three lines where:
#
# The first line contains the sum of the two numbers.
# The second line contains the difference of the two numbers (first - second).
# The third line contains the product of the two numbers.

def arithmeticOperators(a, b):
  res = []
  res.append(a + b)
  res.append(a - b)
  res.append(a * b)
  return res

def main():
  a = int(raw_input(''))
  b = int(raw_input(''))
  res = arithmeticOperators(a, b)
  for i in range(len(res)):
    print(res[i])

if __name__ == '__main__':
  main()