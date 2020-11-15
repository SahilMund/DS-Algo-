def validators(s):
  # creating an array of functions
  funcs = [str.isalnum, str.isalpha, str.isdigit, str.islower, str.isupper]
  # calling for each function
  for func in funcs:
    # calling for each char in string
    # any will return true if any value is true in the iterable
    res = any(func(c) for c in s)
    print(res)

def main():
  # str = raw_input()
  str = "qA2"
  validators(str)

if __name__ == '__main__':
  main()