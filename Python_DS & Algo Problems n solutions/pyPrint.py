# Read an integer .
# Without using any string methods, try to print the following:
# Note that "" represents the values in between.

def printFunction(n):
  oneToN = []
  for i in range(n):
    oneToN.append(str(i+1))
  oneToN =  ''.join(oneToN)
  return oneToN

def main():
  n = int(raw_input(''))
  print(printFunction(n))

if __name__ =='__main__':
  main()