"""
UI Test Designed by Anurag Gupta
 :date: Sep 28, 2020
 :author: Anurag Gupta
"""
from random import random

import pytest
from selenium.webdriver.common.keys import Keys

from lib.helper.common_utilities import get_alert_text, alert_operation, switch_alert, random_name
from pageobjects.alert_frames_window_page import AlertsWindowsPage


class TestAlert:
    """Class contains test cases related to Alert page"""
    def test_see_alert_test(self, driver_instance):
        alert_page = AlertsWindowsPage(driver_instance)
        alert_page.open_url()
        alert_page.click_alert_button()
        alert_page.click_see_alert_button()
        assert get_alert_text(driver_instance) == "You clicked a button", "Alert text mismatched"
        alert_operation(driver_instance, ok=True)

    def test_five_sec_alert_see_alert_test(self, driver_instance):
        alert_page = AlertsWindowsPage(driver_instance)
        alert_page.open_url()
        alert_page.click_alert_button()
        alert_page.click_five_sec_alert_button()
        assert get_alert_text(driver_instance) == "This alert appeared after 5 seconds"
        alert_operation(driver_instance, ok=True)

    @pytest.mark.parametrize("flag, expected_text", [(True, "You selected Ok"), (False, "You selected Cancel")])
    def test_confirm_button_alert_test(self, driver_instance, flag, expected_text):
        alert_page = AlertsWindowsPage(driver_instance)
        alert_page.open_url()
        alert_page.click_alert_button()
        alert_page.click_confirm_button_alert_button()
        assert get_alert_text(driver_instance) == "Do you confirm action?"
        alert_operation(driver_instance, ok=flag)
        assert alert_page.get_confirm_text() == expected_text

    @pytest.mark.parametrize("flag, expected_text", [(True, "You entered "), (False, "")])
    def test_promt_button_alert_test(self, driver_instance, flag, expected_text):
        alert_page = AlertsWindowsPage(driver_instance)
        alert_page.open_url()
        alert_page.click_alert_button()
        alert_page.click_promt_button_alert_button()
        assert get_alert_text(driver_instance) == "Please enter your name"
        msg = random_name(prefix="Message")
        switch_alert(driver_instance).send_keys(msg)
        alert_operation(driver_instance, ok=flag)
        if flag:
            assert alert_page.get_promt_button_text() == expected_text+msg
