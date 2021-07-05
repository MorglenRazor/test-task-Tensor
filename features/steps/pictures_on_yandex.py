import logging
import sys
import time

from behave import *

from features.environment import page_object

logging.basicConfig(filename='log', filemode='w', format='%(name)s - %(levelname)s - %(message)s')


@given('Open website Yandex 2 "{url}"')
def step(context, url):
    # Отрывает станицу "yandex.ru"
    page_object.open_page(context, url)


@then('The link "{url}" is present on the page')
def step(context, url):
    # Ищем элемент "Картинки"
    element = page_object.find_href_element(context, url)
    # Проверем если он есть, логируем это, если нет прекращаем тест
    if element:
        logging.info("Element 'Pictures' theres is on page")
    else:
        logging.info("Element 'Pictures' theres is't on page")
        sys.exit(1)


@When('Click on link "{url}"')
def step(context, url):
    element = page_object.find_href_element(context, url)
    element.click()
    time.sleep(5)


@Then('Check that they went to the url "{url}"')
def step(context, url):
    # Запоминаем id страницы
    new_id_page = context.browser.window_handles
    # Переходим на новою страницу
    context.browser.switch_to.window(new_id_page[1])
    # Получаем текущий URL
    current_url = context.browser.current_url
    # Проверяем известный нам URl с нашим текущим
    assert url in current_url, "The current url {} is not equal to the desired one url {}".format(current_url, url)
    logging.info("The current url {} is equal to the desired one url {}".format(current_url, url))


@When("Open first category and check text in the search field is correct")
def step(context):
    name_category_pictures = page_object.xpath_name_category_picture
    element = page_object.find_element(context, name_category_pictures)
    # Получаем название категории
    name_category = element.text
    element.click()
    time.sleep(5)
    # Получаем название из поиска
    title_yandex = context.browser.title
    # Проверяем что категории совпадают
    assert name_category in title_yandex, "Text {} in the search field is not correct".format(name_category)
    logging.info("Text {} in the search field is correct".format(name_category))


@When("Open first pictures")
def step(context):
    # Находим первую картинку
    element = page_object.search_field_yandex(context, xpath='//a[contains(@class, "serp-item__link")]')
    # Запоминаем текущий url
    element_link = context.browser.current_url
    element.click()
    time.sleep(5)
    # Запоминаем текущий url и делаем его гланым
    page_object.main_yandex_pictures = context.browser.current_url
    # Проверяем что картинка открылась, проверяя что она не равна предыдущему URL
    assert element_link != page_object.main_yandex_pictures, "One Pictures is't open"
    logging.info("One Pictures is open ")


@When("Push the forward button")
def step(context):
    xpath_forward_btn = '/html/body/div[14]/div[1]/div/div/div[3]/div/div[2]/div[1]/div[4]'
    time.sleep(4)
    # Ищем кнопку вперед
    element = page_object.find_element(context, xpath_forward_btn)
    time.sleep(4)
    # Нажимем на нее
    element.click()
    time.sleep(4)
    # Запоминаем Url новой картинки
    current_yandex_link = context.browser.current_url
    # Проверяем что url новой картинки не равен url первой картинки
    assert current_yandex_link != page_object.main_yandex_pictures, "Pictures is't changed"
    logging.info("Pictures changed")


@When("Push the back button")
def step(context):
    xpath_back_btn = '/html/body/div[14]/div[1]/div/div/div[3]/div/div[2]/div[1]/div[1]'
    context.browser.implicitly_wait(10)
    time.sleep(4)
    # Ищем кнопку назад
    element = page_object.find_element(context, xpath_back_btn)
    time.sleep(4)
    # Нажмаем на нее
    element.click()
    time.sleep(5)
    # Запоминаем url первой картинки
    current_yandex_link = context.browser.current_url
    # Проверяем что url главной картинки ссопадает с url который открылся
    assert page_object.main_yandex_pictures == current_yandex_link, "not the same image"
    logging.info("The same image")
