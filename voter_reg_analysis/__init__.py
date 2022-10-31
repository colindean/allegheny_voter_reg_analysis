import logging

import colorlog
from colorlog import ColoredFormatter


root_logger = logging.getLogger()
root_logger.setLevel(logging.INFO)


formatter = ColoredFormatter(
    "%(relativeCreated)-6d %(log_color)s%(levelname)-8s%(reset)s %(blue)s%(message)s",
    datefmt=None,
    reset=True,
    log_colors={
        "DEBUG": "cyan",
        "INFO": "green",
        "WARNING": "yellow",
        "ERROR": "red",
        "CRITICAL": "red,bg_white",
    },
    secondary_log_colors={},
    style="%",
)

handler = colorlog.StreamHandler()
handler.setFormatter(formatter)

root_logger.addHandler(handler)
