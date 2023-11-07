import email
import imaplib
import quopri
import time
import pendulum
import pytest

from settings import DataLogin, WrongDataLogin
from Pages.registration import RegistrationPageLocators

parametrize = pytest.mark.parametrize


def mail_read():
    connection = imaplib.IMAP4_SSL('imap.yandex.ru', 993)
    connection.login(DataLogin.mail_address, DataLogin.mail_pass)
    connection.select("INBOX")
    _, data = connection.uid('search', 'from', 'no-reply@sirius.online')
    latest_msg = data[0].split()[-1]
    _, data = connection.uid('fetch', latest_msg, '(RFC822)')
    raw_msg = data[0][1]

    get_msg = email.message_from_bytes(raw_msg)

    for part in get_msg.walk():
        if part.get_content_maintype() == 'text' and part.get_content_subtype() == 'plain':
            return quopri.decodestring(part.get_payload()).decode('utf-8')


def test_full_std_registration_main_olymp(web_driver):
    """Простая регистрация на основную олимпиаду"""
    page = RegistrationPageLocators(web_driver)
    # filling fields:
    page.surname_fld.send_keys(DataLogin.surmane)
    page.name_fld.send_keys(DataLogin.name)
    page.fathers_name.send_keys(DataLogin.fathersname)
    page.d_o_b.send_keys(DataLogin.d_o_birth)
    page.title.click()
    page.mail_fld.send_keys(DataLogin.mail_address)
    page.vosh_login.send_keys(DataLogin.vosh_login)
    page.phone_numb_fld.send_keys(DataLogin.phone_numb)
    page.snils_fld.send_keys(DataLogin.snils)
    page.profession_fld.send_keys(DataLogin.profesion)

    page.country_selct_fld.scroll_to_element()
    page.country_selct_fld.click()
    time.sleep(1)

    page.city_fld.send_keys(DataLogin.city)
    page.company_nm_fld.send_keys(DataLogin.comp_name)
    page.school_fld.send_keys(DataLogin.school)
    page.grade_nmb_fld.send_keys(DataLogin.grade)

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
            assert page.surname_fld.get_attribute('value') == DataLogin.surmane and \
                   page.name_fld.get_attribute('value') == DataLogin.name and \
                   page.fathers_name.get_attribute('value') == DataLogin.fathersname
            assert page.d_o_b.get_attribute('value') == DataLogin.d_o_birth
            assert page.mail_fld.get_attribute('value') == DataLogin.mail_address
            assert page.vosh_login.get_attribute('value') == DataLogin.vosh_login
            assert page.phone_numb_fld.get_attribute('value') == DataLogin.phone_numb
            assert page.snils_fld.get_attribute('value') == DataLogin.snils
            assert page.profession_fld.get_attribute('value') == DataLogin.profesion
            assert page.city_fld.get_attribute('value') == DataLogin.city
            assert page.company_nm_fld.get_attribute('value') == DataLogin.comp_name
            assert page.school_fld.get_attribute('value') == DataLogin.school
            assert page.grade_nmb_fld.get_attribute('value') == DataLogin.grade
            print('Проверка полей прошла.')

        except Exception as error:
            print(f'\n, что-то пошло не так, {error}')

        time.sleep(2)
        get_email_txt = str(mail_read())
        assert "Основная олимпиада" and 'Макс' in get_email_txt
        print('Проверка почты прошла')

    else:
        print('Кнопка "перейти к тестированию" не активна')
        raise AssertionError


def test_full_std_registration_repeated_data(web_driver):
    """Простая регистрация на основную олимпиаду"""
    page = RegistrationPageLocators(web_driver)
    # filling fields:
    page.surname_fld.send_keys(DataLogin.surmane)
    page.name_fld.send_keys(DataLogin.name)
    page.fathers_name.send_keys(DataLogin.fathersname)
    page.d_o_b.send_keys(DataLogin.d_o_birth)
    page.title.click()
    page.mail_fld.send_keys(DataLogin.mail_address)
    page.vosh_login.send_keys(DataLogin.vosh_login)
    page.phone_numb_fld.send_keys(DataLogin.phone_numb)
    page.snils_fld.send_keys(DataLogin.snils)
    page.profession_fld.send_keys(DataLogin.profesion)

    page.country_selct_fld.scroll_to_element()
    page.country_selct_fld.click()
    time.sleep(1)

    page.city_fld.send_keys(DataLogin.city)
    page.company_nm_fld.send_keys(DataLogin.comp_name)
    page.school_fld.send_keys(DataLogin.school)
    page.grade_nmb_fld.send_keys(DataLogin.grade)

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
            assert page.surname_fld.get_attribute('value') == DataLogin.surmane and \
                   page.name_fld.get_attribute('value') == DataLogin.name and \
                   page.fathers_name.get_attribute('value') == DataLogin.fathersname
            assert page.d_o_b.get_attribute('value') == DataLogin.d_o_birth
            assert page.mail_fld.get_attribute('value') == DataLogin.mail_address
            assert page.vosh_login.get_attribute('value') == DataLogin.vosh_login
            assert page.phone_numb_fld.get_attribute('value') == DataLogin.phone_numb
            assert page.snils_fld.get_attribute('value') == DataLogin.snils
            assert page.profession_fld.get_attribute('value') == DataLogin.profesion
            assert page.city_fld.get_attribute('value') == DataLogin.city
            assert page.company_nm_fld.get_attribute('value') == DataLogin.comp_name
            assert page.school_fld.get_attribute('value') == DataLogin.school
            assert page.grade_nmb_fld.get_attribute('value') == DataLogin.grade
            print('Проверка полей прошла.')

        except Exception as error:
            print(f'\n, что-то пошло не так, {error}')

        time.sleep(2)
        get_email_txt = str(mail_read())
        assert DataLogin.name and 'Ранее вы регистрировались на другие форматы участия в выбранной олимпиаде:' in get_email_txt
        print('Проверка почты прошла')

    else:
        print('Кнопка "перейти к тестированию" не активна')
        raise AssertionError


