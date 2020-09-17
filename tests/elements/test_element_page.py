"""
UI Test Designed by Anurag Gupta
 :date: Aug 16, 2020
 :author: Anurag Gupta
"""

import pytest

from pageobjects.elements_page import ElementPage


class TestElementPage:

    def test_verify_user_can_type_text_in_box(self, driver_instance):
        full_name = "anuragGupta"
        email = "email@email.com"
        per_add = "qwert"
        curr_add = "asdf"
        hp = ElementPage(driver=driver_instance)
        hp.open_url()
        hp.click_text_box_button()
        tb = hp.TextBox(driver=driver_instance)
        tb.write_full_name(text=full_name)
        tb.write_email_text(text=email)
        tb.write_current_address_text(text=curr_add)
        tb.write_permanent_address_text(text=per_add)
        tb.click_submit_button()
        assert full_name in tb.get_full_name_output_text()
        assert email in tb.get_email_out_text()
        assert curr_add in tb.get_current_address_output_text()
        assert per_add in tb.get_permanent_address_output_text()
