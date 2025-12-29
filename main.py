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

class DataService:
    def __init__(self, courses, groups, groups_courses):
        self.courses = courses
        self.groups = groups
        self.groups_courses = groups_courses

    def get_one_to_many(self):
        return [(g.name, g.student_count, c.name)
                for c in self.courses
                for g in self.groups
                if g.course_id == c.id]

    def get_many_to_many(self):
        many_to_many_temp = [(c.name, gc.course_id, gc.group_id)
                             for c in self.courses
                             for gc in self.groups_courses
                             if c.id == gc.course_id]

        return [(g.name, course_name)
                for course_name, course_id, group_id in many_to_many_temp
                for g in self.groups if g.id == group_id]

class GroupProcessor:
    def __init__(self, data_service):
        self.data_service = data_service

    def get_groups_with_courses_starting_with_a(self):
        one_to_many = self.data_service.get_one_to_many()
        res = list(filter(lambda i: i[2].startswith('А'), one_to_many))
        return sorted(res, key=itemgetter(2))

    def get_max_students_per_course(self):
        one_to_many = self.data_service.get_one_to_many()
        res_unsorted = []

        for c in self.data_service.courses:
            c_groups = list(filter(lambda i: i[2] == c.name, one_to_many))
            if len(c_groups) > 0:
                c_students = [student_count for _, student_count, _ in c_groups]
                c_max_students = max(c_students)
                res_unsorted.append((c.name, c_max_students))

        return sorted(res_unsorted, key=itemgetter(1), reverse=True)

    def get_all_groups_with_courses_sorted(self):
        many_to_many = self.data_service.get_many_to_many()
        return sorted(many_to_many, key=itemgetter(1))

def main():
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

    data_service = DataService(courses, groups, groups_courses)
    processor = GroupProcessor(data_service)

    print('Задание Г1')
    res_1 = processor.get_groups_with_courses_starting_with_a()
    for group_name, student_count, course_name in res_1:
        print(f'Курс: {course_name}, Группа: {group_name}, Студентов: {student_count}')

    print('\nЗадание Г2')
    res_2 = processor.get_max_students_per_course()
    for course_name, max_students in res_2:
        print(f'Курс: {course_name}, Макс. студентов в группе: {max_students}')

    print('\nЗадание Г3')
    res_3 = processor.get_all_groups_with_courses_sorted()
    for group_name, course_name in res_3:
        print(f'Курс: {course_name}, Группа: {group_name}')

if __name__ == '__main__':
    main()
