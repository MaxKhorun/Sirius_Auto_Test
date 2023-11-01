import time
import imaplib
import email

import pendulum
import pytest

from settings import mail_adress, mail_pass
from selenium.webdriver import Keys, ActionChains
from Pages.registration import RegistrationPageLocators
parametrize = pytest.mark.parametrize
ch1 = RegistrationPageLocators.checkbox_1
ch2 = RegistrationPageLocators.checkbox_2

def test_full_std_registration_main_olymp(web_driver):
    page = RegistrationPageLocators(web_driver)

    page.surname_fld.send_keys('Хор')
    page.name_fld.send_keys('Макс')
    page.fathers_name.send_keys('Отецович')
    page.d_o_b.send_keys('12.12.1989')
    page.title.click()
    page.mail_fld.send_keys(mail_adress)
    page.phone_numb_fld.send_keys('88123020705')
    page.snils_fld.send_keys('00000000000')
    page.profession_fld.send_keys('Super Mario')

    country = page.country_selct_fld
    country.scroll_to_element()
    country.click()
    time.sleep(2)

    page.city_fld.send_keys("Астана")
    page.company_nm_fld.send_keys('ТрататаLtd')
    page.school_fld.send_keys(r'ГИмназия№2')
    page.grade_nmb_fld.send_keys('5"Ю"')

    page.checkbox_1.click()
    page.checkbox_2.click()
    page.checkbox_3.click()

    if page.submit_btn.is_clickable():
        page.submit_btn.click()
        page.wait_page_loaded()
        assert 'Основная олимпиада' in page.title_txt.get_text() \
               and mail_adress in page.info_txt.get_text()
        # checking an email

        try:
            page.return_btn.click()
            assert page.surname_fld.get_attribute('value') == 'Хор' and \
                   page.name_fld.get_attribute('value') == 'Макс' and \
                   page.fathers_name.get_attribute('value') == 'Отецович'
            assert page.d_o_b.get_attribute('value') == '12.12.1989'
            assert page.mail_fld.get_attribute('value') == mail_adress
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


def test_full_std_registration_add_olymp(web_driver):
    page = RegistrationPageLocators(web_driver)

    page.surname_fld.send_keys('Хор')
    page.name_fld.send_keys('Макс')
    page.fathers_name.send_keys('Отецович')
    page.d_o_b.send_keys('12.12.1989')
    page.fathers_name.click()
    page.mail_fld.send_keys(mail_adress)
    page.phone_numb_fld.send_keys('88123020705')
    page.snils_fld.send_keys('00000000000')
    page.profession_fld.send_keys('Super Mario')

    country = page.country_selct_fld
    country.scroll_to_element()
    country.click()
    time.sleep(2)

    page.city_fld.send_keys("Астана")
    page.company_nm_fld.send_keys('''ТрататаLtd''')
    page.school_fld.send_keys(r'ГИмназия №2')
    page.grade_nmb_fld.send_keys('5"Ю"')

    page.radio_add_olymp.click()
    # здесь параметризируем выбор основной олимпиады или дополнительной.
    page.checkbox_1.click()
    page.checkbox_2.click()
    page.checkbox_3.click()

    if page.submit_btn.is_clickable():
        page.submit_btn.click()
        page.wait_page_loaded()
        assert 'Дополнительная олимпиада' in page.title_txt.get_text() \
               and mail_adress in page.info_txt.get_text()
        # checking an email

        try:
            page.return_btn.click()
            assert page.surname_fld.get_attribute('value') == 'Хор' and \
                   page.name_fld.get_attribute('value') == 'Макс' and \
                   page.fathers_name.get_attribute('value') == 'Отецович'
            assert page.d_o_b.get_attribute('value') == '12.12.1989'
            assert page.mail_fld.get_attribute('value') == mail_adress
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


def test_registration_main_check_boxes(web_driver):
    page = RegistrationPageLocators(web_driver)

    # page.surname_fld.send_keys('Хор')
    # page.name_fld.send_keys('Макс')
    # page.fathers_name.send_keys('Отецович')
    #
    # page.d_o_b.send_keys('12.12.1989')
    # page.fathers_name.click()
    # page.mail_fld.send_keys("23@mail.ru")
    # page.phone_numb_fld.send_keys('88123020705')
    # page.snils_fld.send_keys('00000000000')
    # page.profession_fld.send_keys('Super Mario')
    #
    # country = page.country_selct_fld
    # country.scroll_to_element()
    # country.click()
    # time.sleep(2)
    #
    # page.city_fld.send_keys("Астана")
    # page.company_nm_fld.send_keys('''Тратата Ltd''')
    # page.school_fld.send_keys(r'ГИмназия №2')
    # page.grade_nmb_fld.send_keys('5"Ю"')

    page.checkbox_1.scroll_to_element()

    # здесь параметризируем выбор основной олимпиады или дополнительной.
    page.checkbox_1.click()

    assert page.submit_btn.is_clickable()
    # assert mail_adress in page.title_txt.get_text()


def test_getting_email(web_driver):
    page = RegistrationPageLocators(web_driver)
    page.checkbox_1.scroll_to_element()
    radioclass = page.radio_main_olymp.get_attribute('class')
    print(radioclass)

    time.sleep(2)


@parametrize('date', ['00.00.1000', pendulum.yesterday(), pendulum.tomorrow()], ids=['zeros', 'вчера', 'из будущего'])
def test_date_of_birth(web_driver, date):
    page = RegistrationPageLocators(web_driver)

    page.d_o_b.send_keys(date)
    page.title.click()

    assert page.d_o_b.get_attribute('value') is ''


@parametrize('snils_numb', ['00000000000', '0000000000', ' asdfghjkl;'])
def test_snils_fld(web_driver, snils_numb):

    page = RegistrationPageLocators(web_driver)

    page.snils_fld.send_keys(snils_numb, 1)

    assert "ui-textinput__input-mode-wrong" in page.snils_fld.get_attribute('class')


@parametrize('mail_adrress', ['4@4.55', 'asdfghjkl;qwertyuiop', ])
def test_mail_fld(web_driver, mail_adrress):

    page = RegistrationPageLocators(web_driver)

    page.mail_fld.send_keys(mail_adrress)

    assert "ui-schema-auth-form__error" in page.mail_fld.get_attribute('class')
'''
имя, 
фамилия,
отчество,
 
дата рождения, 
эл.почта, 
телефон, 

страна,
професиия, 
город, 
название организации,
школа, 
класс
'''
