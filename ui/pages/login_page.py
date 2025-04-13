from playwright.async_api import Page
from ui.pages.base_page import BasePage


class LoginPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)
        self.page = page
        self.username_input = self.page.get_by_role("textbox", name="Email or mobile number")
        self.password_input = self.page.get_by_role("textbox", name="Password Enter OTP")
        self.login_nav = self.page.locator("//a[normalize-space()=\"Login\"]")
        self.login_button = self.page.get_by_role("button", name="Login")
        self.error_message = self.page.get_by_text("Warning: No match for E-Mail")
        self.forgot_password_link = self.page.locator("#form-login").get_by_role("link", name="Forgotten Password")

    def navigate_to_login_page(self, url):
        self.open_url(url)
        self.click_element(self.login_nav)

    def enter_username(self, username):
        self.fill_input(self.username_input, username)

    def enter_password(self, password):
        self.fill_input(self.password_input, password)

    def click_login(self):
        self.click_element(self.login_button)

    def get_error_message(self):
        return self.wait_for_element(self.error_message, "visible")

    def click_forgot_password(self):
        self.forgot_password_link.click()
