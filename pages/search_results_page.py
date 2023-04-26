from selenium.webdriver.common.by import By
from pages.base_page import Page


class SearchResultsPage(Page):
    RESULTS = (By.ID, 'ProductCount')

    def verify_search_results(self, product_name):
        actual_result = self.driver.find_element(*self.RESULTS).text
        assert product_name.lower() in actual_result.lower(), f'Expected {product_name} not in {actual_result}'
