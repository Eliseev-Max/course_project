import allure
from UserLoginPage import UserLoginPage


@allure.title("Создание нового пользователя")
@allure.description("Позитивный тест создания нового пользователя."
                    "По завершении теста должна появиться надпись \"Your Account Has Been Created!\"")
def test_create_new_user(browser, base_url):
    new_user = UserLoginPage(browser)
    new_user.open_reg_account_page(base_url)
    new_user.enter_first_and_last_name()
    new_user.enter_all_fields()
    new_user.find_web_element(new_user.PRIVACY_POLICY_CHECKBOX).click()
    new_user.wait_and_click(new_user.SUBMIT_CONTINUE_BUTTON)
    if new_user.view_success_notification() != "Your Account Has Been Created!":
        browser.save_screenshot(new_user.screenshot_name)
        new_user.logger.error("Account creation message was not displayed ")
        raise AssertionError