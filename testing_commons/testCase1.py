import json
import jsonpath
import pytest
import requests



def test_function():
    url = "https://reqres.in/api/users?page=2"

    url_response = requests.get(url)

    response_status_code = url_response.status_code

    json_text = json.loads(url_response.text)

    per_page = jsonpath.jsonpath(json_text, 'per_page')

    #students = jsonpath.jsonpath(json_text, 'data')

    students = url_response.json()['data']
    assert response_status_code == 200

    assert per_page[0] == 6

    assert students[0] == {'avatar': 'https://reqres.in/img/faces/7-image.jpg',
 'email': 'michael.lawson@reqres.in',
 'first_name': 'Michael',
 'id': 7,
 'last_name': 'Lawson'}


