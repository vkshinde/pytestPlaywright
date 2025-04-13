from pytest_bdd import scenarios, given, when, then

scenarios('login.feature')


@given("the user is on the ElectronicsComp login page")
def navigate_to_login_page(login_page, test_data):
    login_page.navigate_to_login_page(test_data.get_url)

@when("the user enters valid username and password")
def enter_valid_credentials(login_page, test_data):
    login_page.enter_username(test_data.get_property("username"))
    login_page.enter_password(test_data.get_property("password"))

@when("the user enters invalid username or password")
def enter_invalid_credentials(login_page):
    login_page.enter_username("invalid_user")
    login_page.enter_password("wrong_password")

@when("the user leaves username and password fields empty")
def leave_fields_empty(login_page):
    login_page.enter_username("")
    login_page.enter_password("")

@when("clicks the login button")
def click_login_button(login_page):
    login_page.click_login()

@then("the user should be redirected to the homepage")
def verify_redirection_to_homepage(page_setup):
    assert page_setup.url == "https://www.electronicscomp.com/my-account"  # Replace with actual URL

@then("an error message should be displayed")
def verify_error_message(login_page):
    error_message = login_page.get_error_message()
    assert error_message, "Invalid username or password"  # Replace with the actual error message

@then("the user should remain on the login page")
def verify_remains_on_login_page(page_setup):
    assert page_setup.url == "https://www.electronicscomp.com/login"

@then("an error message should prompt the user to fill in the required fields")
def verify_required_fields_message(login_page):
    error_message = login_page.get_error_message()
    assert error_message, "Username and password are required"  # Replace with the actual error message

@when("the user clicks the Forgot Password link")
def click_forgot_password(login_page):
    login_page.click_forgot_password()

@then("the user should be redirected to the password recovery page")
def verify_password_recovery_redirection(page_setup):
    assert page_setup.url == "https://www.electronicscomp.com/forgot-password"  # Replace with actual URL
