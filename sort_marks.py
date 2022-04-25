# program to sort the marks of 5 students in a list
print("Enter the marks of 5 students")
marks= []
for i in range (0, 5):
    ele = int(input())
    marks.append(ele)
marks.sort()
print("The marks in ascending order are as follows", marks)
