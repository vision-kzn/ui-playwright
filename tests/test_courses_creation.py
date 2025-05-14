import allure
import pytest

from components.enums.course_action_enum import CourseActionEnum
from pages.courses.course_page import CoursePage
from pages.courses.courses_page import CoursesPage
from tools.routes import AppRoute


@pytest.mark.regression
@pytest.mark.course
class TestCoursesCreation:
    data = [
        (
            "First course test",
            "10",
            "Test description",
            "100",
            "90"
        )
    ]

    @pytest.mark.parametrize("data", data)
    @allure.title("Successful course creation")
    def test_successful_course_creation(
            self,
            courses_page: CoursesPage,
            course_page: CoursePage,
            data: tuple
    ):
        courses_page.visit(AppRoute.COURSES)
        courses_page.courses_toolbar_view.check_visible()
        courses_page.courses_toolbar_view.click_create_button()

        course_page.course_form.check_visible(title="", estimated_time="", description="", max_score="0", min_score="0", has_image=False)
        course_page.save_course_toolbar_view.check_visible(CourseActionEnum.create, data_filled=False)

        course_page.course_form.fill(*data)

        course_page.save_course_toolbar_view.check_visible(CourseActionEnum.create, data_filled=True)
        course_page.save_course_toolbar_view.click_save_button()

        courses_page.courses_view.check_visible_created_course(title=data[0])

        # TODO a lot of courses creation and other tests
