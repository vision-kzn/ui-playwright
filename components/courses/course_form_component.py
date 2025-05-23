import re
from pathlib import Path

import allure
from playwright.sync_api import Page

from components.base_component import BaseComponent
from elements.button import Button
from elements.file_input import FileInput
from elements.image import Image
from elements.input import Input
from elements.textarea import Textarea

LOCAL_IMAGE_PATH = Path("test_files/image1.jpg")


class CourseFormComponent(BaseComponent):
    def __init__(self, page: Page):
        super().__init__(page)

        self.title_input = Input(page, "create-course-form-title-input", "Title")
        self.estimated_time_input = Input(page, "create-course-form-estimated-time-input", "Estimated time")
        self.description_input = Textarea(page, "create-course-form-description-input", "Description")
        self.max_score_input = Input(page, "create-course-form-max-score-input", "Max score")
        self.min_score_input = Input(page, "create-course-form-min-score-input", "Min score")
        self.file_input = FileInput(page, "create-course-preview-image-upload-widget-upload-button", "Courses image upload widget")
        self.preview_image = Image(page, "create-course-preview-image-upload-widget-preview-image", "Course image preview")
        self.remove_image_button = Button(page, "create-course-preview-image-upload-widget-remove-button", "Remove image")

    @allure.step("Fill course creation form")
    def fill(self, title: str, estimated_time: str, description: str, max_score: str, min_score: str):
        self.title_input.fill(title)
        self.title_input.check_have_value(title)

        self.estimated_time_input.fill(estimated_time)
        self.estimated_time_input.check_have_value(estimated_time)

        self.description_input.fill(description)
        self.description_input.check_have_value(description)

        self.max_score_input.fill(max_score)
        self.max_score_input.check_have_value(max_score)

        self.min_score_input.fill(min_score)
        self.min_score_input.check_have_value(min_score)

        # TODO create temporary file
        self.file_input.upload(LOCAL_IMAGE_PATH)
        self.preview_image.check_visible()

    @allure.step("Check visible course creation form")
    def check_visible(self, title: str, estimated_time: str, description: str, max_score: str, min_score: str, has_image: bool):
        self.title_input.check_visible()
        self.title_input.check_have_value(title)

        self.estimated_time_input.check_visible()
        self.estimated_time_input.check_have_value(estimated_time)

        self.description_input.check_visible()
        self.description_input.check_have_value(description)

        self.max_score_input.check_visible()
        self.max_score_input.check_have_value(max_score)

        self.min_score_input.check_visible()
        self.min_score_input.check_have_value(min_score)

        self.file_input.check_visible()
        self.preview_image.check_visible() and self.remove_image_button.check_visible() if has_image else self.preview_image.check_hidden()



