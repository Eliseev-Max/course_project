import time
from BaseClass import BaseClass


class ShoppingCart(BaseClass):

    def go_to_shopping_cart(self, url):
        self.logger.info("Go to the Shopping Cart by URL: {}".format(url + self.SHOPPING_CART_URL))
        self.browser.get(url + self.SHOPPING_CART_URL)
        return self

    def add_product_to_cart(self, prod=0, qty=1):
        for i in range(qty):
            self.find_all_specified_elements(self.ADD_TO_CART)[prod].click()
            time.sleep(0.5)

