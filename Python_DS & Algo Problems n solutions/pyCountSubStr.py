def count_substring(str, sub):
  count = 0
  for i in range(len(str) - len(sub) + 1):
    if str[i] == sub[0]:
      p = 0
      for j in range(len(sub)):
        if str[i + j] != sub[j]:
          break
        p = j
      if (p == len(sub) - 1):
        count += 1
  return count

def main():
  # str = raw_input()
  # sub = raw_input()
  str = "ABCDCDC"
  sub = "CDC"
  res = count_substring(str, sub)
  print(res)

if __name__ == '__main__':
  main()