import pytest

from base_class.wait import web_condition_wait, web_element_wait
from base_class import wait
from lib.configurations.environment_variables import ReadConfigFile
from lib.urls.page_details_constants import PageURLs
from logger.logger import Logger
from pageobjects.home_page import HomePage
from selenium.webdriver.common.by import By

log = Logger.create_logger()


class TestElements:
    @pytest.mark.smock
    def test_verify_user_can_view_elements_page(self, driver_instance):
        hp = HomePage(driver=driver_instance)
        hp.open_url()
        web_element_wait(page=hp, condition=wait.ELEMENT_TO_BE_CLICKABLE, locator_type=By.XPATH,
                         locator=hp.element_button, waiting_for="Element Button")

        # web_condition_wait(page=hp, condition=wait.TITLE_IS, waiting_for="Element Button Page", expected_value="ToolsQA")
        # web_condition_wait(page=hp, condition=wait.ALERT_IS_PRESENT, waiting_for="Alert")

        hp.click_element_button()
        assert hp.driver.current_url == "{}{}".format(ReadConfigFile.get_base_url(), PageURLs.elements_page), \
            "Failed to view the element pages"
    @pytest.mark.regression
    def test_verify_user_can_view_form_page(self, driver_instance):
        log.info("***"*5 + " test_verify_user_can_view_form_page started " + "***"*5)
        hp = HomePage(driver=driver_instance)
        hp.open_url()
        log.info(" %s opened ", ReadConfigFile.get_base_url())
        hp.click_form_button()
        assert hp.driver.current_url == "{}{}".format(ReadConfigFile.get_base_url(), PageURLs.forms_page), \
            "Failed to view the forms pages"
        log.info(" %s opened ", "{}{}".format(ReadConfigFile.get_base_url(),
                                              PageURLs.forms_page))
        log.info("***"*5 + " test_verify_user_can_view_form_page finished " + "***"*5)

    @pytest.mark.smock
    def test_verify_user_can_view_alert_page(self, driver_instance):
        hp = HomePage(driver=driver_instance)
        hp.open_url()
        hp.click_alert_button()
        assert hp.driver.current_url == "{}{}".format(ReadConfigFile.get_base_url(), PageURLs.alert_window_page), \
            "Failed to view the Alert window pages"

    @pytest.mark.senity
    def test_verify_user_can_view_widgets_page(self, driver_instance):
        hp = HomePage(driver=driver_instance)
        hp.open_url()
        hp.click_widgets_button()
        assert hp.driver.current_url == "{}{}".format(ReadConfigFile.get_base_url(), PageURLs.widgets_page), \
            "Failed to view the Alert window pages"

    @pytest.mark.senity
    def test_verify_user_can_view_interactions_page(self, driver_instance):
        hp = HomePage(driver=driver_instance)
        hp.open_url()
        hp.click_interactions_button()
        assert hp.driver.current_url == "{}{}".format(ReadConfigFile.get_base_url(), PageURLs.interaction_page), \
            "Failed to view the Alert window pages"
