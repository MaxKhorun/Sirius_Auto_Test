import time
import imaplib
import email

import pendulum
import pytest
from selenium.webdriver import ActionChains

from settings import DataLogin, WrongDataLogin
from Pages.registration import RegistrationPageLocators

parametrize = pytest.mark.parametrize


def test_full_std_registration_main_olymp(web_driver):
    """Простая регистрация на основную олимпиаду"""
    page = RegistrationPageLocators(web_driver)
    # filling fields:
    page.surname_fld.send_keys('Хор')
    page.name_fld.send_keys('Макс')
    page.fathers_name.send_keys('Отецович')
    page.d_o_b.send_keys(DataLogin.d_o_birth)
    page.title.click()
    page.mail_fld.send_keys(DataLogin.mail_address)
    page.vosh_login.send_keys('dfgh3456767890')
    page.phone_numb_fld.send_keys('88123020705')
    page.snils_fld.send_keys('00000000000')
    page.profession_fld.send_keys('Super Mario')

    page.country_selct_fld.scroll_to_element()
    page.country_selct_fld.click()
    time.sleep(1)

    page.city_fld.send_keys("Астана")
    page.company_nm_fld.send_keys('ТрататаLtd')
    page.school_fld.send_keys('ГИмназия№2')
    page.grade_nmb_fld.send_keys('5"Ю"')

    page.checkbox_1.click()
    page.checkbox_2.click()
    page.checkbox_3.click()

    if page.submit_btn.is_clickable():
        page.submit_btn.click()
        page.wait_page_loaded()
        assert 'Основная олимпиада' in page.title_txt.get_text() \
               and DataLogin.mail_address in page.info_txt.get_text()
        # checking an email

        try:
            page.return_btn.click()
            assert page.surname_fld.get_attribute('value') == 'Хор' and \
                   page.name_fld.get_attribute('value') == 'Макс' and \
                   page.fathers_name.get_attribute('value') == 'Отецович'
            assert page.d_o_b.get_attribute('value') == DataLogin.d_o_birth
            assert page.mail_fld.get_attribute('value') == DataLogin.mail_address
            assert page.vosh_login.get_attribute("value") == 'dfgh3456767890'
            assert page.phone_numb_fld.get_attribute('value') == '88123020705'
            assert page.snils_fld.get_attribute('value') == '00000000000'
            assert page.profession_fld.get_attribute('value') == 'SuperMario'
            assert page.city_fld.get_attribute('value') == 'Астана'
            assert page.company_nm_fld.get_attribute('value') == 'ТрататаLtd'
            assert page.school_fld.get_attribute('value') == 'ГИмназия№2'
            assert page.grade_nmb_fld.get_attribute('value') == '5"Ю"'
            print('Проверка полей прошла.')
        except Exception as error:
            print('\n, Не произошёл возврат назад')

    else:
        print('Кнопка "перейти к тестированию" не активна')
        raise AssertionError


def test_full_std_registration_add_olymp(web_driver):
    """Простая регистрация на дополнительную олимпиаду"""
    page = RegistrationPageLocators(web_driver)

    page.surname_fld.send_keys('Хор')
    page.name_fld.send_keys('Макс')
    page.fathers_name.send_keys('Отецович')
    page.d_o_b.send_keys('12.12.1989')
    page.fathers_name.click()
    page.mail_fld.send_keys(DataLogin.mail_address)
    page.phone_numb_fld.send_keys('88123020705')
    page.snils_fld.send_keys('00000000000')
    page.profession_fld.send_keys('Super Mario')

    page.country_selct_fld.scroll_to_element()
    page.country_selct_fld.click()
    time.sleep(1)

    page.city_fld.send_keys("Астана")
    page.company_nm_fld.send_keys('''ТрататаLtd''')
    page.school_fld.send_keys(r'ГИмназия №2')
    page.grade_nmb_fld.send_keys('5"Ю"')

    # отмечаем дополнительную олимпиаду.
    page.radio_add_olymp.click()

    page.checkbox_1.click()
    page.checkbox_2.click()
    page.checkbox_3.click()

    if page.submit_btn.is_clickable():
        page.submit_btn.click()
        page.wait_page_loaded()
        assert 'Дополнительная олимпиада' in page.title_txt.get_text() \
               and DataLogin.mail_address in page.info_txt.get_text()
        # checking an email

        try:
            page.return_btn.click()
            assert page.surname_fld.get_attribute('value') == 'Хор' and \
                   page.name_fld.get_attribute('value') == 'Макс' and \
                   page.fathers_name.get_attribute('value') == 'Отецович'
            assert page.d_o_b.get_attribute('value') == '12.12.1989'
            assert page.mail_fld.get_attribute('value') == DataLogin.mail_address
            assert page.phone_numb_fld.get_attribute('value') == '88123020705'
            assert page.snils_fld.get_attribute('value') == '00000000000'
            assert page.profession_fld.get_attribute('value') == 'SuperMario'
            assert page.city_fld.get_attribute('value') == 'Астана'
            assert page.company_nm_fld.get_attribute('value') == 'ТрататаLtd'
            assert page.school_fld.get_attribute('value') == 'ГИмназия№2'
            assert page.grade_nmb_fld.get_attribute('value') == '5"Ю"'
            print('Проверка полей прошла.')
        except Exception as error:
            print('\n, Не произошёл возврат назад')
        # проверки на заполнение полей далее:

    else:
        print('Кнопка "перейти к тестированию" не активна')
        raise AssertionError


