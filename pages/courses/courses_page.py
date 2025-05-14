import re

from playwright.sync_api import Page

from components.courses.courses_toolbar_view_component import CoursesToolbarViewComponent
from components.courses.courses_view_component import CoursesViewComponent
from elements.text import Text
from pages.base_page import BasePage


class CoursesPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)

        self.courses_toolbar_view = CoursesToolbarViewComponent(page)
        self.courses_view = CoursesViewComponent(page)
