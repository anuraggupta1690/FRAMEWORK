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


def web_element_wait(**kwargs):
    """
    Function which returns web element
    :param kwargs:
    :return:
    """
    timeout = kwargs.get('timeout', 30)
    poll_frequency = kwargs.get('sleep_seconds', 0.5)
    ignored_exceptions = kwargs.get('expected_exceptions', (WebDriverException, UnexpectedAlertPresentException))
    waiting_for = kwargs.get("waiting_for", '')
    page_instance = kwargs.get('page')
    condition = expected_conditions(condition=kwargs.get('condition'))
    try:
        return WebDriverWait(driver=page_instance.driver, timeout=timeout, poll_frequency=poll_frequency,
                             ignored_exceptions=ignored_exceptions).until(condition((kwargs.get('locator'),
                                                                                     kwargs.get('locator_type'))))
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
    timeout = kwargs.get('timeout', 30)
    poll_frequency = kwargs.get('sleep_seconds', 0.5)
    ignored_exceptions = kwargs.get('expected_exceptions', (WebDriverException, UnexpectedAlertPresentException))
    waiting_for = kwargs.get("waiting_for", '')
    page_instance = kwargs.get('page')
    condition = expected_conditions(condition=kwargs.get('condition'))
    expected_value = kwargs.get('expected_value')
    if expected_value:
        condition = condition(expected_value)
    else:
        condition = condition()
    try:
        if WebDriverWait(driver=page_instance.driver, timeout=timeout, poll_frequency=poll_frequency,
                         ignored_exceptions=ignored_exceptions).until(condition):
            pass
        else:
            raise Exception
    except Exception as exe:
        log.info("Exception raised: %s", exe)
        log.info("waiting for: %s", waiting_for)
        raise TimeoutException(msg="waiting for {}".format(waiting_for))


def expected_conditions(condition):
    return getattr(EC, condition)
