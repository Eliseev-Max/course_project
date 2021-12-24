import time
import allure
import pytest
from MainPage import MainPage


# @allure.title("Добавление товара в корзину с главной страницы")
# @allure.description("Добавляем в корзину товар MacBook нажатием кнопки \"ADD TO CART\" в карточке товара на главной "
#                     "странице.\nОжидаем появления сообщения об успешном добавлении в корзину")
# def test_add_product_to_the_shopping_cart(browser, base_url):
#     mp_actions = MainPage(browser)
#     mp_actions.go_to_mainpage(base_url)
#     add_to_cart = mp_actions.find_all_specified_elements(mp_actions.ADD_TO_CART)
#     add_to_cart[1].click()
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
    total_price = mp_actions.wait_web_element(mp_actions.CART_TOTAL).text.split(" - ")[1]
    num_total_price = float(total_price[1::].replace(",", ""))
    assert calculated_total_price == num_total_price, "Error in calculating or displaying the total price "

#
# @allure.title("НазваниеТеста")
# @pytest.mark.skip
# def test_name03(browser, base_url):
#     pass
