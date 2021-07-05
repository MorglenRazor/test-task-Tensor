import logging

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Page_object:
    field_search = None
    main_yandex_pictures = None
    xpath_yandex_search_field = '//input[contains(@class, "input__control input__input mini-suggest__input")]'
    xpath_name_category_picture = '//div[contains(@class, "PopularRequestList-SearchText")]'

    @staticmethod
    def open_page(context, url):
        logging.info('Start testing...')
        context.browser.maximize_window()
        context.browser.get(url)

    @staticmethod
    def search_field_yandex(context, xpath):
        element = WebDriverWait(context.browser, 120).until(
            EC.element_to_be_clickable(
                (By.XPATH, xpath))
        )
        return element

    @staticmethod
    def find_href_element(context, text):
        xpath_find_link = '//a[contains(@href, "{}")]'.format(text)
        element = context.browser.find_element_by_xpath('{}'.format(xpath_find_link))
        return element

    @staticmethod
    def find_element(context, xpath):
        element = context.browser.find_element_by_xpath('{}'.format(xpath))
        return element
