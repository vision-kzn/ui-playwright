import allure
import pytest

from pages.courses_page import CoursesPage
from tools.routes import AppRoute


@pytest.mark.regression
@pytest.mark.registration
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
            data: tuple
    ):
        courses_page.visit(AppRoute.COURSES)
        courses_page.courses_toolbar_view.check_visible()
        courses_page.click_create_button()

        courses_page.create_course_form.check_visible(title="", estimated_time="", description="", max_score="0", min_score="0")
        courses_page.create_course_form.fill(*data)
        courses_page.create_course_form.click_save_button()

        courses_page.check_visible_created_course(title=data[0])

        # TODO a lot of courses creation and other tests
