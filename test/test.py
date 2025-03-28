import pytest
from playwright.sync_api import sync_playwright
from page import HomePage

def test_result_appear():
    with sync_playwright() as pw:
        browser = pw.chromium.launch()
        context = browser.new_context()
        page = context.new_page()
        hompage = HomePage(page)
        hompage.get()
        hompage.fill_input("1")
        hompage.select("1inch", "ada")
        hompage.click_convert()
        hompage.is_text_appear()