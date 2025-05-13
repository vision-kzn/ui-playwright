from re import Pattern

import allure
from playwright.sync_api import Page

from components.base_component import BaseComponent
from elements.button import Button


class SidebarListItemComponent(BaseComponent):
    def __init__(self, page: Page, identifier: str):
        super().__init__(page)

        self.title = Button(page, f'{identifier}-dashboard-toolbar-title-text', identifier)

    @allure.step("Check visible sidebar list item")
    def check_visible(self, identifier: str):
        self.title.check_visible()
        self.title.check_have_text(identifier)@allure.step("Check visible sidebar list item")

    @allure.step("Navigate to sidebar list item")
    def navigate(self, expected_url: Pattern[str]):
        self.title.click()
        self.check_current_url(expected_url)
