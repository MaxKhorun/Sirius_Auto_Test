from settings import base_url
from Pages.base import WebPage
from Pages.elements import WebElement


class RegistrationPageLocators(WebPage):

    def __init__(self, web_driver, url=''):
        if not url:
            url = base_url

        super().__init__(web_driver, url)

    title = WebElement(class_name='login_page__title')
    """Данные о себе"""
    surname_fld = WebElement(xpath="(//input[contains( @ type, 'text')])[1]")
    name_fld = WebElement(xpath="(//input[contains( @ type, 'text')])[2]")
    fathers_name = WebElement(xpath="(//input[contains(@type,'text')])[3]")
    d_o_b = WebElement(css_selector="input[placeholder='дд.мм.гггг']")
    mail_fld = WebElement(xpath="(//input[contains(@type,'text')])[5]")

    vosh_login = WebElement(xpath="(//input[contains(@type,'text')])[6]")
    phone_numb_fld = WebElement(xpath="(//input[contains(@type,'text')])[7]")
    snils_fld = WebElement(xpath="(//input[contains(@type,'text')])[8]")
    profession_fld =WebElement(xpath="(//input[contains(@type,'text')])[9]")
    """Информация о школе"""
    country_selct_fld = WebElement(class_name="ui-schema-auth-form__country-select")
    australia = WebElement(css_selector="option[value='AT']")
    bagams = WebElement(css_selector="option[value='BS']")
    city_fld = WebElement(xpath="(//input[contains(@type,'text')])[10]")
    company_nm_fld = WebElement(xpath="(//input[contains(@type,'text')])[11]")
    school_fld = WebElement(xpath="(//input[contains(@type,'text')])[12]")
    grade_nmb_fld = WebElement(xpath="(//input[contains(@type,'text')])[13]")

    """Блок радио-кнопок, кнопок и чек-боксов ui-schema-auth-form__enum-input-radio-checked-false"""
    radio_main_olymp = WebElement(xpath="//span[contains(text(),'Основная олимпиада')]")
    radio_add_olymp = WebElement(xpath="//span[contains(text(),'Дополнительная олимпиада')]")
    checkbox_1 = WebElement(xpath="(//input[contains(@type,'checkbox')])[1]")
    checkbox_2 = WebElement(xpath="(//input[contains(@type,'checkbox')])[2]")
    checkbox_3 = WebElement(xpath="(//input[contains(@type,'checkbox')])[3]")
    submit_btn = WebElement(class_name="smt-register-form__register-btn")

    """Страница подтверждения отправки"""

    title_txt = WebElement(class_name="text-xxl")
    info_txt = WebElement(class_name="text-l")
    return_btn = WebElement(css_selector=".ui-button__content")