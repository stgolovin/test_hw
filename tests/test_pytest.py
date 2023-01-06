import pytest
from main import task_1, task_2, task_3, task_4, task_5
from constants import *


class TestFunc:
    def test_task_1(self):
        result = task_1(geo_logs=geo_logs)
        etalon = [{'visit1': ['Москва', 'Россия']},
                  {'visit3': ['Владимир', 'Россия']},
                  {'visit7': ['Тула', 'Россия']},
                  {'visit8': ['Тула', 'Россия']},
                  {'visit9': ['Курск', 'Россия']},
                  {'visit10': ['Архангельск', 'Россия']}]
        assert result == etalon
