"""
Module contains generic utilities functions by Anurag Gupta
 :date: Sep 19, 2020
 :author: Anurag Gupta

"""
import random
import string

from lib.helper import wait
from lib.helper.wait import web_condition_wait


def execute_js_script(driver, script):
    """ example of common scripts:
 (arguments[0].click(); , web_element) -> will click on that element
 (return document.title;) - > returns the page title like driver .title
 (history.go(0);) -> refresh page
 (alert.("Alert message");) -> pop up a alert
(return document.documentElement.innerText;) - > returns the all inner text of page
(arguments[0].style.border = '3px solid red', web_element) -> highlight border line of given element
(window.scrollTo(0, document.body.scrollHeight) -> scroll to page bottom and for scroll up reverse the arguments
(window.scrollTo(argument[0].scrollIntoView(true);, web_element) -> scroll to page bottom and for scroll up reverse the
arguments
("window.scrollBy(100, 100);") - > scroll by 100 by 100
("document.body.style_zoom='150%'") to zoom
(return navigator.userAgent;) -> return user agent

"""
    return driver.execute_script(script)

def take_screen_shot(driver, file_path, full_page=False):
    if full_page:
        s = lambda x: execute_js_script(driver, 'return document.body.parentNode.scroll'+x)
        driver.set_window_size(s('Width'), s('Height'))
        driver.find_element_by_tag_name('body').screenshot(file_path)
    else:
        driver.get_screenshot_as_file(file_path)


def switch_alert(driver):
    web_condition_wait(driver=driver, condition=wait.ALERT_IS_PRESENT, waiting_for="Alert")
    alert = driver.switch_to_alert()
    return alert


def get_alert_text(driver):
    return switch_alert(driver).text


def alert_operation(driver, ok=False):
    alert = switch_alert(driver)
    if ok:
        alert.accept()
    else:
        alert.dismiss()

def random_name(prefix="Automation"):
    return prefix+" "+''.join(random.choice(string.ascii_letters) for i in range(5))