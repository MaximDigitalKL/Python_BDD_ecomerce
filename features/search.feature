Feature: Check the functionality of the search button

  Background:
    Given I navigate to search page

    @Search
    Scenario: User wants to search for generic item
      When I search for generic item "hoodie"
      Then I receive a list of items

    @Search
    Scenario: User wants to search for specific item
      When I search for specific item "Oslo Trek Hoodie"
      Then First item in result list is "Oslo Trek Hoodie"

    @Search
    Scenario: User wants to search for non-existing item
      When I search for non existing item "cartofi prajiti"
      Then I receive appropriate error message "Your search returned no results."