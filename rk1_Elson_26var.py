from operator import itemgetter

class StudentGroup:
    def __init__(self, id, name, student_count, course_id):
        self.id = id
        self.name = name
        self.student_count = student_count
        self.course_id = course_id

class Course:
    def __init__(self, id, name):
        self.id = id
        self.name = name

class GroupCourse:
    def __init__(self, course_id, group_id):
        self.course_id = course_id
        self.group_id = group_id

courses = [
    Course(1, 'Архитектура АСОИУ'),
    Course(2, 'Аналитическая геометрия'),
    Course(3, 'Физика'),
    Course(4, 'Английский язык'),
    Course(5, 'Программирование'),
]

groups = [
    StudentGroup(1, 'ИУ5-35Б', 25, 1),
    StudentGroup(2, 'ИУ6-51', 30, 2),
    StudentGroup(3, 'МТ8-32Б', 20, 3),
    StudentGroup(4, 'СМ2-15', 15, 4),
    StudentGroup(5, 'РК1-66Б', 28, 1),
]

groups_courses = [
    GroupCourse(1, 1),
    GroupCourse(2, 2),
    GroupCourse(3, 3),
    GroupCourse(4, 4),
    GroupCourse(1, 5),
    GroupCourse(4, 1),
    GroupCourse(5, 2),
    GroupCourse(5, 5),
]

def main():
    one_to_many = [(g.name, g.student_count, c.name)
                   for c in courses
                   for g in groups
                   if g.course_id == c.id]

    many_to_many_temp = [(c.name, gc.course_id, gc.group_id)
                         for c in courses
                         for gc in groups_courses
                         if c.id == gc.course_id]

    many_to_many = [(g.name, course_name)
                    for course_name, course_id, group_id in many_to_many_temp
                    for g in groups if g.id == group_id]

    print('Задание Г1')
    res_1 = list(filter(lambda i: i[2].startswith('А'), one_to_many))
    res_1_sorted = sorted(res_1, key=itemgetter(2))
    for group_name, student_count, course_name in res_1_sorted:
        print(f'Курс: {course_name}, Группа: {group_name}, Студентов: {student_count}')

    print('\nЗадание Г2')
    res_2_unsorted = []
    for c in courses:
        c_groups = list(filter(lambda i: i[2] == c.name, one_to_many))
        if len(c_groups) > 0:
            c_students = [student_count for _, student_count, _ in c_groups]
            c_max_students = max(c_students)
            res_2_unsorted.append((c.name, c_max_students))

    res_2 = sorted(res_2_unsorted, key=itemgetter(1), reverse=True)
    for course_name, max_students in res_2:
        print(f'Курс: {course_name}, Макс. студентов в группе: {max_students}')

    print('\nЗадание Г3')
    res_3_sorted = sorted(many_to_many, key=itemgetter(1))
    for group_name, course_name in res_3_sorted:
        print(f'Курс: {course_name}, Группа: {group_name}')

if __name__ == '__main__':
    main()
