from selenium.webdriver.common.by import By
from pages.base_page import Page


class MainPage(Page):
    SEARCH_ICON = (By.CSS_SELECTOR, '.header__search')
    SEARCH_FIELD = (By.ID, 'Search-In-Modal')
    SEARCH_BUTTON = (By.CSS_SELECTOR, 'button[aria-label="Search our site"]')
    FOOTER_POLICY_LINKS = (By.CSS_SELECTOR, 'a[href*="/policies"]')
    POLICY_LINK_TITLE = (By.CSS_SELECTOR, '.shopify-policy__title')

    def open_main_page(self):
        self.open_url('https://shop.cureskin.com/')

    def click_on_search_icon(self):
        self.click(*self.SEARCH_ICON)

    def search_for_product(self, text):
        self.input_text(text, *self.SEARCH_FIELD)
        self.click(*self.SEARCH_BUTTON)

    def verify_policy_links(self):
        links = self.find_elements(*self.FOOTER_POLICY_LINKS)
        for i in range(len(links)):
            link = self.find_elements(*self.FOOTER_POLICY_LINKS)[i]
            link_name = link.text
            link.click()
            link_title = self.find_element(*self.POLICY_LINK_TITLE).text
            assert link_name.lower() in link_title.lower(), \
                f'Link name {link_name} not in link title{link_title}'
