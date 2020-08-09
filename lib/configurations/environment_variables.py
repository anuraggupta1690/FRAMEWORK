"""
Configuration file Designed by Anurag Gupta
 :date: Aug 09, 2020
 :author: Anurag Gupta
"""

import configparser

import path

config = configparser.RawConfigParser()
config.read("{}/lib/configurations/config.ini".format(path.get_project_path()))


class ReadConfigFile:

    @staticmethod
    def get_base_url():
        return config.get("demo_qa", "url")
