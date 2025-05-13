import allure
from playwright.sync_api import Page

from components.base_component import BaseComponent
from elements.text import Text


class CoursesToolbarViewComponent(BaseComponent):
    def __init__(self, page: Page):
        super().__init__(page)

        self.title = Text(page, 'courses-list-toolbar-title-text', 'Courses')

    @allure.step("Check visible courses toolbar view")
    def check_visible(self):
        self.title.check_visible()
        self.title.check_have_text('Courses')
