import re

from playwright.sync_api import Page

from components.courses.courses_toolbar_view_component import CoursesToolbarViewComponent
from components.courses.create_course_form_component import CreateCourseFormComponent
from elements.button import Button
from elements.text import Text
from pages.base_page import BasePage


class CoursesPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)

        self.courses_toolbar_view = CoursesToolbarViewComponent(page)
        self.create_course_form = CreateCourseFormComponent(page)

        self.create_course_button = Button(page, "courses-list-toolbar-create-course-button", "Create course")
        self.course_title = Text(page, "course-widget-title-text", "Course title")

    def click_create_button(self):
        self.create_course_button.click()
        self.check_current_url(re.compile(".*/#/courses/create"))

    def check_visible_created_course(self, title: str):
        self.course_title.check_visible()
        self.course_title.check_have_text(title)
