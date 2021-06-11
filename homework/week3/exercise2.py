# Creating dictionary
student_scores = {'Amy': 67,
                'Billy' : 70,
                'Charlie' : 90,
                'Daisy': 66,
                'Emily': 71}

# Function to add a new key:value pair
def addKeyValue(key, value):
    student_scores[key] = value
    print(student_scores)

addKeyValue('Fran', 85)

# Creating a list named passStudents of students who have a score >=70 
passStudents = []
notpassStudents = []
for k,v in student_scores.items():
    if v >= 70:
        passStudents.append(k)
    else:
        notpassStudents.append(k)
print(passStudents)
print(notpassStudents)

# Removing students from dictionary who have a score of less than 70
for j in notpassStudents:
    if j in student_scores.keys():
        del student_scores[j]

print(student_scores)
