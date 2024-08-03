grades = [[5, 3, 3, 5, 4],[2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
students=sorted(students)
students_new_list= {}
for student, grades_list in zip(students, grades):
    average = sum(grades_list) / len(grades_list)
    students_new_list[student] = average
print(students_new_list)


