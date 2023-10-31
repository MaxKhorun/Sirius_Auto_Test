import time
import imaplib
import email

import pytest

from settings import mail_adress, mail_pass
from selenium.webdriver import Keys, ActionChains
from Pages.registration import RegistrationPageLocators

parametrize = pytest.mark.parametrize


def test_full_std_registration_ain_olymp(web_driver):
    page = RegistrationPageLocators(web_driver)

    page.surname_fld.send_keys('Хор')
    page.name_fld.send_keys('Макс')
    page.fathers_name.send_keys('Отецович')

    assert page.surname_fld.get_attribute('value') == 'Хор' and \
           page.name_fld.get_attribute('value') == 'Макс' and \
           page.fathers_name.get_attribute('value') == 'Отецович'

    page.d_o_b.send_keys('12.12.1989')
    page.fathers_name.click()
    assert page.d_o_b.get_attribute('value') == '12.12.1989'

    page.mail_fld.send_keys(mail_adress)
    assert page.mail_fld.get_attribute('value') == mail_adress

    page.phone_numb_fld.send_keys('88123020705')
    assert page.phone_numb_fld.get_attribute('value') == '88123020705'

    page.snils_fld.send_keys('00000000000')
    assert page.snils_fld.get_attribute('value') == '00000000000'

    page.profession_fld.send_keys('Super Mario')
    assert page.profession_fld.get_attribute('value') == 'SuperMario'

    country = page.country_selct_fld
    country.scroll_to_element()
    country.click()
    time.sleep(2)

    page.city_fld.send_keys("Астана")
    assert page.city_fld.get_attribute('value') == 'Астана'

    page.company_nm_fld.send_keys('''ТрататаLtd''')
    assert page.company_nm_fld.get_attribute('value') == 'ТрататаLtd'

    page.school_fld.send_keys(r'ГИмназия №2')
    assert page.school_fld.get_attribute('value') == 'ГИмназия№2'

    page.grade_nmb_fld.send_keys('5"Ю"')
    assert page.grade_nmb_fld.get_attribute('value') == '5"Ю"'

    page.radio_main_olymp.scroll_to_element()
    # здесь параметризируем выбор основной олимпиады или дополнительной.
    page.checkbox_1.click()
    page.checkbox_2.click()
    page.checkbox_3.click()

    assert page.submit_btn.is_clickable()

    page.submit_btn.click()
    page.wait_page_loaded()
    assert 'Основная олимпиада' in page.title_txt.get_text() \
           and mail_adress in page.info_txt.get_text()

    #проверки на заполнение полей далее:
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


def test_full_std_registration_add_olymp(web_driver):
    page = RegistrationPageLocators(web_driver)

    page.surname_fld.send_keys('Хор')
    page.name_fld.send_keys('Макс')
    page.fathers_name.send_keys('Отецович')

    assert page.surname_fld.get_attribute('value') == 'Хор' and \
           page.name_fld.get_attribute('value') == 'Макс' and \
           page.fathers_name.get_attribute('value') == 'Отецович'

    page.d_o_b.send_keys('12.12.1989')
    page.fathers_name.click()
    assert page.d_o_b.get_attribute('value') == '12.12.1989'

    page.mail_fld.send_keys(mail_adress)
    assert page.mail_fld.get_attribute('value') == mail_adress

    page.phone_numb_fld.send_keys('88123020705')
    assert page.phone_numb_fld.get_attribute('value') == '88123020705'

    page.snils_fld.send_keys('00000000000')
    assert page.snils_fld.get_attribute('value') == '00000000000'

    page.profession_fld.send_keys('Super Mario')
    assert page.profession_fld.get_attribute('value') == 'SuperMario'

    country = page.country_selct_fld
    country.scroll_to_element()
    country.click()
    time.sleep(2)

    page.city_fld.send_keys("Астана")
    assert page.city_fld.get_attribute('value') == 'Астана'

    page.company_nm_fld.send_keys('''ТрататаLtd''')
    assert page.company_nm_fld.get_attribute('value') == 'ТрататаLtd'

    page.school_fld.send_keys(r'ГИмназия №2')
    assert page.school_fld.get_attribute('value') == 'ГИмназия№2'

    page.grade_nmb_fld.send_keys('5"Ю"')
    assert page.grade_nmb_fld.get_attribute('value') == '5"Ю"'

    page.radio_add_olymp.click()
    # здесь параметризируем выбор основной олимпиады или дополнительной.
    page.checkbox_1.click()
    page.checkbox_2.click()
    page.checkbox_3.click()

    page.submit_btn.click()
    page.wait_page_loaded()
    assert 'Дополнительная олимпиада' in page.title_txt.get_text() \
           and mail_adress in page.info_txt.get_text()

    #проверки на заполнение полей далее:
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

# @parametrize('checkbox', [RegistrationPageLocators.checkbox_1,
#                            RegistrationPageLocators.checkbox_2, RegistrationPageLocators.checkbox_3])
def test_registration_main_check_boxes(web_driver):
    page = RegistrationPageLocators(web_driver)

    page.surname_fld.send_keys('Хор')
    page.name_fld.send_keys('Макс')
    page.fathers_name.send_keys('Отецович')

    assert page.surname_fld.get_attribute('value') == 'Хор' and \
           page.name_fld.get_attribute('value') == 'Макс' and \
           page.fathers_name.get_attribute('value') == 'Отецович'

    page.d_o_b.send_keys('12.12.1989')
    page.fathers_name.click()
    assert page.d_o_b.get_attribute('value') == '12.12.1989'

    page.mail_fld.send_keys("23@mail.ru")
    assert page.mail_fld.get_attribute('value') == '23@mail.ru'

    page.phone_numb_fld.send_keys('88123020705')
    assert page.phone_numb_fld.get_attribute('value') == '88123020705'

    page.snils_fld.send_keys('00000000000')
    assert page.snils_fld.get_attribute('value') == '00000000000'

    page.profession_fld.send_keys('Super Mario')
    assert page.profession_fld.get_attribute('value') == 'SuperMario'

    country = page.country_selct_fld
    country.scroll_to_element()
    country.click()
    time.sleep(2)

    page.city_fld.send_keys("Астана")
    assert page.city_fld.get_attribute('value') == 'Астана'

    page.company_nm_fld.send_keys('''Тратата Ltd''')
    assert page.company_nm_fld.get_attribute('value') == 'Тратата Ltd'

    page.school_fld.send_keys(r'ГИмназия №2')
    assert page.school_fld.get_attribute('value') == 'ГИмназия№2'

    page.grade_nmb_fld.send_keys('5"Ю"')
    assert page.grade_nmb_fld.get_attribute('value') == '5"Ю"'

    page.checkbox_1.scroll_to_element()

    # здесь параметризируем выбор основной олимпиады или дополнительной.
    page.checkbox_1.click()
    page.checkbox_2.click()
    page.checkbox_3.click()

    assert page.submit_btn.is_clickable()
    assert mail_adress in page.title_txt.get_text()


def test_getting_email(web_driver):
    page = RegistrationPageLocators(web_driver)
    page.checkbox_1.scroll_to_element()

    time.sleep(2)


# @parametrize('date_o_b', [], ids=['невозможные цифры', 'вчера', 'из будущего'])
def test_date_of_birth(web_driver):
    pass


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
