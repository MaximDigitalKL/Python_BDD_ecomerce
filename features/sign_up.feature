Feature: Verify the create account functionality

  Background:
    Given I navigate to the create account page

  @Account
  Scenario Outline: Create an account filling in all the correct parameters
    When I fill in the form "<first_name>","<last_name>","<email>","<password>","<confirm_password>"
    Then I receive success message "<success_message>"
    Examples:
      | first_name | last_name   | email               | password      | confirm_password | success_message                                            |
      | Matilda    | Ianos_Bravo | matilda11@bravo.com | Calcumanere@1 | Calcumanere@1    | My Account |

  @Account
  Scenario Outline: Trying to creat an account without filling in all required fields
    When The user fills in the form "<first_name>","<last_name>","<email>","<password>","<confirm_password>"
    Then I receive error message "<error_message>"
    Examples:
      | first_name | last_name | email           | password     | confirm_password | error_message             |
      |    N/A     | petre     | test@auto.com   | Qwerty1234   | Qwerty1234       |  This is a required field.|
      |   tutuca   |  N/A      | test@auto.com   | Qwerty1234   | Qwerty1234       |  This is a required field.|
      |   tutuca   | petre     |    N/A          | Qwerty1234   | Qwerty1234       |  This is a required field.|
      |   tutuca   | petre     | test@auto.com   |   N/A        | Qwerty1234       |  This is a required field.|
      |   tutuca   | petre     | test@auto.com   | Qwerty1234   |    N/A           |  This is a required field.|
      |   tutuca   | petre     | test.auto.io    | Qwerty1234   | Qwerty1234       |  Please enter a valid email address |
      |   tutuca   | petre     | test@auto.com   | qwertyui     | qwertyui         |  Minimum of different classes of characters in password is 3.|
      |   tutuca   | petre     | test@auto.com   | qwertyu2     | qwertyu2         |  Minimum of different classes of characters in password is 3.|
      |   tutuca   | petre     | test@auto.com   | Qwertyu2     | Qwetyu2          |  Please enter the same value again.|
      |   tutuca   | petre     | test@auto.com   | Qwe1234      | Qwe1234          |  Minimum length of this field must be equal or greater than 8 symbols.|
      |   M@rius   | petre     | test@auto.com   | Qwerty1234   | Qwerty1234       |  First Name is not valid! |
      |   M4rius   | petre     | test40@auto.com | Qwerty1234   | Qwerty1234       |  First Name is not valid! |
      |   M        | petre     | test41@auto.com | Qwerty1234   | Qwerty1234       |  First Name is not valid! |
      | Qwertyuiopasdfghjklzxcvbnmqwertyuiopasdfghjklzxcvb| petre|  test42@auto.com| Qwerty1234| Qwerty1234| First Name is not valid! |





