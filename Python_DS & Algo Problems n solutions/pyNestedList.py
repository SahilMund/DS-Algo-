# Given the names and grades for each student in a Physics class of  students, store them in a nested list and print the name(s) of any student(s) having the second lowest grade.
# Note: If there are multiple students with the same grade, order their names alphabetically and print each name on a new line.
# Input Format
# The first line contains an integer, , the number of students.
# The  subsequent lines describe each student over  lines; the first line contains a student's name, and the second line contains their grade.
# Constraints
# There will always be one or more students having the second lowest grade.
# Output Format
# Print the name(s) of any student(s) having the second lowest grade in Physics; if there are multiple students, order their names alphabetically and print each one on a new line.
# Sample Input
# 5
# Harry
# 37.21
# Berry
# 37.21
# Tina
# 37.2
# Akriti
# 41
# Harsh
# 39
# Sample Output
# Berry
# Harry

def main():
  max1 = 0;
  max2 = 0
  dict = {}
  for _ in range(int(raw_input())):
    name = raw_input()
    score = float(raw_input())
    if(score in dict):
      dict[score].append(name)
    else:
      dict[score] = [name]
    if(score >= max1):
      if(score != max1):
        max2 = max1
      max1 = score
    elif(score > max2):
      max2 = score
  res = dict[max2]
  res.sort()
  for i in range(len(res)):
    print(res[i])

if __name__ == '__main__':
  main()