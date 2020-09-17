import pytest

from base_class.web_driver_instance import WebDriverInstance
from logger.logger import Logger

log = Logger.create_logger()


@pytest.fixture()
def driver_instance(browser, headless):
    driver = WebDriverInstance.get_web_driver_instance(browser, headless)
    driver.maximize_window()
    log.info(" Browser is maximised ")
    yield driver
    driver.quit()
    log.info(" Browser is closed ")


def pytest_addoption(parser):
    parser.addoption("--browser")
    parser.addoption("--headless")

@pytest.fixture()
def browser(request):
    return request.config.getoption("--browser")

@pytest.fixture()
def headless(request):
    return request.config.getoption("--headless")
