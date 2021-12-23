import time
import allure
import pytest
from MainPage import MainPage

CURRENCY = dict({"USD": "$", "EUR": "€", "GBP": "£"})
CURRENCY_LIST = list(CURRENCY.keys())

#
# @allure.title("Проверка смены знака валюты у товаров")
# def test_check_sign_with_changing_currency(browser, base_url):
#     """ Проверяем смену знака валюты у товаров при смене валюты в хедере главной страницы """
#     main_page = MainPage(browser)
#     main_page.go_to_mainpage(base_url)
#     for cur in CURRENCY_LIST:
#         main_page.choose_currency(cur)
#
#         if main_page.find_web_element(main_page.CURRENCY_SIGN).text != CURRENCY[cur]:
#             main_page.find_web_element(main_page.CURRENCY_SIGN).screenshot("./screenshot/currency_sign.png")
#             browser.save_screenshot(main_page.screenshot_name)
#             main_page.logger.error("The currency sign in the prices of products does not match the selected one")
#             raise AssertionError
#         time.sleep(1)
#
#
# @allure.title("Проверка смены денежного выражения цены товаров при смене валюты")
# def test_currency_of_product_price(browser, base_url):
#     """ Проверяем смену денежного выражения цены избранных товаров при смене валюты """
#     main_page = MainPage(browser)
#     main_page.go_to_mainpage(base_url)
#     for cur in CURRENCY_LIST:
#         main_page.choose_currency(cur)
#         prod_list = main_page.find_all_specified_elements(MainPage.PRODUCT_PRICE)
#         for price in prod_list:
#             assert CURRENCY[cur] in price.text
#         time.sleep(1)

#
# @allure.title("Добавление товара в корзину с главной страницы")
# @allure.description("Добавляем в корзину товар MacBook нажатием кнопки \"ADD TO CART\" в карточке товара на главной "
#                     "странице.\nОжидаем появления сообщения об успешном добавлении в корзину")
# def test_add_product_to_the_shopping_cart(browser, base_url):
#     mp_actions = MainPage(browser)
#     mp_actions.go_to_mainpage(base_url)
#     add_to_cart = mp_actions.find_all_specified_elements(mp_actions.ADD_TO_CART)
#     add_to_cart[0].click()
#     mp_actions.wait_web_element(mp_actions.SUCCESS_ALERT)


@allure.title("Удаление товара из корзины")
def test_delete_from_cart(browser, base_url):
    mp_actions = MainPage(browser)
    mp_actions.go_to_mainpage(base_url)
    add_to_cart = mp_actions.find_all_specified_elements(mp_actions.ADD_TO_CART)
    add_to_cart[1].click()
    mp_actions.wait_web_element(mp_actions.CART_BUTTON).click()
    mp_actions.wait_web_element(mp_actions.REMOVE_FROM_CART_BUTTON).click()
    time.sleep(1)
    assert mp_actions.find_web_element(mp_actions.CART_TOTAL).text == "0 item(s) - $0.00"


@allure.title("Двойное нажатие кнопки добавления в корзину")
def test_double_click_add(browser, base_url):
    NUMBER_OF_CLICKS = 3
    mp_actions = MainPage(browser)
    mp_actions.go_to_mainpage(base_url)
    # add_to_cart = mp_actions.find_all_specified_elements(mp_actions.ADD_TO_CART)
    # for i in range(NUMBER_OF_CLICKS):
    #     add_to_cart[0].click()
    print(mp_actions.find_web_element(mp_actions.PRODUCT_PRICE).text)


#
#
# @allure.title("НазваниеТеста")
# @pytest.mark.skip
# def test_name03(browser, base_url):
#     pass
