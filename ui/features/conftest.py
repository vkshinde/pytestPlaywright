import pytest

from ui.pages.login_page import LoginPage


@pytest.fixture
def login_page(page_setup) -> LoginPage:
    return LoginPage(page_setup)

