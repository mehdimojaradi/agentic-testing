    Scenario: Validate email address for a user
        Given I have a user with username 'Antonette'
        When I want to validate his email address
        Then I should receive "Shanna@melissa.tv"