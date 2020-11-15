# Given a string and an integer k, you need to reverse the first k characters for every 2k characters counting from the
# start of the string. If there are less than k characters left, reverse all of them. If there are less than 2k but
# greater than or equal to k characters, then reverse the first k characters and left the other as original.
# Example:
# Input: s = "abcdefg", k = 2
# Output: "bacdfeg"

def reverseStr(s, k):
  # increase i by k in every step, select a subtring from i to i+k index
  # [::-1] -- this is extended slices, that make the copy of same list in reverse order
  sub_parts = [ s[i : i + k][::-1] + s[ i + k : i + 2 * k] for i in range(0, len(s), 2 * k) ]
  return ''.join(sub_parts)


def main():
  s = "abcdefg"
  k = 2
  print(reverseStr(s, k))


if __name__ == '__main__':
  main()
