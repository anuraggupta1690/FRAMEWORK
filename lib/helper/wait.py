"""
Wait module Designed by Anurag Gupta
 :date: Aug 12, 2020
 :author: Anurag Gupta
"""
from selenium.common.exceptions import UnexpectedAlertPresentException, WebDriverException, TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from logger.logger import Logger

log = Logger.create_logger()

TITLE_IS = 'title_is'
TITLE_CONTAINS = 'title_contains'
PRESENCE_OF_ELEMENT_LOCATED = 'presence_of_element_located'
VISIBILITY_OF_ELEMENT_LOCATED = 'visibility_of_element_located'
VISIBILITY_OF = 'visibility_of'
PRESENCE_OF_ALL_ELEMENTS_LOCATED = 'presence_of_all_elements_located'
TEXT_TO_BE_PRESENT_IN_ELEMENT = 'text_to_be_present_in_element'
TEXT_TO_BE_PRESENT_IN_ELEMENT_VALUE = 'text_to_be_present_in_element_value'
FRAME_TO_BE_AVAILABLE_AND_SWITCH_TO_IT = 'frame_to_be_available_and_switch_to_it'
INVISIBILITY_OF_ELEMENT_LOCATED = 'invisibility_of_element_located'
ELEMENT_TO_BE_CLICKABLE = 'element_to_be_clickable'
STALENESS_OF = 'staleness_of'
ELEMENT_TO_BE_SELECTED = 'element_to_be_selected'
ELEMENT_LOCATED_TO_BE_SELECTED = 'element_located_to_be_selected'
ELEMENT_SELECTION_STATE_TO_BE = 'element_selection_state_to_be'
ELEMENT_LOCATED_SELECTION_STATE_TO_BE = 'element_located_selection_state_to_be'
ALERT_IS_PRESENT = 'alert_is_present'


def web_driver_wait(**kwargs):
    timeout = kwargs.get('timeout', 30)
    poll_frequency = kwargs.get('sleep_seconds', 0.5)
    ignored_exceptions = kwargs.get('expected_exceptions', (WebDriverException, UnexpectedAlertPresentException))
    driver = kwargs.get('driver')

    return WebDriverWait(driver=driver, timeout=timeout, poll_frequency=poll_frequency,
                         ignored_exceptions=ignored_exceptions)


def web_element_wait(**kwargs):
    """
    Function which returns web element
    :param kwargs:
    :return:
    """
    condition = expected_conditions(condition=kwargs.get('condition'))
    locator = kwargs.get('locator')
    locator_type = kwargs.get('locator_type')
    waiting_for = kwargs.get('waiting_for')

    try:
        wait = web_driver_wait(driver=kwargs.get('driver'), timeout=kwargs.get('timeout', 30),
                               poll_frequency=kwargs.get('poll_frequency', 0.5),
                               ignored_exceptions=kwargs.get('ignored_exceptions',
                                                             (WebDriverException, UnexpectedAlertPresentException)))
        return wait.until(condition((locator_type, locator)))
    except TimeoutException as exe:
        log.info("Timeout Exception raised: %s", exe)
        log.info("waiting for: %s", waiting_for)
        raise TimeoutException


def web_condition_wait(**kwargs):
    """
    Function which returns True and false based on condition
    :param kwargs:
    :return:
    """
    condition = expected_conditions(condition=kwargs.get('condition'))
    expected_value = kwargs.get('expected_value')
    waiting_for = kwargs.get('waiting_for')

    try:
        wait = web_driver_wait(driver=kwargs.get('driver'), timeout=kwargs.get('timeout', 30),
                               poll_frequency=kwargs.get('poll_frequency', 0.5),
                               ignored_exceptions=kwargs.get('ignored_exceptions',
                                                             (WebDriverException, UnexpectedAlertPresentException)))
        value = False
        if expected_value:
            if wait.until(condition(expected_value)):
                value = True
        else:
            if wait.until(condition()):
                value = True
        return value
    except Exception as e:
        raise TimeoutException(msg=waiting_for+" Not Found")

def expected_conditions(condition):
    return getattr(EC, condition)
