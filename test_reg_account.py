import allure
import pytest
from UserLoginPage import UserLoginPage


@allure.title("Создание нового пользователя")
@allure.description("Позитивный тест создания нового пользователя."
                    "По завершении теста должна появиться надпись \"Your Account Has Been Created!\"")
def test_create_new_user(browser, base_url):
    new_user = UserLoginPage(browser)
    new_user.open_reg_account_page(base_url)
    new_user.form_autocomplete()
    new_user.find_web_element(new_user.PRIVACY_POLICY_CHECKBOX).click()
    new_user.wait_and_click(new_user.SUBMIT_CONTINUE_BUTTON)
    if new_user.view_success_notification() != "Your Account Has Been Created!":
        browser.save_screenshot(new_user.screenshot_name)
        new_user.logger.error("Account creation message was not displayed ")
        raise AssertionError("No message")


@allure.title("Отправка пустой формы")
@allure.description("Попытка отправки незаполненной формы регистрации пользователя."
                    "При нажатии кнопки Continue должно появиться сообщение об ошибке")
def test_send_empty_form(browser, base_url):
    form_filling = UserLoginPage(browser)
    form_filling.open_reg_account_page(base_url)
    form_filling.wait_and_click(form_filling.SUBMIT_CONTINUE_BUTTON)
    form_filling.wait_web_element(form_filling.WARNING_ALERT)


@allure.title("Отправка пустой формы с установленным в чекбоксе флагом")
@allure.description("Попытка отправки незаполненной формы регистрации пользователя с установленным в чекбоксе\
 \"I have read and agree to the Privacy Policy\" флагом."
"При нажатии кнопки Continue под полями ввода должны появиться сообщения об ошибке")
def test_send_empty_form_with_checkbox_on(browser, base_url):
    form_filling = UserLoginPage(browser)
    form_filling.open_reg_account_page(base_url)
    form_filling.find_web_element(form_filling.PRIVACY_POLICY_CHECKBOX).click()
    form_filling.wait_and_click(form_filling.SUBMIT_CONTINUE_BUTTON)
    assert len(form_filling.find_all_specified_elements(form_filling.INPUT_FIELD_ERROR)) == 5, "Not all warnings \
    about incorrect filling of fields appeared "

@allure.title("Проверка допустимого количества символов в полях ввода")
@allure.description("Проверка граничных условий полей для ввода имени и фамилии")
@pytest.mark.parametrize("first_name",[UserLoginPage.generate_string(num_of_chars=1),
                                       UserLoginPage.generate_string(num_of_chars=32, num=True, uppercase=True)])
@pytest.mark.parametrize("last_name",[UserLoginPage.generate_string(num_of_chars=1),
                                       UserLoginPage.generate_string(num_of_chars=32, num=True, uppercase=True)])
def test_border_conditions(browser, base_url, first_name, last_name):
    new_user = UserLoginPage(browser)
    new_user.open_reg_account_page(base_url)
    new_user.fill_in_with_letters(new_user.FIRST_NAME_FIELD, name=first_name)
    new_user.fill_in_with_letters(new_user.LAST_NAME_FIELD, name=last_name)
    new_user.enter_email()
    new_user.enter_telephone()
    new_user.enter_and_confirm_password()
    new_user.find_web_element(new_user.PRIVACY_POLICY_CHECKBOX).click()
    new_user.wait_and_click(new_user.SUBMIT_CONTINUE_BUTTON)
    if new_user.view_success_notification() != "Your Account Has Been Created!":
        browser.save_screenshot(new_user.screenshot_name)
        new_user.logger.error("Account creation message was not displayed ")
        raise AssertionError("No message")


@allure.title("Проверка недопустимого количества символов в полях ввода")
@allure.description("Ввод символов в поля для имени и фамилии в количестве, превышающем верхний порог")
@pytest.mark.parametrize("name_field", [1, 2])
def test_exceeding_character_value(browser, base_url, name_field):
    new_user = UserLoginPage(browser)
    new_user.open_reg_account_page(base_url)
    first_name = None
    last_name = None
    if name_field == 1:
        first_name = new_user.generate_string(num_of_chars=33, uppercase=True)
    if name_field == 2:
        last_name = new_user.generate_string(num_of_chars=33, uppercase=True)
    new_user.fill_in_with_letters(new_user.FIRST_NAME_FIELD, name=first_name)
    new_user.fill_in_with_letters(new_user.LAST_NAME_FIELD, name=last_name)
    new_user.enter_email()
    new_user.enter_telephone()
    new_user.enter_and_confirm_password()
    new_user.find_web_element(new_user.PRIVACY_POLICY_CHECKBOX).click()
    new_user.wait_and_click(new_user.SUBMIT_CONTINUE_BUTTON)
    new_user.wait_web_element(new_user.INPUT_FIELD_ERROR)


@pytest.mark.parametrize("confirmation", ["", "123456"])
def test_no_confirm_password(browser, base_url, confirmation):
    PASSWORD = "qwerty"
    WARNING_TEXT = "Password confirmation does not match password!"
    new_user = UserLoginPage(browser)
    new_user.open_reg_account_page(base_url)
    new_user.fill_in_with_letters(new_user.FIRST_NAME_FIELD)
    new_user.fill_in_with_letters(new_user.LAST_NAME_FIELD)
    new_user.enter_email()
    new_user.enter_telephone()
    new_user.enter_password(pwd=PASSWORD)
    new_user.fill_in_with_letters(new_user.PASSWORD_CONFIRM_FIELD, name=confirmation)
    new_user.find_web_element(new_user.PRIVACY_POLICY_CHECKBOX).click()
    new_user.wait_and_click(new_user.SUBMIT_CONTINUE_BUTTON)
    assert new_user.wait_web_element(new_user.INPUT_FIELD_ERROR).text == WARNING_TEXT, "Invalid warning message"


def test_email_without_domain(browser, base_url):
    WARNING_TEXT = "E-Mail Address does not appear to be valid!"
    new_user = UserLoginPage(browser)
    new_user.open_reg_account_page(base_url)
    new_user.fill_in_with_letters(new_user.FIRST_NAME_FIELD)
    new_user.fill_in_with_letters(new_user.LAST_NAME_FIELD)
    new_user.enter_email(email="test@mail")
    new_user.enter_telephone()
    new_user.enter_and_confirm_password()
    new_user.find_web_element(new_user.PRIVACY_POLICY_CHECKBOX).click()
    new_user.wait_and_click(new_user.SUBMIT_CONTINUE_BUTTON)
    assert new_user.wait_web_element(new_user.INPUT_FIELD_ERROR).text == WARNING_TEXT, "Invalid warning message"
