from BaseClass import BaseClass


class MainPage(BaseClass):

    def go_to_mainpage(self, url):
        self.logger.info("Opening source: {}".format(url))
        self.browser.get(url)
        return self

    def choose_currency(self, currency):
        currency_designations = ["USD", "EUR", "GBP"]
        self.logger.info('Choosing currency: {}'.format(currency))
        self.find_web_element(self.CURRENCY).click()

        if currency.upper() not in currency_designations:
            self.logger.error('{} is not among the available currencies'.format(currency))
            print(f"Указанная валюта {currency} отсутствует в перечне доступных")
            return None
        elif currency.upper() == currency_designations[1]:
            self.find_web_element(self.EURO).click()
        elif currency.upper() == currency_designations[2]:
            self.find_web_element(self.POUND_STERLING).click()
        else:
            self.find_web_element(self.US_DOLLAR).click()


    def get_total_amount_and_price(self):
        button_label = self.find_web_element(self.CART_TOTAL)
        button_label_list = button_label.text.split(" - ")
        total_amount = int(button_label_list[0].rstrip(" item(s)"))
        total_price = float(button_label_list[1][1::].replace(",", ""))
        total = (total_amount, total_price)
        return total
