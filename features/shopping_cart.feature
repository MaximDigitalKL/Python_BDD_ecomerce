Feature: Check the functionality of the shopping cart

  Background:
    Given Navigate to items page

  @Shopping
  Scenario: Adding one item to the shopping cart
    When We add one item to shopping cart
    Then Count of items in shopping cart is one

  @Shopping
  Scenario: Adding multiple items to the shopping cart
    When I add multiple items to shopping cart
    Then There are multiple items in shopping cart

  @Shopping
  Scenario: I want to remove an item from the shopping cart
    When I add multiple items to shopping cart
    When I change my mind regarding an item, I navigate to shopping cart page
    Then I remove one item from the shopping cart and shopping cart  displays one less item

  @Shopping
  Scenario: Edit one item from the shopping cart
    When We add one item to shopping cart
    When I change my mind regarding an item, I navigate to shopping cart page
    Then I edit one item details