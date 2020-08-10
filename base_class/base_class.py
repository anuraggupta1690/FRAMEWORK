from lib.configurations.environment_variables import ReadConfigFile


class BasePage:
    def __init__(self, driver, url=ReadConfigFile.get_base_url()):
        self.driver = driver
        self.url = url

    @property
    def driver(self):
        return self.__driver

    @driver.setter
    def driver(self, driver):
        self.__driver = driver

    @property
    def url(self):
        return self.__url

    @url.setter
    def url(self, url):
        self.__url = url

    def find(self, locator_type, locator):
        return self.driver.find_element(locator_type, locator)

    def open_url(self):
        self.driver.get(self.url)
