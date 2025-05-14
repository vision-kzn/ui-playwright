import re

import allure
from playwright.sync_api import Page

from components.base_component import BaseComponent
from components.enums.course_action_enum import CourseActionEnum
from elements.button import Button
from elements.text import Text


class CourseToolbarViewComponent(BaseComponent):
    def __init__(self, page: Page):
        super().__init__(page)

        self.title = Text(page, 'create-course-toolbar-title-text', 'Create course')
        self.save_button = Button(page, "create-course-toolbar-create-course-button", "Save")

    @allure.step("Check visible create course toolbar view, while data is filled or not, depending on action")
    def check_visible(self, action: CourseActionEnum, data_filled: bool):
        """

        :param action: Toolbar for create or update action
        :param data_filled: True if data is filled and "save" button should be enabled
        :return: void
        """
        self.title.check_visible()
        self.title.check_have_text('Create course') \
            if action == CourseActionEnum.create \
            else self.title.check_have_text('Update course')

        self.save_button.check_visible()
        self.save_button.check_enabled() if data_filled else self.save_button.check_disabled()

    @allure.step("Click save button")
    def click_save_button(self):
        self.save_button.click()
        self.check_current_url(re.compile(".*/#/courses"))
