Feature: Observer Pattern
  As a news system developer
  I want to use Observer pattern
  To notify subscribers about news

  Scenario: Subscribe to news
    Given a news publisher is created
    And an email subscriber with address "user@example.com" is created
    When the subscriber subscribes to the publisher
    Then the subscriber should be in publisher's subscribers list

  Scenario: Receive news notification
    Given a news publisher is created
    And an email subscriber with address "user@example.com" is created
    And the subscriber subscribes to the publisher
    When the publisher publishes news "Important update"
    Then the subscriber should receive notification with "Important update"
