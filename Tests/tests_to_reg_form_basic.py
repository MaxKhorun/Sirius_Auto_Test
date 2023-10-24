import pytest
from Pages.registration import RegistrationPageLocators

def start_page(web_driver):

    page = RegistrationPageLocators(web_driver)
