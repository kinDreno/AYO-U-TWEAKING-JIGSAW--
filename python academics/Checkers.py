# students = [
#     {'name': 'Alice', 'grade': 90},
#     {'name': 'Bob', 'grade': 75},
#     {'name': 'Charlie', 'grade': 60},
#     {'name': 'David', 'grade': 80},
#     {'name': 'Eve', 'grade': 55},
# ]

# grd = [student for student in students if student['grade'] > 76]
# print(grd)


x = "Hello world"
nest = [[word] for word in x.split()]
print(nest)


y = []
for n in nest:
    if len(n[0]) > 4:  
        
        y.append([n[0][::-1]]) 
    else:
        y.append(n)

print(y)  

result_string = ' '.join([item[0] for item in y])

print(result_string) 
