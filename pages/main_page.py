from selenium.webdriver.common.by import By
from pages.base_page import Page


class MainPage(Page):
    SEARCH_ICON = (By.CSS_SELECTOR, '.header__search')
    SEARCH_FIELD = (By.ID, 'Search-In-Modal')
    SEARCH_BUTTON = (By.CSS_SELECTOR, 'button[aria-label="Search our site"]')

    def open_main_page(self):
        self.open_url('https://shop.cureskin.com/')

    def click_on_search_icon(self):
        self.click(*self.SEARCH_ICON)

    def search_for_product(self, text):
        self.input_text(text, *self.SEARCH_FIELD)
        self.click(*self.SEARCH_BUTTON)
