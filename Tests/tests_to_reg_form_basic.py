import time

from Pages.registration import RegistrationPageLocators


def test_start_page(web_driver):

    page = RegistrationPageLocators(web_driver)

    page.name_fld.click()
    time.sleep(2)
    page.name_fld.send_keys("vf")
    time.sleep(3)
