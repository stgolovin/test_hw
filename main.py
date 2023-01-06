from constants import *
import requests


def task_1(geo_logs: list) -> list:
    russia_list = []
    for dicts in geo_logs:
        for item in dicts.values():
            if 'Россия' in item:
                russia_list.append(dicts)
    geo_logs = russia_list
    return geo_logs


def task_2(ids: dict) -> list:
    ids_upd = []
    ids_upd_2 = []
    ids_upd_3 = []
    for elem in ids.values():
        ids_upd.append(elem)
    for item in ids_upd:
        if type(item) is list:
            for digit in item:
                ids_upd_2.append(digit)
        else:
            ids_upd_2.append(item)
    for digit in ids_upd_2:
        if digit in ids_upd_3:
            pass
        else:
            ids_upd_3.append(digit)
    return ids_upd_3


def task_3(queries: list) -> str:
    lst_1 = []
    dct = {}
    for item in queries:
        lst_1.append(len(item.split()))
    for item_ in lst_1:
        dct.setdefault(item_, 0)
        dct[item_] += 1
    sum_v = 0
    for v in dct.values():
        sum_v += v
    for k, v in dct.items():
        percantage = v/sum_v * 100
        percantage = round(percantage, 1)
        final_str = f'Доля строк с {k}-мя словами составляет {percantage}%'
        return final_str


def task_4(stats: dict) -> str:
    list_ = []
    for value in stats.values():
        list_.append(value)
    max_value = max(list_)
    result = list(stats.keys())[list(stats.values()).index(max_value)]
    return result


def task_5(r_list: list) -> dict:
    dct = {r_list[-2]: r_list[-1]}
    for item in r_list[-3::-1]:
        dct = {item: dct}
    return dct


class YaDisk:
    def __init__(self, token: str):
        self.token = token

    def get_headers(self):
        return {
            'Content-Type': 'application/json',
            'Authorization': f'OAuth {self.token}'
        }

    def create_folder(self, folder_name: str) -> int:
        url = f'https://cloud-api.yandex.net/v1/disk/resources/'
        headers = self.get_headers()
        params = {'path': f'{folder_name}',
                  'overwrite': 'false'}
        try:
            response = requests.put(url=url, headers=headers, params=params)
            if response.status_code == 201:
                print(f'Папка "{folder_name}" создана.')
            else:
                print(f'Папка "{folder_name}" уже существует на диске.')
            return response.status_code
        except:
            print(f'Папку "{folder_name}" не удалось создать.')

    def get_info(self, folder_name):
        url = 'https://cloud-api.yandex.net/v1/disk/resources'
        headers = self.get_headers()
        params = {'path': f'{folder_name}'}
        response = requests.get(url=url, headers=headers, params=params)
        return response.status_code


ya_token = input('Введите токен Яндекс.Диск:   ')
uploader = YaDisk(ya_token)


if __name__ == '__main__':
    print(task_1(geo_logs=geo_logs))
    print(task_2(ids=ids))
    print(task_3(queries=queries))
    print(task_4(stats=stats))
    print(task_5(r_list=r_list))
    uploader.create_folder(folder_name='tratata')
    uploader.get_info(folder_name='tratata')
