Feature: Search
    Search Google and Yahoo

@Smoke
Scenario: Search Google
    Given Open Google Search Page
    When I do search
    And I click Result


@search
Scenario: Search Yahoo
    Given Open Yahoo Search Page
