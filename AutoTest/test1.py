from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time
import pytest
from webdriver_manager.chrome import ChromeDriverManager
import data
import requests

link = "https://b2c.passport.rt.ru"
link2 = 'https://b2c.passport.rt.ru/auth/realms/b2c/login-actions/registration?client_id=lk_b2c&tab_id=NHQTQsIU5VI'
browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()))


class Test_Rostelecom:
    browser.get(link)

    def test1(self):
        time.sleep(5)
        url = browser.current_url
        print(url)
        assert requests.head(url).status_code == 200, 'Сайт не загружен '

    def test2(self):
        browser.implicitly_wait(10)
        assert len(browser.find_elements(By.TAG_NAME, 'section')) == 2, 'Количество блоков на странице не равно 2'

    def test3(self):
        browser.implicitly_wait(10)
        browser.find_element(By.CSS_SELECTOR, '#t-btn-tab-mail').click()
        browser.find_element(By.CSS_SELECTOR, '#username').send_keys(data.Login)
        browser.find_element(By.CSS_SELECTOR, '#password').send_keys(data.Password)
        browser.find_element(By.CSS_SELECTOR, '#kc-login').click()
        time.sleep(5)
        assert browser.find_element(By.CSS_SELECTOR, '#lk-btn').text == 'Личный кабинет', 'Авторизация не прошла'
        browser.find_element(By.CSS_SELECTOR, '#logout-btn').click()

    def test4(self):
        browser.implicitly_wait(10)
        browser.find_element(By.CSS_SELECTOR, '#forgot_password').click()
        assert browser.find_element(By.TAG_NAME, 'h1').text == 'Восстановление пароля'
        browser.find_element(By.CSS_SELECTOR, '#reset-back').click()

    def test5(self):
        browser.find_element(By.CSS_SELECTOR, '#t-btn-tab-mail').click()
        browser.find_element(By.CSS_SELECTOR, '#username').send_keys(data.Login)
        browser.find_element(By.CSS_SELECTOR, '#password').send_keys('123123123s')
        browser.find_element(By.CSS_SELECTOR, '#kc-login').click()
        time.sleep(3)
        assert browser.find_element(By.CSS_SELECTOR, '#form-error-message').text == 'Неверный логин или пароль'

    def test6(self):
        browser.implicitly_wait(10)
        assert browser.find_element(By.LINK_TEXT, 'пользовательского соглашения').text == 'пользовательского соглашения'

    def test7(self):
        browser.implicitly_wait(10)
        browser.find_element(By.CSS_SELECTOR, '#t-btn-tab-phone').click()  # telephone
        browser.find_element(By.CSS_SELECTOR, '#username').send_keys(data.rand)
        browser.find_element(By.CSS_SELECTOR, '#password').click()
        assert browser.find_element(By.CSS_SELECTOR,'main.app-container:nth-child(2) div.card-container.login-form-container div.card-container__wrapper div.card-container__content form.login-form div.tabs-input-container div.rt-input-container.tabs-input-container__login:nth-child(3) div.rt-input.rt-input--rounded.rt-input--orange > span.rt-input__placeholder.rt-input__placeholder--top').text == 'Логин'
        time.sleep(0.5)
        browser.find_element(By.CSS_SELECTOR, '#username').clear()

    def test8(self):
        browser.implicitly_wait(10)
        browser.find_element(By.CSS_SELECTOR, '#username').send_keys(data.Login)
        browser.find_element(By.CSS_SELECTOR, '#password').send_keys('6543Атогнпенпе')
        browser.find_element(By.CSS_SELECTOR, '#kc-login').click()
        assert browser.find_element(By.CSS_SELECTOR,'#form-error-message').text == 'Введите данные на английском языке', 'Сайт не вывел предупреждение о кириллице'

    def test9(self):
        browser.implicitly_wait(10)
        browser.find_element(By.CSS_SELECTOR, '#kc-register').click()
        browser.find_element(By.CSS_SELECTOR,'#page-right > div > div > div > form > div.name-container > div:nth-child(1) > div > input').send_keys('Влад')
        browser.find_element(By.CSS_SELECTOR,'#page-right > div > div > div > form > div.name-container > div:nth-child(2) > div > input').send_keys('Влад')
        browser.find_element(By.CSS_SELECTOR, '#address').send_keys(data.Login)
        browser.find_element(By.CSS_SELECTOR, '#password').send_keys(data.Password)
        browser.find_element(By.CSS_SELECTOR, '#password-confirm').send_keys(data.Password)
        browser.find_element(By.TAG_NAME, 'button').click()
        browser.implicitly_wait(10)
        assert browser.find_element(By.TAG_NAME, 'h2').text == 'Учётная запись уже существует'
        browser.back()
        browser.back()

    def test10(self):
        browser.implicitly_wait(10)
        browser.find_element(By.CSS_SELECTOR, '#t-btn-tab-phone').click()
        browser.find_element(By.CSS_SELECTOR, '#username').send_keys('758439ПОА6543')
        browser.find_element(By.CSS_SELECTOR, '#password').click()
        assert browser.find_element(By.CSS_SELECTOR,'main.app-container:nth-child(2) div.card-container.login-form-container div.card-container__wrapper div.card-container__content form.login-form div.tabs-input-container div.rt-input-container.tabs-input-container__login:nth-child(3) div.rt-input.rt-input--rounded.rt-input--orange > span.rt-input__placeholder.rt-input__placeholder--top').text == 'Логин'
        browser.find_element(By.CSS_SELECTOR, '#username').clear()

    def test11(self):
        browser.implicitly_wait(10)
        browser.find_element(By.CSS_SELECTOR, '#kc-register').click()
        browser.find_element(By.CSS_SELECTOR,'main.app-container:nth-child(2) div.card-container.register-form-container div.card-container__wrapper div.card-container__content form.register-form div.name-container:nth-child(2) div.rt-input-container:nth-child(1) div.rt-input.rt-input--rounded.rt-input--orange > input.rt-input__input.rt-input__input--rounded.rt-input__input--orange').send_keys('asdfghj')
        browser.find_element(By.CSS_SELECTOR, '#address').click()
        assert browser.find_element(By.CSS_SELECTOR,'main.app-container:nth-child(2) div.card-container.register-form-container div.card-container__wrapper div.card-container__content form.register-form div.name-container:nth-child(2) div.rt-input-container.rt-input-container--error:nth-child(1) > span.rt-input-container__meta.rt-input-container__meta--error').text == 'Необходимо заполнить поле кириллицей. От 2 до 30 символов.'
        browser.back()

    def test12(self):
        browser.implicitly_wait(10)
        browser.find_element(By.CSS_SELECTOR, '#kc-register').click()
        browser.find_element(By.CSS_SELECTOR,'main.app-container:nth-child(2) div.card-container.register-form-container div.card-container__wrapper div.card-container__content form.register-form div.name-container:nth-child(2) div.rt-input-container:nth-child(1) div.rt-input.rt-input--rounded.rt-input--orange > input.rt-input__input.rt-input__input--rounded.rt-input__input--orange').send_keys(
            'Влад Влад')
        browser.find_element(By.CSS_SELECTOR, '#address').click()
        assert browser.find_element(By.CSS_SELECTOR,'main.app-container:nth-child(2) div.card-container.register-form-container div.card-container__wrapper div.card-container__content form.register-form div.name-container:nth-child(2) div.rt-input-container.rt-input-container--error:nth-child(1) > span.rt-input-container__meta.rt-input-container__meta--error').text == 'Необходимо заполнить поле кириллицей. От 2 до 30 символов.'
        browser.back()

    def test13(self):
        browser.implicitly_wait(10)
        browser.find_element(By.CSS_SELECTOR, '#kc-register').click()
        browser.find_element(By.CSS_SELECTOR, '#address').send_keys('владвлад@gmail.com')
        browser.find_element(By.CSS_SELECTOR, '#password').click()
        assert browser.find_element(By.CSS_SELECTOR,'main.app-container:nth-child(2) div.card-container.register-form-container div.card-container__wrapper div.card-container__content form.register-form div.rt-input-container.rt-input-container--error.email-or-phone.register-form__address:nth-child(6) > span.rt-input-container__meta.rt-input-container__meta--error').text == 'Введите телефон в формате +7ХХХХХХХХХХ или +375XXXXXXXXX, или email в формате example@email.ru'
        browser.back()

    def test14(self):
        browser.implicitly_wait(10)
        browser.find_element(By.CSS_SELECTOR, '#kc-register').click()
        browser.find_element(By.CSS_SELECTOR, '#password').send_keys('123123123sS')
        browser.find_element(By.CSS_SELECTOR, '#password-confirm').send_keys('123123123sSC')
        assert browser.find_element(By.CSS_SELECTOR,'main.app-container:nth-child(2) div.card-container.register-form-container div.card-container__wrapper div.card-container__content form.register-form div.new-password-container:nth-child(8) div.rt-input-container.rt-input-container--error.new-password-container__password:nth-child(1) > span.rt-input-container__meta.rt-input-container__meta--error').text == 'Ваш пароль не совпадает'
        browser.back()

    def test15(self):
        browser.implicitly_wait(10)
        browser.find_element(By.CSS_SELECTOR, '#kc-register').click()
        browser.find_element(By.CSS_SELECTOR, '#password').send_keys('123123123s')
        browser.find_element(By.CSS_SELECTOR, '#password-confirm').click()
        assert browser.find_element(By.CSS_SELECTOR,'main.app-container:nth-child(2) div.card-container.register-form-container div.card-container__wrapper div.card-container__content form.register-form div.new-password-container:nth-child(8) div.rt-input-container.rt-input-container--error.new-password-container__password:nth-child(1) > span.rt-input-container__meta.rt-input-container__meta--error').text == 'Пароль должен содержать хотя бы одну заглавную букву'
        browser.back()

    def test16(self):
        browser.implicitly_wait(10)
        browser.find_element(By.CSS_SELECTOR, '#t-btn-tab-login').click()
        browser.find_element(By.CSS_SELECTOR, '#username').send_keys('mijori4914wwgoc.com')
        browser.find_element(By.CSS_SELECTOR, '#password').send_keys('123123123sS')
        browser.find_element(By.CSS_SELECTOR, '#kc-login').click()
        assert browser.find_element(By.CSS_SELECTOR, '#form-error-message').text == "Неверный email"

    def test17(self):
        browser.implicitly_wait(10)
        browser.find_element(By.CSS_SELECTOR, '#t-btn-tab-login').click()
        browser.find_element(By.CSS_SELECTOR, '#username').clear()
        browser.find_element(By.CSS_SELECTOR, '#username').send_keys('mijori4914@wwgoc.com')
        browser.find_element(By.CSS_SELECTOR, '#password').clear()
        browser.find_element(By.CSS_SELECTOR, '#password').send_keys('123123123')
        browser.find_element(By.CSS_SELECTOR, '#kc-login').click()
        assert browser.find_element(By.CSS_SELECTOR,'#form-error-message').text == "Пароль должен содержать буквы и цифры"

    def test18(self):
        browser.implicitly_wait(10)
        browser.find_element(By.CSS_SELECTOR, '#t-btn-tab-login').click()
        browser.find_element(By.CSS_SELECTOR, '#username').clear()
        browser.find_element(By.CSS_SELECTOR, '#username').send_keys(data.Login)
        browser.find_element(By.CSS_SELECTOR, '#password').clear()
        browser.find_element(By.CSS_SELECTOR, '#password').send_keys('123')
        browser.find_element(By.CSS_SELECTOR, '#kc-login').click()
        assert browser.find_element(By.CSS_SELECTOR,'#form-error-message').text == "Пароль должен быть не менее 6 символов"

    def test19(self):
        browser.implicitly_wait(10)
        browser.find_element(By.CSS_SELECTOR, '#t-btn-tab-login').click()
        browser.find_element(By.CSS_SELECTOR, '#username').clear()
        browser.find_element(By.CSS_SELECTOR, '#username').send_keys(data.Login)
        browser.find_element(By.CSS_SELECTOR, '#password').clear()
        browser.find_element(By.CSS_SELECTOR, '#password').send_keys('123234567898765456789876sSEFDGhgf')
        browser.find_element(By.CSS_SELECTOR, '#kc-login').click()
        assert browser.find_element(By.CSS_SELECTOR,'#form-error-message').text == "Пароль должен быть не более 20 символов"

    def test20(self):
        browser.implicitly_wait(10)
        browser.find_element(By.CSS_SELECTOR, '#t-btn-tab-login').click()
        browser.find_element(By.CSS_SELECTOR, '#username').clear()
        browser.find_element(By.CSS_SELECTOR, '#password').clear()
        browser.find_element(By.CSS_SELECTOR, '#kc-login').click()
        assert browser.find_element(By.CSS_SELECTOR,'#form-error-message').text == "Ожидаемый результат: система должна вывести сообщение об ошибке с текстом Заполните все поля"
