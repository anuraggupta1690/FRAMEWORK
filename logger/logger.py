"""
Logger file Designed by Anurag Gupta
 :date: Aug 09, 2020
 :author: Anurag Gupta
"""
import logging
import path


class Logger:
    @staticmethod
    def create_logger():
        logging.basicConfig(filename="{}/logs/automation.log".format(path.get_project_path()),
                            format='%(asctime)s: %(levelname)s: %(message)s', datefmt='%m/%d/%y %I:%M:%S %p')
        log = logging.getLogger()
        log.setLevel(logging.INFO)
        return log
