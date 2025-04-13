import time

import allure
from playwright.sync_api import Page, Locator


class BasePage:
    def __init__(self, page:Page=None):
        self.page = page

    def open_url(self, url: str):
        """
        Open a specific URL.
        Args:
            url (str): The URL to navigate to.
        """
        self.page.goto(url)
        print(f"Navigated to URL: {url}")

    def get_current_url(self) -> str:
        """
        Get the current page URL.
        Returns:
            str: The current page URL.
        """
        return self.page.url

    def refresh_page(self):
        """
        Refresh the current page.
        """
        self.page.reload()
        print("Page refreshed.")

    def go_back(self):
        """
        Navigate to the previous page in the browser history.
        """
        self.page.go_back()
        print("Navigated back.")

    def go_forward(self):
        """
        Navigate to the next page in the browser history.
        """
        self.page.go_forward()
        print("Navigated forward.")

    def wait_for_navigation(self, timeout: int = 5000):
        """
        Wait for the navigation to complete.
        Args:
            timeout (int): Maximum wait time in milliseconds.
        """
        self.page.wait_for_load_state(state="load",timeout=timeout)
        print("Navigation completed.")

    def wait_for_element(self, locator: Locator, state: str = "visible", timeout: int = 5000):
        allure.attach(f"state: {state}", name="Log", attachment_type=allure.attachment_type.TEXT)
        if state.lower() == "visible":
            self.waiting()
            return locator.is_visible(timeout=timeout), f"Element not visible within {timeout} ms."
        elif state.lower() == "enabled":
            self.waiting()
            return locator.is_enabled(timeout=timeout), f"Element not enabled within {timeout} ms."
        else:
            raise ValueError(f"Unsupported state: {state}")

    def click_element(self, locator: Locator, timeout: int = 5000):
        """
        Wait for and click an element.
        Args:
            locator (Locator): The Playwright locator object.
            timeout (int): Maximum wait time for the element.
        """
        self.wait_for_navigation()
        self.wait_for_element(locator, state="visible", timeout=timeout)
        locator.click()

    def fill_input(self, locator: Locator, value: str, timeout: int = 5000):
        """
        Wait for an input field and fill it with a value.
        Args:
            locator (Locator): The Playwright locator object.
            value (str): The text to fill in the input field.
            timeout (int): Maximum wait time for the element.
        """
        self.wait_for_element(locator, state="visible", timeout=timeout)
        locator.fill(value)

    def get_text(self, locator: Locator, timeout: int = 5000) -> str:
        """
        Wait for an element and return its text content.
        Args:
            locator (Locator): The Playwright locator object.
            timeout (int): Maximum wait time for the element.
        Returns:
            str: The text content of the element.
        """
        self.wait_for_element(locator, state="visible", timeout=timeout)
        return locator.text_content()

    def is_element_visible(self, locator: Locator, timeout: int = 5000) -> bool:
        """
        Check if an element is visible within the specified timeout.
        Args:
            locator (Locator): The Playwright locator object.
            timeout (int): Maximum wait time.
        Returns:
            bool: True if the element is visible, False otherwise.
        """
        try:
            self.wait_for_element(locator, state="visible", timeout=timeout)
            return True
        except TimeoutError:
            return False

    def select_dropdown_option(self, locator: Locator, value: str, timeout: int = 5000):
        """
        Select a value in a dropdown menu.
        Args:
            locator (Locator): The Playwright locator object.
            value (str): The value to select.
            timeout (int): Maximum wait time for the element.
        """
        self.wait_for_element(locator, state="visible", timeout=timeout)
        locator.select_option(value)

    def hover_over_element(self, locator: Locator, timeout: int = 5000):
        """
        Hover over an element.
        Args:
            locator (Locator): The Playwright locator object.
            timeout (int): Maximum wait time for the element.
        """
        self.wait_for_element(locator, state="visible", timeout=timeout)
        locator.hover()

    def get_attribute(self, locator: Locator, attribute: str, timeout: int = 5000) -> str:
        """
        Get an attribute's value from an element.
        Args:
            locator (Locator): The Playwright locator object.
            attribute (str): The attribute to retrieve.
            timeout (int): Maximum wait time for the element.
        Returns:
            str: The value of the attribute.
        """
        self.wait_for_element(locator, state="visible", timeout=timeout)
        return locator.get_attribute(attribute)

    def take_screenshot(self, path: str = "screenshot.png"):
        """
        Take a screenshot of the current page.
        Args:
            path (str): The file path to save the screenshot.
        """
        self.page.screenshot(path=path)



















    @staticmethod
    def waiting(delay=1):
        time.sleep(delay)

