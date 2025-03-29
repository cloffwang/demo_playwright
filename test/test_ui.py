import pytest
from playwright.sync_api import Page
from test.page import HomePage
from helpers.file_loader import load_csv
from pathlib import Path

TEST_DATA_CSV = Path('data/convert_test.csv')
try:
    test_data = load_csv(TEST_DATA_CSV, ["input","from_cur", "to_cur", "expected"])
except Exception as e:
    test_data = []
    pytest.skip(f"Skipping due to loading csv files: {e}", allow_module_level=True)

@pytest.mark.parametrize(
        "input, from_cur, to_cur, expected",
        test_data
)
def test_result_appear(page, input, from_cur, to_cur, expected):
    hompage = HomePage(page)
    hompage.get()
    hompage.fill_input(input)
    hompage.select(from_cur, to_cur)
    hompage.click_convert()
    hompage.has_result()
    result = hompage.get_covered_value()
    if from_cur == to_cur:
        assert result == float(expected)
    else:
        assert result 

