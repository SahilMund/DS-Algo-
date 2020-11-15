# You have a record of  students. Each record contains the student's name, and their percent marks in Maths, Physics and Chemistry. The marks can be floating values. The user enters some integer  followed by the names and marks for  students. You are required to save the record in a dictionary data type. The user then enters a student's name. Output the average percentage marks obtained by that student, correct to two decimal places.
# Input Format
# The first line contains the integer , the number of students. The next  lines contains the name and marks obtained by that student separated by a space. The final line contains the name of a particular student previously listed.
# Constraints
# Output Format
# Print one line: The average of the marks obtained by the particular student correct to 2 decimal places.
# Sample Input
# 3
# Krishna 67 68 69
# Arjun 70 98 63
# Malika 52 56 60
# Malika
# Sample Output
# 56.00

def main():
  N = int(raw_input())
  student_marks = {}
  for _ in range(N):
    line = raw_input().split()
    name = line[0]
    scores = line[1:]
    student_marks[name] = map(float, scores)
  query_name = raw_input()
  res = sum(student_marks[query_name]) / len(student_marks[query_name])
  print("%.2f" % res)

if __name__ == '__main__':
  main()