"""
Web Driver instance module Designed by Anurag Gupta
 :date: Aug 12, 2020
 :author: Anurag Gupta
"""
from selenium.webdriver import Firefox, Ie
import path


class WebDriverInstance:

    @staticmethod
    def get_web_driver_instance(browser_type):
        driver = None
        if browser_type == "ff":
            driver = Firefox(executable_path="{}/drivers/geckodriver.exe".format(path.get_project_path()))
        elif browser_type == "ie":
            driver = Ie(executable_path="{}/drivers/IEDriverServer.exe".format(path.get_project_path()))
        elif browser_type == "op":
            driver = Ie(executable_path="{}/drivers/selenium-opera-driver.exe".format(path.get_project_path()))
        return driver
