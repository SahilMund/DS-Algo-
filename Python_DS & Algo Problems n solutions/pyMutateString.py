# abracadabra
# 5 k
# Sample Output
# abrackdabra

def mutate_string(s, i, c):
  changed = s[:i] + c + s[i+1:]
  return changed

if __name__ == '__main__':
  s = raw_input()
  i, c = raw_input().split()
  s_new = mutate_string(s, int(i), c)
  print s_new
