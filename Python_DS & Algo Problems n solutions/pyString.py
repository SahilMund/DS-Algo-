# You are given a string . Your task is to swap cases. In other words, convert all lowercase letters to uppercase
# letters and vice versa.
# For Example:
# Www.HackerRank.com → wWW.hACKERrANK.COM
# Pythonist 2 → pYTHONIST 2

def main():
  str = raw_input()
  ascii_vals = map(ord, str)
  swapped = [(c + 32 if c > 64 and c < 91 else (c - 32 if c > 96 and c < 123 else c))  for c in ascii_vals]
  swapped_case = map(chr, swapped)
  print(''.join(swapped_case))

if __name__ == '__main__':
  main()