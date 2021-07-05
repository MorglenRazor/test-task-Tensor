@logging
@capture
Feature: Pictures in yandex

      Scenario: Pictures on Yandex

      Given Open website Yandex 2 "https://yandex.ru/"
      Then The link "https://yandex.ru/images/?utm_source=main_stripe_big" is present on the page
      When Click on link "https://yandex.ru/images/?utm_source=main_stripe_big"
      Then Check that they went to the url "https://yandex.ru/images/"
      When Open first category and check text in the search field is correct
      When Open first pictures
      When Push the forward button
      When Push the back button