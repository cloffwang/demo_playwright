from playwright.sync_api import Page, expect
class HomePage:
    url = 'http://localhost:3000/'

    def __init__(self, page):
        self.page = page
        self.input = page.locator("[data-testid='amount']")
        self.field_from = page.locator("[data-testid='from-currency']")
        self.field_to = page.locator("[data-testid='to-currency']")
        self.button = page.locator("//button")
        self.result = page.locator(".result")

    def get(self):
        self.page.goto(self.url)

    def select(self, from_value, to_value):
        self.field_from.select_option(from_value)
        self.field_to.select_option(to_value)

    def fill_input(self, value):
        self.input.fill(value)

    def click_convert(self):
        self.button.click()
    
    def has_result(self) -> bool:
        expect(self.result).to_be_visible()

    def get_covered_value(self):
        text = self.result.text_content()
        converted = text.strip().split('=')[-1].strip().split()[0]
        return float(converted)
        
