import logging
import os


def get_logger():
    logger = logging.getLogger("wpflog")
    logger.setLevel(logging.INFO)

    curr_path = os.path.abspath(__file__)
    dir = os.path.dirname(os.path.dirname(curr_path))
    # 每次被调用后，清空已经存在handler
    logger.handlers.clear()
    handler = logging.FileHandler(filename=dir+"/report/logger.txt")
    handler.setLevel(logging.INFO)
    handler.setFormatter(logging.Formatter("[%(asctime)s] - [%(levelname)s] - %(message)s"))

    logger.addHandler(handler)
    return logger
#
# a ="dfjsafhjkafhjkfsda"
# get_logger().info(a)