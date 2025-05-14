import re

from playwright.sync_api import Page

from components.courses.course_form_component import CourseFormComponent
from components.courses.course_toolbar_view_component import CourseToolbarViewComponent
from pages.base_page import BasePage


class CoursePage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)

        self.save_course_toolbar_view = CourseToolbarViewComponent(page)
        self.course_form = CourseFormComponent(page)



