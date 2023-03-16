Feature: Check the Login functionality on HerukuApp

  Background:
    Given login: I am a user on the HerukuApp login page

  @login_heruku
  Scenario: Check the user, password and login button
    When login: I check the username field
    When login: I check the password field
    When login: I check the login button to be displayed and enabled
    Then login: I log in successfully with "tomsmith" and "SuperSecretPassword!"

#  behave -f html -o behave-report.html --tags=login_heruku