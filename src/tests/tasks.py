
from invoke import task

import requests
import json
import pytest

from requests.auth import HTTPBasicAuth


"""
    Тест проверяющий получения списка пользователей с пагинацией в качестве параметра метода
"""
@pytest.mark.parametrize(argnames="param",argvalues=[
    1, 2, 3
])
def test_get_categories_success(param):
    # payload = {"key1": 1, "key2": "value2"}
    
    url = "http://91.210.171.73:8080/api/category?limit={}&offset={}"

    position = 0

    dictionary = dict()

    res = requests.get(url.format(param, position),
                       auth=HTTPBasicAuth('admin', 'admin'))

    count = int(json.loads(res.content)["count"])

    while 10 > position and res.status_code == 200:
        res = requests.get(url.format(param, position),
                           auth=HTTPBasicAuth('admin', 'admin'))
        print(json.loads(res.content), res.status_code)

        entity = json.loads(res.content)["results"][0]
        if entity["id"] in dictionary:
            raise RuntimeError(
                "Entity with id {} already exists!".format(entity["id"]))
        dictionary[entity["id"]] = entity["name"]
        position += param
        

"""
    Тест проверяющий удаление пользователя
"""
@pytest.mark.parametrize(argnames="param",argvalues=[
    238
])
def test_delete_category_success(param):
    
    uri_delete = "http://91.210.171.73:8080/api/category/{}/"

    uri_get = "http://91.210.171.73:8080/api/category/{}"

    res = requests.get(uri_get.format(param), auth=HTTPBasicAuth('admin', 'admin'))
    
    assert res.status_code == 200
    
    result = json.loads(res.content)

    res = requests.delete(uri_delete.format(param), auth=HTTPBasicAuth('admin', 'admin'))
    
    assert res.status_code < 300
    
    res = requests.get(uri_get.format(param), auth=HTTPBasicAuth('admin', 'admin'))
    
    assert res.status_code != 200
    

        
        

def test_my_test():
    assert 0 == 0
