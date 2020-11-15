# Consider a list (list = []). You can perform the following commands:
# insert i e: Insert integer  at position .
# print: Print the list.
# remove e: Delete the first occurrence of integer .
# append e: Insert integer  at the end of the list.
# sort: Sort the list.
# pop: Pop the last element from the list.
# reverse: Reverse the list.
# Initialize your list and read in the value of  followed by  lines of commands where each command will be of the  types
# listed above. Iterate through each command in order and perform the corresponding operation on your list.
# Input Format
# The first line contains an integer, , denoting the number of commands.
# Each line  of the  subsequent lines contains one of the commands described above.#
# Constraints
# The elements added to the list must be integers.

def pyList(c, commands):
  resList = []
  cmd = []
  for i in range(len(commands)):
    cmd = commands[i].split()
    if(cmd[0] == 'insert'):
      resList.insert(int(cmd[1]),int(cmd[2]))
    elif(cmd[0] == 'print'):
          print(resList)
    elif(cmd[0] == 'remove'):
          resList.remove(int(cmd[1]))
    elif(cmd[0] == 'append'):
          resList.append(int(cmd[1]))
    elif(cmd[0] == 'sort'):
          resList.sort()
    elif(cmd[0] == 'pop'):
          resList.pop()
    elif(cmd[0] == 'reverse'):
      resList.reverse()
  return resList

def main():
  N = int(raw_input(''))
  commands = []
  for i in range(N):
    commands.append(raw_input(''))
  pyList(N, commands)

if __name__ == '__main__':
  main()