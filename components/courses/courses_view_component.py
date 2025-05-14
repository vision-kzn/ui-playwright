import re

import allure
from playwright.sync_api import Page

from components.base_component import BaseComponent
from elements.button import Button
from elements.text import Text


class CoursesViewComponent(BaseComponent):
    def __init__(self, page: Page):
        super().__init__(page)

        self.course_title = Text(page, "course-widget-title-text", "Course title")

        self.menu_button = Button(page, "course-view-menu-button", "Menu")

    @allure.step("Check visible courses toolbar view")
    def check_visible_created_course(self, title: str):
        self.course_title.check_visible()
        self.course_title.check_have_text(title)

    def click_menu_button(self):
        self.menu_button.click()
