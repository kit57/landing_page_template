import logging
import sys
from datetime import datetime

from pytz import timezone


def timetz(*args):
    return datetime.now(tz).timetuple()


tz = timezone("Europe/Berlin")


def init_logger(logger_name="landing_page_gen_logger", level=logging.INFO) -> logging.Logger:

    logger = logging.getLogger(logger_name)
    level = logging.getLevelName(level)
    logger.setLevel(level)

    TIMESTAMP_FORMAT = "%Y-%m-%d %H:%M:%S"

    formatter = logging.Formatter(
        "%(asctime)s - %(levelname)s - %(name)s  \t  %(message)s",
        datefmt=TIMESTAMP_FORMAT,
    )
    formatter.converter = timetz

    # console handler
    sh = logging.StreamHandler(sys.stdout)
    sh.setFormatter(formatter)
    logger.handlers.clear()
    logger.addHandler(sh)

    sys.excepthook = handle_exception  # type: ignore # log uncaught exceptions
    return logger


def handle_exception(exc_type: type, exc_value: NameError, exc_traceback):
    """Log uncaught exceptions (linked to sys.excepthook)
    Args:
        exc_type (type): Type of the exception
        exc_value (NameError): Value of the exception
        exc_traceback: Traceback of the exception
    """
    if issubclass(exc_type, KeyboardInterrupt):
        sys.__excepthook__(exc_type, exc_value, exc_traceback)
        return