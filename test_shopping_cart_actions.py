import time
import allure
import pytest
from MainPage import MainPage
from ShoppingCart import ShoppingCart

# /index.php?route=checkout/cart    - not logged in
#

@allure.title("Переход в пустую корзину")
@allure.description("Переходим в пустую корзину по нажатию кнопки \"Shopping Cart\"")
def test_go_to_empty_shopping_cart(browser, base_url):
    cart = MainPage(browser)
    cart.go_to_mainpage(base_url)
    cart.find_web_element(cart.SHOPPING_CART_REFERENCE).click()
    assert cart.wait_web_element(cart.SHOPPING_CART_PROMPT).text == cart.EMPTY_CART_TEXT


@allure.title("Переход в корзину при нажатии на ссылку View Cart")
@allure.description("")
def test_click_on_view_cart(browser, base_url):
    customer = MainPage(browser)
    customer.go_to_mainpage(base_url)
    customer.find_all_specified_elements(customer.ADD_TO_CART)[1].click()
    time.sleep(0.5)
    customer.wait_web_element(customer.CART_BUTTON).click()
    customer.find_web_element(customer.VIEW_CART).click()
    customer.wait_web_element(customer.TABLE_OF_PRODUCTS)



@allure.title("Проверка изменения количества товаров в корзине")
@allure.description("Изменяем количество товаров в корзине и после нажатия кнопки \"Update\" проверяем \
                    появление сообщения об успешно выполненном изменении количества единиц товара")
def test_update_quantity(browser, base_url):
    cart = ShoppingCart(browser)
    cart.go_to_mainpage(base_url)
    cart.add_product_to_cart()
    cart.go_to_shopping_cart(base_url)
    quantity = cart.wait_web_element(cart.INPUT_QUANTITY)
    quantity.clear()
    quantity.send_keys(3)
    cart.find_web_element(cart.UPDATE_QUANTITY_BUTTON).click()
    cart.wait_web_element(cart.SUCCESS_ALERT)


@allure.title("Задать количество товаров равным нулю")
@allure.description("")
def test_set_quantity_in_zero(browser, base_url):
    cart = ShoppingCart(browser)
    cart.go_to_mainpage(base_url)
    cart.add_product_to_cart()
    cart.go_to_shopping_cart(base_url)
    quantity = cart.wait_web_element(cart.INPUT_QUANTITY)
    quantity.clear()
    quantity.send_keys(0)
    cart.find_web_element(cart.UPDATE_QUANTITY_BUTTON).click()
    assert cart.wait_web_element(cart.SHOPPING_CART_PROMPT).text == cart.EMPTY_CART_TEXT


@allure.title("Удаление товара из корзины")
@allure.description("Проверка удаления товара из корзины нажатием кнопки Remove")
@pytest.mark.skip
def test_remove_product_from_cart(browser, base_url):
    cart = ShoppingCart(browser)
    cart.go_to_mainpage(base_url)
    cart.add_product_to_cart()
    cart.go_to_shopping_cart(base_url)
    cart.wait_web_element(cart.SHOPPING_CART_REMOVE_BUTTON)
    assert cart.wait_web_element(cart.SHOPPING_CART_PROMPT).text == cart.EMPTY_CART_TEXT


@allure.title("")
@allure.description("")
def test_continue_shopping(browser, base_url):
    cart = ShoppingCart(browser)
    cart.go_to_mainpage(base_url)
    cart.add_product_to_cart()
    cart.go_to_shopping_cart(base_url)
    cart.wait_web_element(cart.CONTINUE_SHOPPING).click()
    assert browser.current_url == base_url + "index.php?route=common/home"


@allure.title("")
@allure.description("")
@pytest.mark.skip
def test_too_many_products(browser, base_url):
    pass
