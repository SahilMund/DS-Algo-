# Given two non-negative integers num1 and num2 represented as string, return the sum of num1 and num2.
# Note:
# The length of both num1 and num2 is < 5100.
# Both num1 and num2 contains only digits 0-9.
# Both num1 and num2 does not contain any leading zero.
# You must not use any built-in BigInteger library or convert the inputs to integer directly.

def addStrings(num1, num2):
  large = num1 if len(num1) >= len(num2) else num2
  small = num2  if large == num1 else num1
  res = ''
  carry = 0
  sum = 0
  for i in range(0, len(small)):
    sum = int(large[-(i + 1)]) + int(small[-(i + 1)])
    sum += carry
    carry = sum / 10
    sum = sum % 10
    res += str(sum)
  for i in range(len(small), len(large)):
    sum = int(large[-(i + 1)])
    sum += carry
    carry = sum / 10
    sum = sum % 10
    res += str(sum)
  res += str(carry)
  res = int(res[::-1])
  print(res)


def main():
  addStrings("999","1")


if __name__ == '__main__':
  main()