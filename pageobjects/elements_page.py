"""
Elements Page Model Designed by Anurag Gupta
 :date: Aug 16, 2020
 :author: Anurag Gupta
"""
from selenium.webdriver.common.by import By
from lib.urls.page_details_constants import PageURLs
from base_class import wait
from base_class.base_class import BasePage
from base_class.wait import web_element_wait


class ElementPage(BasePage):
    text_box = "//span[text()='Text Box']"
    check_box = "//span[text()='Check Box']"
    radio_button = "//span[text()='Radio Button']"
    web_table = "//span[text()='Web Tables']"
    buttons = "//span[text()='Buttons']"
    links = "//span[text()='Links']"
    upload_download = "//span[text()='Upload and Download']"
    dynamic_properties = "//span[text()='Dynamic Properties']"

    def __init__(self, driver):
        super().__init__(driver=driver)

    def open_url(self):
        self.driver.get(self.url+PageURLs.elements_page)

    def get_text_box_button(self):
        return self.find(By.XPATH, self.text_box)

    def click_text_box_button(self):
        self.get_text_box_button().click()

    class TextBox(BasePage):
        full_name = "//input[@id='userName']"
        email = "//input[@id='userEmail']"
        current_address = "//textarea[@id='currentAddress']"
        permanent_address = "//textarea[@id='permanentAddress']"
        submit_button = "//button[@id='submit']"

        name_output = "//p[@id='name']"
        email_output = "//p[@id='email']"
        current_address_output = "//p[@id='currentAddress']"
        permanent_address_output = "//p[@id='permanentAddress']"

        def __init__(self, driver):
            super().__init__(driver=driver)

        def get_submit_button(self):
            return self.find(By.XPATH, self.submit_button)

        def click_submit_button(self):
            self.get_submit_button().click()

        def get_full_name_text_element(self):
            return self.find(By.XPATH, self.full_name)

        def clear_full_name(self):
            self.get_full_name_text_element().clear()

        def write_full_name(self, text):
            self.clear_full_name()
            self.get_full_name_text_element().send_keys(text)

        def get_email_text_element(self):
            return self.find(By.XPATH, self.email)

        def clear_email(self):
            self.get_email_text_element().clear()

        def write_email_text(self, text):
            self.clear_email()
            self.get_email_text_element().send_keys(text)

        def get_current_address_text_element(self):
            return self.find(By.XPATH, self.current_address)

        def clear_current_address(self):
            self.get_current_address_text_element().clear()

        def write_current_address_text(self, text):
            self.clear_current_address()
            self.get_current_address_text_element().send_keys(text)

        def get_permanent_address_text_element(self):
            return self.find(By.XPATH, self.permanent_address)

        def clear_permanent_address(self):
            self.get_permanent_address_text_element().clear()

        def write_permanent_address_text(self, text):
            self.clear_permanent_address()
            self.get_permanent_address_text_element().send_keys(text)

        def get_full_name_output_element(self):
            return self.find(By.XPATH, self.name_output)

        def wait_full_name_output(self):
            web_element_wait(page=self, condition=wait.VISIBILITY_OF, locator_type=By.XPATH,
                             locator=self.get_full_name_output_element, waiting_for="Name Output text")

        def get_full_name_output_text(self):
            #self.wait_full_name_output()
            return self.get_full_name_output_element().text

        def get_email_output_element(self):
            return self.find(By.XPATH, self.email_output)

        def wait_email_output(self):
            web_element_wait(page=self, condition=wait.VISIBILITY_OF, locator_type=By.XPATH,
                             locator=self.get_email_output_element, waiting_for="Email Output text")

        def get_email_out_text(self):
            #self.wait_email_output()
            return self.get_email_output_element().text

        def get_current_address_output_element(self):
            return self.find(By.XPATH, self.current_address_output)

        def wait_current_address_output(self):
            web_element_wait(page=self, condition=wait.VISIBILITY_OF, locator_type=By.XPATH,
                             locator=self.get_current_address_output_element, waiting_for="current address Output text")

        def get_current_address_output_text(self):
            #self.wait_current_address_output()
            return self.get_current_address_output_element().text

        def get_permanent_address_output_element(self):
            return self.find(By.XPATH, self.permanent_address_output)

        def wait_permanent_address_output(self):
            web_element_wait(page=self, condition=wait.VISIBILITY_OF, locator_type=By.XPATH,
                             locator=self.get_permanent_address_output_element,
                             waiting_for="Permanent address Output text")

        def get_permanent_address_output_text(self):
            #self.wait_permanent_address_output()
            return self.get_permanent_address_output_element().text
