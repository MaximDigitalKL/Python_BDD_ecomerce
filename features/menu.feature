Feature: Check the functionality of menu buttons on the menu page

  Background:
    Given I navigate to the menu page

  #-----------------------------What's New category----------------------------
    @Menu
    Scenario Outline: User wants to navigate to news pages
      When User selects the "<main_page_button>" button
      Then I am redirected to new page "<expected_url>"
      Examples:
        | main_page_button | expected_url                                                         |
        | what_is_new      | https://magento.softwaretestingboard.com/what-is-new.html            |
        | sale             | https://magento.softwaretestingboard.com/sale.html                   |
        | training         | https://magento.softwaretestingboard.com/training/training-video.html|

   #---------------------------Women/Men Category------------------------------------
    @Menu
    Scenario Outline: User wants to navigate clothing articles
      When I select the "<menu_item>" "<submenu>" "<product_category>" button
      Then I am redirected to new page "<expected_url>"
      Examples:
        | menu_item |submenu  | product_category     | expected_url |
        | Women     | Tops    | jackets_w            | https://magento.softwaretestingboard.com/women/tops-women/jackets-women.html                |
        | Women     | Tops    | hoodies_w            | https://magento.softwaretestingboard.com/women/tops-women/hoodies-and-sweatshirts-women.html|
        | Women     | Tops    | tees_w               | https://magento.softwaretestingboard.com/women/tops-women/tees-women.html                   |
        | Women     | Tops    | tanks_w              | https://magento.softwaretestingboard.com/women/tops-women/tanks-women.html                  |
        | Women     | Bottom  | pants_w              | https://magento.softwaretestingboard.com/women/bottoms-women/pants-women.html               |
        | Women     | Bottom  | shorts_w             | https://magento.softwaretestingboard.com/women/bottoms-women/shorts-women.html              |
        | Men       | Tops    | jackets_m            | https://magento.softwaretestingboard.com/men/tops-men/jackets-men.html                      |
        | Men       | Tops    | hoodies_m            | https://magento.softwaretestingboard.com/men/tops-men/hoodies-and-sweatshirts-men.html      |
        | Men       | Tops    | tees_m               | https://magento.softwaretestingboard.com/men/tops-men/tees-men.html                         |
        | Men       | Tops    | tanks_m              | https://magento.softwaretestingboard.com/men/tops-men/tanks-men.html                        |
        | Men       | Bottom  | pants_m              | https://magento.softwaretestingboard.com/men/bottoms-men/pants-men.html                     |
        | Men       | Bottom  | shorts_m             | https://magento.softwaretestingboard.com/men/bottoms-men/shorts-men.html                    |



  #--------------------------------------Additional_Categories-----------------------------------------------------
    @Menu
    Scenario Outline: User wants to navigate to extra articles
      When User decides to look for "<article_ctg>"
      Then I am redirected to new page "<expected_url>"
      Examples:
        | article_ctg | expected_url                                                        |
        | bags        | https://magento.softwaretestingboard.com/gear/bags.html             |
        | fitness_eqp | https://magento.softwaretestingboard.com/gear/fitness-equipment.html|
        | watches     | https://magento.softwaretestingboard.com/gear/watches.html          |



