# Task
# Read two integers and print two lines. The first line should contain integer division,  // . The second line should
# contain float division,  / .
# You don't need to perform any rounding or formatting operations.
# Input Format
# The first line contains the first integer, . The second line contains the second integer, .

from __future__ import division

def pyDivision(a, b):
  res = []
  res.append(int(a/b))
  res.append(a/b)
  return res

def main():
  a = int(raw_input(''))
  b = int(raw_input(''))
  res = pyDivision(a, b)
  for i in range(len(res)):
    print(res[i])

if __name__ == '__main__':
  main()