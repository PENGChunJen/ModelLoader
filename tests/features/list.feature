Feature: List All Models
  As a user,
  I want to see all existing models by command model --list
  So that I can see what available models I have.


  Scenario: List available models
    Given the user use the modelloader cli tool
    When the user type model --list command
    Then the cli tool print all available models on terminal 