def test_full_std_registration_add_olymp(web_driver):
    """Простая регистрация на дополнительную олимпиаду"""
    page = RegistrationPageLocators(web_driver)

    page.surname_fld.send_keys(DataLogin.surmane)
    page.name_fld.send_keys(DataLogin.name)
    page.fathers_name.send_keys(DataLogin.fathersname)
    page.d_o_b.send_keys(DataLogin.d_o_birth)
    page.title.click()
    page.mail_fld.send_keys(DataLogin.mail_address)
    page.vosh_login.send_keys(DataLogin.vosh_login)
    page.phone_numb_fld.send_keys(DataLogin.phone_numb)
    page.snils_fld.send_keys(DataLogin.snils)
    page.profession_fld.send_keys(DataLogin.profesion)

    page.country_selct_fld.scroll_to_element()
    page.country_selct_fld.click()
    time.sleep(1)

    page.city_fld.send_keys(DataLogin.city)
    page.company_nm_fld.send_keys(DataLogin.comp_name)
    page.school_fld.send_keys(DataLogin.school)
    page.grade_nmb_fld.send_keys(DataLogin.grade)

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
            assert page.surname_fld.get_attribute('value') == DataLogin.surmane and \
                   page.name_fld.get_attribute('value') == DataLogin.name and \
                   page.fathers_name.get_attribute('value') == DataLogin.fathersname
            assert page.d_o_b.get_attribute('value') == DataLogin.d_o_birth
            assert page.mail_fld.get_attribute('value') == DataLogin.mail_address
            assert page.vosh_login.get_attribute('value') == DataLogin.vosh_login
            assert page.phone_numb_fld.get_attribute('value') == DataLogin.phone_numb
            assert page.snils_fld.get_attribute('value') == DataLogin.snils
            assert page.profession_fld.get_attribute('value') == DataLogin.profesion
            assert page.city_fld.get_attribute('value') == DataLogin.city
            assert page.company_nm_fld.get_attribute('value') == DataLogin.comp_name
            assert page.school_fld.get_attribute('value') == DataLogin.school
            assert page.grade_nmb_fld.get_attribute('value') == DataLogin.grade
            print('Проверка полей прошла.')
        except Exception as error:
            print(f'\n, что-то пошло не так, {error}')
        # проверки на заполнение полей далее:

        time.sleep(2)
        get_email_txt = str(mail_read())
        assert "Дополнительная олимпиада" and 'Макс' in get_email_txt
        print('Проверка почты прошла')

    else:
        print('Кнопка "перейти к тестированию" не активна')
        raise AssertionError


def test_no_check_boxes_registration_main_olymp(web_driver):
    """Заполнены обязательный поля, не отмечены чек-боксы. Проверяем кликабельность кнопки."""
    page = RegistrationPageLocators(web_driver)

    page.surname_fld.send_keys(DataLogin.surmane)
    page.name_fld.send_keys(DataLogin.name)
    page.fathers_name.send_keys(DataLogin.fathersname)
    page.d_o_b.send_keys(DataLogin.d_o_birth)
    page.title.click()
    page.mail_fld.send_keys(DataLogin.mail_address)
    page.vosh_login.send_keys(DataLogin.vosh_login)
    page.phone_numb_fld.send_keys(DataLogin.phone_numb)
    page.snils_fld.send_keys(DataLogin.snils)
    page.profession_fld.send_keys(DataLogin.profesion)

    page.country_selct_fld.scroll_to_element()
    page.country_selct_fld.click()
    time.sleep(1)

    page.city_fld.send_keys(DataLogin.city)
    page.company_nm_fld.send_keys(DataLogin.comp_name)
    page.school_fld.send_keys(DataLogin.school)
    page.grade_nmb_fld.send_keys(DataLogin.grade)

    assert not page.submit_btn.is_clickable()


