import logging
import sys
import time

from behave import *
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from selenium.webdriver.common.keys import Keys

from features.environment import page_object

logging.basicConfig(filename='log', filemode='w', format='%(name)s - %(levelname)s - %(message)s')


@given('Open website Yandex 1 "{url}"')
def step(context, url):
    page_object.open_page(context, url)


@then("Check for the presence of a search field")
def step(context):
    try:
        # Пытаемся найти поле поиска Яндекс
        # И запоминаем этот элемент
        page_object.field_search = page_object.search_field_yandex(context, page_object.xpath_yandex_search_field)
        logging.info('Field is find')
    except TimeoutException:
        # Если не нашли, логируем это и завершаем тест
        logging.info("Field is finded't")
        logging.info("Stop test...")
        assert False, "The test is stopped. Search field not found"


@when('Search for "{text}"')
def step(context, text):
    time.sleep(5)
    # Вводим в поле поиска текст "Тензор"
    page_object.field_search.send_keys(text)
    logging.info('Input "Tensor" in field search')


@then('Check table with suggest')
def step(context):
    # Нажимаем кнопку вниз
    page_object.field_search.send_keys(Keys.ARROW_DOWN)
    # Проверяем что появился атрибут отвкчающий за подсказки
    check_attribute = page_object.field_search.get_attribute('aria-activedescendant')
    # Если атрибута нет, то заканчиваем тест
    if check_attribute:
        logging.info("appeared suggest's")
        page_object.field_search.submit()
    else:
        logging.info("Not appeared suggest's")
        assert False, "Suggest's did not appear. stop test"


@then('Check that in the first five results, there is "{text}"')
def step(context, text):
    time.sleep(10)
    # Ищем найденые элементы
    elements = context.browser.find_elements_by_xpath('//li[contains(@class, "serp-item")]')
    # Проходим по элементам
    for elem in elements:
        # Задаем условие что искомый сайт должен быть в первых 5-и выборках
        if int(elem.get_attribute('data-cid')) != 5:
            try:
                # Ищем искомый сайт "tensor.ru"
                page_object.find_element(context, '//a[contains(@href, "{}")]'.format(text))
            except NoSuchElementException:
                # Не нахлдим заканчиваем тест
                logging.info("Site {} there is't in first five result".format(text))
                assert False, "Site 'tensor.ru' there is't in first five result"
    logging.info('Site {} there is in first five result'.format(text))
