Feature: Verify placing an order works and discount is applied

  Background:
    Given The user navigates to main page

  @Order
  Scenario: Placing an order without having an account
    When He searches for a desired item "Lando Gym Jacket"
    When He adds the item to the shopping cart
    When He proceeds to checkout
    When He fills in all the required details "qwer@qwe.com","petru","maior","lalelelor","Denver","Colorado","12345","United States","12345432"
    When He places the order
    Then The order is placed, success message "Your order # is:"

  @Order
  Scenario: Logging in and placing an order
    When The user logs into his account email "matilda2@bravo.com" password "Calcumanere@1"
    When He searches for a desired item "Lando Gym Jacket"
    When He adds the item to the shopping cart
    When He proceeds to checkout
    When He fills in the shipping details
    When He places the order
    Then The order is placed, success message "Your order number is:"

  @Order
  Scenario: Check Discount is applied correctly
    When The user logs into his account email "matilda2@bravo.com" password "Calcumanere@1"
    When He searches for a desired item "Lando Gym Jacket"
    When He adds the item to the shopping cart
    When He edits the quantity of the item
    Then The discount is correctly calculated