@parametrize('snils_numb', ['00000000000', '0000000000', WrongDataLogin.namelatin],
             ids=['11 zeros', '10 zeros', 'latin'])
@parametrize('phone', [WrongDataLogin.namespec, WrongDataLogin.namelatin, WrongDataLogin.namecyrillic,
                       WrongDataLogin.phone_13dig],
             ids=['specials', 'latin', 'cyrillic', '13 digits after +7'])
@parametrize('vosh_data', [WrongDataLogin.name260, WrongDataLogin.namespec, WrongDataLogin.vosh_loginzero],
             ids=['long str - 260', 'specials', 'vosh_zero'])
def test_other_flds_errors(web_driver, snils_numb, phone, vosh_data):
    '''Проверка поведения поля даты'''
    page = RegistrationPageLocators(web_driver)

    page.snils_fld.send_keys(snils_numb)
    page.phone_numb_fld.send_keys(phone)
    page.vosh_login.send_keys(vosh_data)
    page.title.click()

    assert "ui-textinput__input-mode-wrong" in page.snils_fld.get_attribute('class')
    assert "ui-textinput__input-mode-wrong" in page.phone_numb_fld.get_attribute('class')
    assert "ui-textinput__input-mode-wrong" in page.vosh_login.get_attribute('class')


@parametrize('mail_address', ['4@4.55', WrongDataLogin.namelatin, '!#$%^&*@#$.ru', 'апролд@апрол.ru'],
             ids=['digits', 'latin', 'specials', 'cyrillic'])
@parametrize('str_input_data', [WrongDataLogin.name260, WrongDataLogin.namespec, WrongDataLogin.namelatin, ''],
             ids=['long str - 260', 'specials', 'latin', 'empty'])
@parametrize('date', ['00.00.1000', pendulum.yesterday(), pendulum.tomorrow()],
             ids=['zeros', 'вчера', 'из будущего'])
def test_wrong_data_for_flds(web_driver, mail_address, str_input_data, date):
    '''Проверка появления текстовых ошибок/подсказок обязательных полей
    под полями при вводе потенциально некорректного значения'''

    page = RegistrationPageLocators(web_driver)

    page.name_fld.send_keys(str_input_data)
    page.surname_fld.send_keys(str_input_data)
    page.d_o_b.send_keys(date)
    page.title.click()
    page.mail_fld.send_keys(mail_address)
    page.profession_fld.send_keys(str_input_data)
    page.country_selct_fld.scroll_to_element()
    page.country_selct_fld.click()
    time.sleep(1)
    page.city_fld.send_keys(str_input_data)
    page.company_nm_fld.send_keys(str_input_data)
    page.school_fld.send_keys(str_input_data)
    page.grade_nmb_fld.send_keys(str_input_data)

    if page.submit_btn.is_clickable():
        print('Кнопка "Перейти к тестированию" активна')
    else:
        # В проверку также можно добавить конкретные тексты ошибок, в зависимости от вводимых данных.
        assert all([
                    "ui-textinput__input-mode-wrong" in page.name_fld.get_attribute('class'),
                    "ui-textinput__input-mode-wrong" in page.surname_fld.get_attribute('class'),
                    "ui-textinput__input-mode-wrong" in page.d_o_b.get_attribute('class'),
                    "ui-textinput__input-mode-wrong" in page.mail_fld.get_attribute('class'),
                    "ui-textinput__input-mode-wrong" in page.profession_fld.get_attribute('class'),
                    "ui-textinput__input-mode-wrong" in page.city_fld.get_attribute('class'),
                    "ui-textinput__input-mode-wrong" in page.company_nm_fld.get_attribute('class'),
                    "ui-textinput__input-mode-wrong" in page.school_fld.get_attribute('class'),
                    "ui-textinput__input-mode-wrong" in page.grade_nmb_fld.get_attribute('class')
                    ])


def test_errors_under_fields_to_check(web_driver):
    "Проверка работы поле и появления ошибок. Для теста механизма."
    page = RegistrationPageLocators(web_driver)

    page.mail_fld.send_keys(WrongDataLogin.mail_address)
    page.vosh_login.send_keys(WrongDataLogin.vosh_loginlatin)
    page.snils_fld.send_keys(WrongDataLogin.snils)

    assert all(["ui-textinput__input-mode-wrong" in page.mail_fld.get_attribute('class'),
                "ui-textinput__input-mode-wrong" in page.vosh_login.get_attribute('class'),
                "ui-textinput__input-mode-wrong" in page.snils_fld.get_attribute('class')])
