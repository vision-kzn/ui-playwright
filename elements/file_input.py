import pathlib
import tempfile
import typing

import allure
from playwright.sync_api import expect, Locator, FilePayload, Page

from elements.base_element import BaseElement
from tools.logger import get_logger

logger = get_logger("FILE_INPUT")


class FileInput(BaseElement):
    def __init__(self, page: Page, locator: str, name: str) -> None:
        super().__init__(page, locator, name)

    @property
    def type_of(self) -> str:
        return "file_input"

    def get_locator(self, nth: int = 0, **kwargs) -> Locator:
        return super().get_locator(nth, **kwargs).locator('input')

    def upload(
        self,
        files: typing.Union[
            str,
            pathlib.Path,
            FilePayload,
            typing.Sequence[typing.Union[str, pathlib.Path]],
            typing.Sequence[FilePayload],
        ],
        nth: int = 0,
        **kwargs
    ):
        step = f'Upload file to {self.type_of} "{self.name}"'

        with allure.step(step):
            locator = self.get_locator(nth, **kwargs)
            logger.info(step)
            locator.set_input_files(files)

