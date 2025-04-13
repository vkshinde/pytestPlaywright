import pytest
import configparser
import os
from jproperties import Properties
from playwright.async_api import Playwright
from playwright.sync_api import sync_playwright, Browser
from Utility.test_data import TestData


@pytest.fixture(scope="session")
def read_properties():
    # Path to the properties file
    properties_file = os.path.join(os.path.dirname(__file__), "config.properties")
    config = configparser.ConfigParser()
    config.read(properties_file)
    return config

@pytest.fixture(scope="session")
def read_properties():
    # Path to the properties file
    properties_file = os.path.join(os.path.dirname(__file__), "user_credentials.properties")
    properties = Properties()
    with open(properties_file, "rb") as file:
        properties.load(file)
    return properties

@pytest.fixture(scope="session", autouse=True)
def page_setup(browser: Browser, playwright: Playwright, request, pytestconfig):
    context_args = {
        "viewport": {"width":1900,"height":900},
        "is_mobile": False,
        "has_touch": False
    }
    context = browser.new_context(**context_args)
    context.tracing.start(
        title=request.node.name,
        screenshots=True,
        snapshots=True
    )
    context.tracing.start_chunk()
    page = context.new_page()
    yield page
    context.tracing.stop_chunk(path=f"data/trace_{request.node.name}.zip")
    page.close()

@pytest.fixture(scope="session")
def test_data(read_properties):
    test_data = TestData()
    test_data.set_properties(read_properties)
    yield test_data

@pytest.fixture(scope="session")
def api_context(page_setup):
    api_context = page_setup.context.request
    yield api_context

@pytest.fixture(scope="session", autouse=True)
def allure_environment(request):
    environment_variables = dict()
    yield  environment_variables
    allure_dir = request.config.getoption("--alluredir")
    allure_dir_path = os.path.join(allure_dir, "environment.properties")
    data = [f"{key}-{value}"for key, value in environment_variables.items()]
    with open(allure_dir_path, "w") as file:
        file.write("\n".join(data))

@pytest.fixture(autouse=True)
def environment_variables(allure_environment, page_setup, browser, test_data):
    allure_environment.update({"URL": test_data.get_url})
    allure_environment.update({"Browser": browser.browser_type.name})


