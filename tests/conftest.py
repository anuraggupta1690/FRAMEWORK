import pytest
from selenium.webdriver import Firefox

import path
from logger.logger import Logger

log = Logger.create_logger()


@pytest.fixture()
def driver_instance(browser):
    driver = None
    if browser == "ff":
        driver = Firefox(executable_path="{}/driver/geckodriver.exe".format(path.get_project_path()))
        log.info(" Fire Fox Web driver object is created ")
    driver.maximize_window()
    log.info(" Browser is maximised ")
    yield driver
    driver.quit()
    log.info(" Browser is closed ")


def pytest_addoption(parser):
    parser.addoption("--browser")


@pytest.fixture()
def browser(request):
    return request.config.getoption("--browser")
