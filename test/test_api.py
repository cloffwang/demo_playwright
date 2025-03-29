import requests
from pathlib import Path
from helpers.file_loader import load_csv
import pytest

URL = 'https://cdn.jsdelivr.net/npm/@fawazahmed0/currency-api@latest/v1/currencies.json'
TEST_DATA_CSV = Path('data/cur_name_test.csv')
try:
    test_data = load_csv(TEST_DATA_CSV, ["code","name"])
except Exception as e:
    test_data = []
    pytest.skip(f"Skipping due to loading csv files: {e}", allow_module_level=True)

@pytest.fixture(scope="module")
def get_response():
    yield requests.get(URL)

def test_response_ok(get_response):
    assert get_response.status_code == 200

@pytest.mark.parametrize(
        "code, name",
        test_data
        )
def test_code_name(get_response, code, name):
    jsonobj = get_response.json()
    assert jsonobj[code] == name