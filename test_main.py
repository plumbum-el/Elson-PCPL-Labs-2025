import unittest
from main import StudentGroup, Course, GroupCourse, DataService, GroupProcessor

class TestGroupProcessor(unittest.TestCase):

    def setUp(self):
        self.courses = [
            Course(1, 'Архитектура АСОИУ'),
            Course(2, 'Аналитическая геометрия'),
            Course(3, 'Физика'),
            Course(4, 'Английский язык'),
            Course(5, 'Программирование'),
        ]

        self.groups = [
            StudentGroup(1, 'ИУ5-35Б', 25, 1),
            StudentGroup(2, 'ИУ6-51', 30, 2),
            StudentGroup(3, 'МТ8-32Б', 20, 3),
            StudentGroup(4, 'СМ2-15', 15, 4),
            StudentGroup(5, 'РК1-66Б', 28, 1),
        ]

        self.groups_courses = [
            GroupCourse(1, 1),
            GroupCourse(2, 2),
            GroupCourse(3, 3),
            GroupCourse(4, 4),
            GroupCourse(1, 5),
            GroupCourse(4, 1),
            GroupCourse(5, 2),
            GroupCourse(5, 5),
        ]

        self.data_service = DataService(self.courses, self.groups, self.groups_courses)
        self.processor = GroupProcessor(self.data_service)

    def test_get_groups_with_courses_starting_with_a(self):
        result = self.processor.get_groups_with_courses_starting_with_a()

        self.assertGreater(len(result), 0)

        for group_name, student_count, course_name in result:
            self.assertTrue(course_name.startswith('А'))

        sorted_result = sorted(result, key=lambda x: x[2])
        self.assertEqual(result, sorted_result)

        expected_courses = ['Аналитическая геометрия', 'Архитектура АСОИУ', 'Английский язык']
        result_courses = [course_name for _, _, course_name in result]
        for expected in expected_courses:
            self.assertIn(expected, result_courses)

    def test_get_max_students_per_course(self):
        result = self.processor.get_max_students_per_course()

        self.assertGreater(len(result), 0)

        for i in range(len(result) - 1):
            self.assertGreaterEqual(result[i][1], result[i + 1][1])

        result_dict = dict(result)

        self.assertEqual(result_dict.get('Архитектура АСОИУ'), 28)
        self.assertEqual(result_dict.get('Аналитическая геометрия'), 30)

        for course_name, max_students in result:
            self.assertIsInstance(max_students, int)
            self.assertGreater(max_students, 0)

    def test_get_all_groups_with_courses_sorted(self):
        result = self.processor.get_all_groups_with_courses_sorted()

        self.assertGreater(len(result), 0)

        sorted_result = sorted(result, key=lambda x: x[1])
        self.assertEqual(result, sorted_result)

        for group_name, course_name in result:
            self.assertIsInstance(group_name, str)
            self.assertIsInstance(course_name, str)
            self.assertGreater(len(group_name), 0)
            self.assertGreater(len(course_name), 0)

        group_courses = [course_name for group_name, course_name in result
                        if group_name == 'ИУ5-35Б']
        expected_courses_for_group = ['Архитектура АСОИУ', 'Английский язык']
        for expected in expected_courses_for_group:
            self.assertIn(expected, group_courses)

if __name__ == '__main__':
    unittest.main(verbosity=2)
