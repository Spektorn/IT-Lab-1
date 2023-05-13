# Массив с данными студентов
groupmates = [
    {
        "name": "Михаил",
        "surname": "Иванов",
        "exams": ["Информатика", "БЖД", "Философия"],
        "marks": [5, 4, 4]
    },
    {
        "name": "Александр",
        "surname": "Петров",
        "exams": ["История", "Информатика", "АиГ"],
        "marks": [5, 3, 3]
    },
    {
        "name": "Анастасия",
        "surname": "Фролова",
        "exams": ["КТП", "ИС", "МСиС"],
        "marks": [5, 4, 5]
    },
    {
        "name": "Валерия",
        "surname": "Смирнова",
        "exams": ["БЖД", "КТП", "Философия"],
        "marks": [5, 5, 5]
    },
    {
        "name": "Иван",
        "surname": "Федоров",
        "exams": ["Информатика", "АиГ", "МСиС"],
        "marks": [3, 3, 4]
    },
    {
        "name": "Федор",
        "surname": "Кузнецов",
        "exams": ["ИС", "КТП", "История"],
        "marks": [3, 4, 5]
    },
    {
        "name": "Кирилл",
        "surname": "Суханов",
        "exams": ["МСиС", "АиГ", "Философия"],
        "marks": [3, 5, 4]
    },
]

# Функция для фильтрации студентов по заданному среднему баллу
def filter_students_by_average_mark(students, expected_average):
    filtered_students = []

    for student in students:
        average_mark = 0

        for mark in student["marks"]:
            average_mark += mark
        
        average_mark /= len(student["marks"])
        
        if average_mark > expected_average:
            filtered_students.append(student)
    
    return filtered_students

# Функция для вывода списка студентов
def print_students(students):
    print(u"Имя".ljust(15), u"Фамилия".ljust(10), u"Экзамены".ljust(40), u"Оценки".ljust(20))

    for student in students:
        print(student["name"].ljust(15), 
              student["surname"].ljust(10), 
              str(student["exams"]).ljust(40), 
              str(student["marks"]).ljust(20))

expected_average = float(input("Введите средний балл: "))
filtered_students = filter_students_by_average_mark(groupmates, expected_average)

print_students(filtered_students)
