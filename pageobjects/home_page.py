from selenium.webdriver.common.by import By

from base_class.base_class import BasePage


class HomePage(BasePage):
    element_button = "//h5[text()='Elements']/parent::div/preceding-sibling::div[1]"
    form_button = "//h5[text()='Forms']/parent::div/preceding-sibling::div[1]"
    alert_button = "//h5[text()='Alerts, Frame & Windows']/parent::div/preceding-sibling::div[1]"
    widgets_button = "//h5[text()='Widgets']/parent::div/preceding-sibling::div[1]"
    interactions_button = "// h5[text()='Interactions']/parent::div/preceding-sibling::div[1]"
    book_store_button = "// h5[text()='Book Store Application']/parent::div/preceding-sibling::div[1]"

    def __init__(self, driver):
        super().__init__(driver=driver)

    def get_element_button(self):
        return self.find(By.XPATH, self.element_button)

    def click_element_button(self):
        self.get_element_button().click()

    def get_form_button(self):
        return self.find(By.XPATH, self.form_button)

    def click_form_button(self):
        self.get_form_button().click()

    def get_alert_button(self):
        return self.find(By.XPATH, self.alert_button)

    def click_alert_button(self):
        self.get_alert_button().click()

    def get_widgets_button(self):
        return self.find(By.XPATH, self.widgets_button)

    def click_widgets_button(self):
        self.get_widgets_button().click()

    def get_interactions_button(self):
        return self.find(By.XPATH, self.interactions_button)

    def click_interactions_button(self):
        self.get_interactions_button().click()

    def get_book_store_button(self):
        return self.find(By.XPATH, self.book_store_button)

    def click_book_store_button(self):
        self.get_book_store_button().click()
