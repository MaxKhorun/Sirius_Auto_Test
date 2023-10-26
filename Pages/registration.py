from settings import base_url
from selenium.webdriver.common.by import By
from Pages.base import WebPage
from Pages.elements import WebElement


class RegistrationPageLocators(WebPage):

    def __init__(self, web_driver, url=''):
        if not url:
            url = base_url

        super().__init__(web_driver, url)
        
    name_fld = WebElement(class_name="test-locator-sf-lastName")
