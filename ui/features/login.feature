Feature: Login to ElectronicsComp website
  As a registered user
  I want to log in to the ElectronicsComp website
  So that I can access my account and make purchases

  Background:
    Given the user is on the ElectronicsComp login page
  @smoke
  Scenario: Successful login with valid credentials
    When the user enters valid username and password
    And clicks the login button
    Then the user should be redirected to the homepage
  @smoke
  Scenario: Login attempt with invalid credentials
    When the user enters invalid username or password
    And clicks the login button
    Then an error message should be displayed
    And the user should remain on the login page

  @smoke
  Scenario: Login with empty credentials
    When the user leaves username and password fields empty
    And clicks the login button
    Then an error message should prompt the user to fill in the required fields

  @smoke
  Scenario: Password reset option availability
    When the user clicks the Forgot Password link
    Then the user should be redirected to the password recovery page
