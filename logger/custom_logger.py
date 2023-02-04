import logging
import inspect
import os


def get_logger(file_name, log_level=logging.NOTSET,
               _format="%(asctime)s: %(levelname)s: %(name)s: %(message)s", _datefmt='%d/%m/%Y %H:%M:%S'):
    logger = logging.getLogger(file_name)
    file_logger = logging.FileHandler(filename=f"{file_name}.log", mode='w')
    formatter = logging.Formatter(_format, datefmt=_datefmt)
    file_logger.setFormatter(formatter)
    logger.addHandler(file_logger)
    logger.setLevel(level=log_level)
    return logger

def f1():
    log1 = get_logger(file_name="f1", log_level=logging.WARNING)
    log1.debug("f1 debug")
    log1.warning("f1 warning")
    log1.error("f1 error")
    log1.critical("f1 critical")

def f2():
    log2 = get_logger(file_name="f2", log_level=logging.WARNING)
    log2.debug("f2 debug")
    log2.warning("f2 warning")
    log2.error("f2 error")
    log2.critical("f2 critical")

f1()
f2()
