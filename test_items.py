import time
from selenium.webdriver.common.by import By

def test_add_to_basket_button(browser):
    link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    browser.get(link)
    time.sleep(30)
    message = browser.find_element(By.CSS_SELECTOR, "button.btn-add-to-basket")

    assert message, f'Отсутствует кнопка добавить в корзину'