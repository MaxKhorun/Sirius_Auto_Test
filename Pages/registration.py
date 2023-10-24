from settings import base_url
from selenium.webdriver.common.by import By
from Pages.base import WebPage


class RegistrationPageLocators(WebPage):

    def __init__(self, web_driver, url=''):
        if not url:
            url = base_url

        super().__init__(web_driver, url)
        
    name_fld = (By.LINK_TEXT, 'Фамилия')