@logging
@capture
Feature: Search in yandex

    Scenario: Check will find the Yandex site "Tenzor"

      Given Open website Yandex 1 "https://yandex.ru/"
      Then Check for the presence of a search field
      When Search for "Тензор"
      Then Check table with suggest
      Then Check that in the first five results, there is "tensor.ru"


