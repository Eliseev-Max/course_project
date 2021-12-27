import random
import time
import allure
import pytest
from MainPage import MainPage


@allure.title("Добавление товара в корзину с главной страницы")
@allure.description("Добавляем в корзину товар MacBook нажатием кнопки \"ADD TO CART\" в карточке товара на главной "
                    "странице.\nОжидаем появления сообщения об успешном добавлении в корзину")
@pytest.mark.skip
def test_add_product_to_the_shopping_cart(browser, base_url):
    mp_actions = MainPage(browser)
    mp_actions.go_to_mainpage(base_url)
    add_to_cart = mp_actions.find_all_specified_elements(mp_actions.ADD_TO_CART)
    add_to_cart[1].click()
    mp_actions.wait_web_element(mp_actions.SUCCESS_ALERT)


@allure.title("Удаление товара из корзины")
def test_delete_from_cart(browser, base_url):
    mp_actions = MainPage(browser)
    mp_actions.go_to_mainpage(base_url)
    add_to_cart = mp_actions.find_all_specified_elements(mp_actions.ADD_TO_CART)
    add_to_cart[1].click()
    add_to_cart.wait_web_element(mp_actions.SUCCESS_ALERT)
    mp_actions.wait_web_element(mp_actions.CART_BUTTON).click()
    mp_actions.wait_web_element(mp_actions.REMOVE_FROM_CART_BUTTON).click()
    time.sleep(1)
    assert mp_actions.find_web_element(mp_actions.CART_TOTAL).text == "0 item(s) - $0.00"


@allure.title("Двухкратное нажатие кнопки добавления в корзину")
def test_double_click_add(browser, base_url):
    NUMBER_OF_CLICKS = 2
    mp_actions = MainPage(browser)
    mp_actions.go_to_mainpage(base_url)
    add_to_cart = mp_actions.find_all_specified_elements(mp_actions.ADD_TO_CART)
    price_in_details = mp_actions.find_web_element(mp_actions.PRODUCT_PRICE).text
    price = price_in_details.split("\n")[0]
    num_price = float(price[1::])
    calculated_total_price = NUMBER_OF_CLICKS * num_price
    for i in range(NUMBER_OF_CLICKS):
        add_to_cart[0].click()
        time.sleep(1)
    total_price = mp_actions.get_total_amount_and_price()[1]
    assert calculated_total_price == total_price, "Error in calculating or displaying\
     the total price "


@allure.title("Добавоение в корзину товаров из каталога")
@allure.description("С главной страницы сайта переходим в категорию \"Phones & PDAs\" ")
@pytest.mark.parametrize("index", range(3))
def test_add_to_the_cart_from_catalog(browser, base_url, index):
    customer = MainPage(browser)
    customer.go_to_mainpage(base_url)
    customer.find_web_element(customer.PHONES_AND_PDAS).click()
    time.sleep(0.5)
    customer.find_all_specified_elements(customer.ADD_TO_CART)[index].click()
    customer.wait_web_element(customer.SUCCESS_ALERT)


@allure.title("Добавоение в корзину товара со страницы товара")
def test_add_to_the_cart_from_prod_page(browser, base_url):
    customer = MainPage(browser)
    customer.go_to_mainpage(base_url)
    customer.find_web_element(customer.PHONES_AND_PDAS).click()
    customer.find_all_specified_elements(customer.NAME_OF_PRODUCT)[random.randint(0, 2)].click()
    customer.fill_specified_field(customer.wait_web_element(customer.QTY_FIELD), 1)
    customer.find_web_element(customer.ADD_TO_CART_PRODUCT).click()
    customer.wait_web_element(customer.SUCCESS_ALERT)


@allure.title("Соответствие указанного и отображаемого в корзине количества единиц товара")
def test_set_quantity_of_products(browser, base_url):
    quantity = 3
    customer = MainPage(browser)
    customer.go_to_mainpage(base_url)
    customer.find_web_element(customer.PHONES_AND_PDAS).click()
    customer.find_all_specified_elements(customer.NAME_OF_PRODUCT)[random.randint(0, 2)].click()
    customer.fill_specified_field(customer.wait_web_element(customer.QTY_FIELD), quantity)
    customer.find_web_element(customer.ADD_TO_CART_PRODUCT).click()
    time.sleep(1)
    amount = customer.get_total_amount_and_price()[0]
    assert quantity == amount, "Количество единиц выбранного товара не совпадает с количеством единиц товара в корзине"
