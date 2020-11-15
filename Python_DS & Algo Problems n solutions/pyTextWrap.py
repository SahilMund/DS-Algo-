import textwrap

def wrap(s, w):
  return textwrap.fill(s,w)

def main():
  # s = raw_input()
  # w = int(raw_input())

  s = "ABCDEFGHIJKLIMNOQRSTUVWXYZ"
  w = 4
  print(wrap(s, w))

if __name__ == '__main__':
  main()