def test_no_check_boxes_registration_main_olymp(web_driver):
    """Заполнены обязательный поля, не отмечены чек-боксы. Проверяем кликабельность кнопки."""
    page = RegistrationPageLocators(web_driver)

    page.surname_fld.send_keys('Хор')
    page.name_fld.send_keys('Макс')
    page.fathers_name.send_keys('Отецович')

    page.d_o_b.send_keys('12.12.1989')
    page.fathers_name.click()
    page.mail_fld.send_keys("23@mail.ru")
    page.phone_numb_fld.send_keys('88123020705')
    page.snils_fld.send_keys('00000000000')
    page.profession_fld.send_keys('Super Mario')

    country = page.country_selct_fld
    country.scroll_to_element()
    country.click()
    time.sleep(2)

    page.city_fld.send_keys("Астана")
    page.company_nm_fld.send_keys('''Тратата Ltd''')
    page.school_fld.send_keys(r'ГИмназия №2')
    page.grade_nmb_fld.send_keys('5"Ю"')

    assert not page.submit_btn.is_clickable()
    assert DataLogin.mail_address in page.title_txt.get_text()


def test_getting_email(web_driver):
    page = RegistrationPageLocators(web_driver)
    page.checkbox_1.scroll_to_element()

    time.sleep(2)


@parametrize('date', ['00.00.1000', pendulum.yesterday(), pendulum.tomorrow()],
             ids=['zeros', 'вчера', 'из будущего'])
def test_date_of_birth(web_driver, date):
    '''Проверка поведения поля даты'''
    page = RegistrationPageLocators(web_driver)

    page.d_o_b.send_keys(date)
    page.title.click()

    assert page.d_o_b.get_attribute('value') is ''


@parametrize('snils_numb', ['00000000000', '0000000000', WrongDataLogin.namelatin],
             ids=['11 zeros', '10 zeros', 'latin'])
@parametrize('mail_address', ['4@4.55', WrongDataLogin.namelatin, '!#$%^&*@#$.ru', 'апролд@апрол.ru'],
             ids=['digits', 'latin', 'specials', 'cyrillic'])
@parametrize('name', [WrongDataLogin.name260, WrongDataLogin.namespec, 1234567890],
             ids=['260 symb', 'specials', 'digits'])
@parametrize('phone', [WrongDataLogin.namespec, WrongDataLogin.namelatin, WrongDataLogin.namecyrillic,
                       WrongDataLogin.phone_13dig, 0000000000],
             ids=['specials', 'latin', 'cyrillic', '13 digits after +7', 'zeros'])
@parametrize('str_input_data', [WrongDataLogin.name260, WrongDataLogin.namespec, ''],
             ids=['long str - 260', 'specials', 'empty'])
@parametrize('vosh_data', [WrongDataLogin.name260, WrongDataLogin.namespec, '', WrongDataLogin.vosh_loginzero],
             ids=['long str - 260', 'specials', 'empty', 'vosh_zero'])
def test_wrong_data_for_flds(web_driver, snils_numb, mail_address, name, str_input_data,
                             phone, vosh_data):
    ''''Проверка появления текстовых ошибок/подсказок под полями при вводе некорректного значения'''

    page = RegistrationPageLocators(web_driver)

    page.name_fld.send_keys(name)
    page.surname_fld.send_keys(name)
    page.fathers_name.send_keys(name)
    page.mail_fld.send_keys(mail_address)
    page.vosh_login.send_keys(vosh_data)
    page.phone_numb_fld.send_keys(phone)
    page.snils_fld.send_keys(snils_numb)
    page.profession_fld.send_keys(str_input_data)
    page.city_fld.send_keys(str_input_data)
    page.company_nm_fld.send_keys(str_input_data)
    page.school_fld.send_keys(str_input_data)
    page.grade_nmb_fld.send_keys(str_input_data)

    # В проверку также можно добавить конкретные тексты ошибок, в зависиомости от вводимых данных.
    assert all([
                "ui-textinput__input-mode-wrong" in page.name_fld.get_attribute('class'),
                "ui-textinput__input-mode-wrong" in page.surname_fld.get_attribute('class'),
                "ui-textinput__input-mode-wrong" in page.fathers_name.get_attribute('class'),
                "ui-textinput__input-mode-wrong" in page.phone.get_attribute('class'),
                "ui-textinput__input-mode-wrong" in page.snils_fld.get_attribute('class'),
                "ui-textinput__input-mode-wrong" in page.mail_fld.get_attribute('class'),
                "ui-textinput__input-mode-wrong" in page.profession_fld.get_attribute('class'),
                "ui-textinput__input-mode-wrong" in page.city_fld.get_attribute('class'),
                "ui-textinput__input-mode-wrong" in page.company_nm_fld.get_attribute('class'),
                "ui-textinput__input-mode-wrong" in page.school_fld.get_attribute('class'),
                "ui-textinput__input-mode-wrong" in page.grade_nmb_fld.get_attribute('class')
                ])


# @parametrize('snils_numb', ['00000000000', '0000000000', ' asdfghjkl;'],
#              ids=['11 zeros', '10 zeros', 'latin'])
def test_mail_fld(web_driver):
    page = RegistrationPageLocators(web_driver)


