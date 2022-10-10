import requests
import pytest

headers = {
    'Content-Type': 'application/json',
    'Authorization': f'OAuth AQAAAAAe1CU1AADLW3g9SRXLakVDs6qbBD5fLC4'}
url = 'https://cloud-api.yandex.net/v1/disk/resources'
answer = [('test_folder', 201), ('test_folder', 409), (None, 400)]


@pytest.mark.parametrize('folder, code', answer)
def test_response_code(folder, code):
    res = requests.put(url, headers=headers, params={'path': folder})
    assert res.status_code == code
