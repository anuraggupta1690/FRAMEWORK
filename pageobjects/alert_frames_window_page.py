"""
Alerts Windows Page by Anurag Gupta
 :date: Sep 28, 2020
 :author: Anurag Gupta
"""

from selenium.webdriver.common.by import By

from base_class.base_class import BasePage
from lib.urls.page_details_constants import PageURLs


class AlertsWindowsPage(BasePage):
    alert_button = "//span[text() ='Alerts']"
    see_alert = "//button[@id='alertButton']"
    five_sec_alert = "//button[@id='timerAlertButton']"
    confirm_button_alert = "//button[@id='confirmButton']"
    confirm_text = "//span[@id='confirmResult']"
    promt_button = "//button[@id='promtButton']"
    promt_button_text = "//span[@id='promptResult']"


    def __init__(self, driver):
        super().__init__(driver=driver)

    def get_promt_button_alert_button(self):
        return self.find(By.XPATH, self.promt_button)

    def click_promt_button_alert_button(self):
        self.get_promt_button_alert_button().click()

    def get_promt_button_text_element(self):
        return self.find(By.XPATH, self.promt_button_text)

    def get_promt_button_text(self):
        return self.get_promt_button_text_element().text

    def get_confirm_text_element(self):
        return self.find(By.XPATH, self.confirm_text)

    def get_confirm_text(self):
        return self.get_confirm_text_element().text


    def get_confirm_button_alert_button(self):
        return self.find(By.XPATH, self.confirm_button_alert)

    def click_confirm_button_alert_button(self):
        self.get_confirm_button_alert_button().click()


    def get_five_sec_alert_button(self):
        return self.find(By.XPATH, self.five_sec_alert)

    def click_five_sec_alert_button(self):
        self.get_five_sec_alert_button().click()

    def get_alert_button(self):
        return self.find(By.XPATH, self.alert_button)

    def click_alert_button(self):
        self.get_alert_button().click()

    def get_see_alert_button(self):
        return self.find(By.XPATH, self.see_alert)

    def click_see_alert_button(self):
        self.get_see_alert_button().click()

    def open_url(self):
        self.driver.get(self.url+PageURLs.alert_window_page)

