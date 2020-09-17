"""
Web Driver instance module Designed by Anurag Gupta
 :date: Aug 12, 2020
 :author: Anurag Gupta
"""
from selenium.webdriver import Firefox, Ie, Chrome
from selenium import webdriver
import path
from  webdriver_manager import firefox, chrome, microsoft


class WebDriverInstance:

    @staticmethod
    def get_web_driver_instance(browser_type, headless):
        driver = None
        if browser_type == "ff":
            option = webdriver.FirefoxOptions()
            option.headless = False
            if headless == "True":
                option.headless = True
            driver = Firefox(executable_path="{}/drivers/geckodriver.exe".format(path.get_project_path()),
                             options=option)
        elif browser_type == "ie":
            option = webdriver.IeOptions()
            option.headless = False
            if headless == "True":
                option.headless = True
            driver = Ie(executable_path=microsoft.IEDriverManager().install(), options=option)
        elif browser_type == "chrome":
            option = webdriver.ChromeOptions()
            option.headless = False
            #option.add_argument("--incognito")
            option.add_argument("--headless")

            if headless == "True":
                option.headless = True
            driver = Chrome(executable_path=chrome.ChromeDriverManager().install(), options=option)
        return driver
