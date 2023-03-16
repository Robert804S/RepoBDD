Feature: Check the Forgot password functionality
"""se ruleaza inainte de fiecare scenariu"""

  Background:
    Given login: I am a user on the login page
    When  login: I click on the forgot password link

  @smoke
  Scenario: Check validation error message when email is invalid format
    When forgot_pass: I fill in my email "my_email@"
    When forgot_pass: I click on the recover button
    Then forgot_pass: I verify the invalid email validation message "Wrong email"

  @test
  Scenario: Check validation error message when email is empty
    When forgot_pass: I make sure the email input is cleared
    When forgot_pass: I click on the recover button
    Then forgot_pass: I verify the invalid email validation message "Enter your email"

  @multiple_value_email
  Scenario Outline: Check various email validation
    When forgot_pass: I fill in my email "<email>"
    When forgot_pass: I click on the recover button
    Then forgot_pass: I verify the invalid email validation message "<expected_error>"
    Then forgot_pass: I verify the notification "<expected_notification>"

  Examples:
    |email         |expected_error|expected_notification|
    |test          |Wrong email   |None                 |
    |test@         |Wrong email   |None                 |
    |test.com      |Wrong email   |None                 |
    |test@mail.com |None          |Email not found.     |

#    behave -f html -o behave-report.html --tags=