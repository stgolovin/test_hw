import unittest
from parameterized import parameterized, parameterized_class
from main import task_1, task_2, task_3, task_4, task_5, YaDisk, ya_token, uploader
from constants import *

FIXTURE = [
    ({'facebook': 55, 'yandex': 120, 'vk': 115, 'google': 99, 'email': 42, 'ok': 98}, 'yandex'),
    ({'facebook': 105, 'yandex': 37, 'vk': 199, 'google': 77, 'email': 3, 'ok': 150}, 'vk'),
    ({'audi': 5, 'bmw': 100, 'vw': 150, 'opel': 55, 'mercedes': 79, 'jaguar': 99}, 'vw')
]


class TestFunc(unittest.TestCase):
    def test_task_1(self):
        result = task_1(geo_logs=geo_logs)
        etalon = [{'visit1': ['Москва', 'Россия']},
                  {'visit3': ['Владимир', 'Россия']},
                  {'visit7': ['Тула', 'Россия']},
                  {'visit8': ['Тула', 'Россия']},
                  {'visit9': ['Курск', 'Россия']},
                  {'visit10': ['Архангельск', 'Россия']}]
        self.assertEqual(result, etalon)

    def test_task_4(self):
        result = task_4(stats=stats)
        etalon = 'yandex'
        self.assertEqual(result, etalon)

    @parameterized.expand(FIXTURE)
    def test_task_4param(self, stats, etalon):
        result = task_4(stats)
        self.assertEqual(result, etalon)

    def test_task_4_2(self):
        result = task_4(stats=stats)
        self.assertIsInstance(result, str)


class TestFuncYa(unittest.TestCase):
    def test_yandex(self):
        result = uploader.create_folder(folder_name='tratata')
        etalon = 201
        self.assertEqual(result, etalon)

    def test_ya_folder(self):
        result = uploader.get_info(folder_name='tratata')
        etalon = 200
        self.assertEqual(result, etalon)
