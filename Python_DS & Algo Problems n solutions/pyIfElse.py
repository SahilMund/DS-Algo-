# Task
# Given an integer, , perform the following conditional actions:
# If  is odd, print Weird
# If  is even and in the inclusive range of  to , print Not Weird
# If  is even and in the inclusive range of  to , print Weird
# If  is even and greater than , print Not Weird
# Input Format
# A single line containing a positive integer, .
# Constraints
# Output Format
# Print Weird if the number is weird; otherwise, print Not Weird.
# Sample Input 0
# 3
# Sample Output 0
# Weird
# Sample Input 1
# 24
# Sample Output 1
# Not Weird
# Explanation
# Sample Case 0:
#  is odd and odd numbers are weird, so we print Weird.
# Sample Case 1:
#  and  is even, so it isn't weird. Thus, we print Not Weird.


def pyIfElse(n):
  if(n & 1 == 1):
    return 'Weird'
  else:
    if(n >1 and n < 6):
      return 'Not Weird'
    elif(n>5 and n < 21):
      return 'Weird'
    else:
      return 'Not Weird'

def main():
  n = input('')
  res = pyIfElse(n)
  print(res)

if __name__ == '__main__':
  main()