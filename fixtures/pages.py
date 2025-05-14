import uuid

import allure
import pytest
from playwright.sync_api import Playwright, Page, expect

from config import Settings
from pages.courses.course_page import CoursePage
from pages.courses.courses_page import CoursesPage
from pages.dashboard_page import DashboardPage
from pages.registration_page import RegistrationPage
from tools.routes import AppRoute


@pytest.fixture
def chromium_page(playwright: Playwright, settings: Settings) -> Page:
    expect.set_options(timeout=settings.expect_timeout)

    browser = playwright.chromium.launch(headless=settings.headless)
    context = browser.new_context(
        base_url=f"{settings.app_url}/",
        record_video_dir=settings.videos_dir
    )
    context.tracing.start(screenshots=True, snapshots=True, sources=True)

    page = context.new_page()
    yield page

    tracing_file = settings.tracing_dir.joinpath(f'{uuid.uuid4()}.zip')
    context.tracing.stop(path=tracing_file)
    browser.close()

    allure.attach.file(tracing_file, name='trace', extension='zip')
    allure.attach.file(page.video.path(), name='video', attachment_type=allure.attachment_type.WEBM)


@pytest.fixture
def dashboard_page(chromium_page: Page) -> DashboardPage:
    return DashboardPage(page=chromium_page)


@pytest.fixture
def registration_page(chromium_page: Page) -> RegistrationPage:
    return RegistrationPage(page=chromium_page)


@pytest.fixture
def course_page(chromium_page: Page) -> CoursePage:
    return CoursePage(page=chromium_page)


@pytest.fixture
def courses_page(chromium_page: Page, registration_page: RegistrationPage, dashboard_page: DashboardPage):
    registration_page.visit(AppRoute.REGISTRATION)
    registration_page.registration_form.check_visible(email="", username="", password="")
    registration_page.registration_form.fill(
        email="user@example.com",
        username="Playwright",
        password="qwerty"
    )
    registration_page.click_registration_button()

    dashboard_page.navbar.check_visible("Playwright")

    yield CoursesPage(page=registration_page.page)

    # TODO using login page
