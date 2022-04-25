#program to remove two elements and replace it with one element
color = ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
color = ['Purple' if (i == 'Black') | (i == 'Pink') else i for i in color]
print(color)