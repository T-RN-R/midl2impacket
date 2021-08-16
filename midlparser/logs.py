import logging
import logging.handlers
import pathlib

LIMIT_1_MB = 1024 * 256 * 1
LOG_DIR = pathlib.Path(__file__).parent / "logs"
INITIALIZED = False
DEFAULT_LEVEL = logging.ERROR

 
class ColorFormatter(logging.Formatter):

    # Format
    log_format = "[%(name)s:%(funcName)s(%(filename)s:%(lineno)s) %(levelname)+9s]: %(message)s"

    # Colors
    grey = "\x1b[38;21m"
    yellow = "\x1b[33;21m"
    red = "\x1b[31;21m"
    bold_red = "\x1b[31;1m"
    reset = "\x1b[0m"
    
    COLORS = {
        logging.DEBUG: grey,
        logging.INFO: grey,
        logging.WARNING: yellow,
        logging.ERROR: red,
        logging.CRITICAL: bold_red,
    }

    def __init__(self, fmt=None, datefmt=None, style='%', validate=True) -> None:
        super().__init__(fmt=fmt or self.log_format, datefmt=datefmt, style=style, validate=validate)

    def formatMessage(self, record: logging.LogRecord) -> str:
        if record.exc_info:
            fmt_ext = self.formatException(record.exc_info, internal=True)
            record.message = fmt_ext
        s = super().formatMessage(record)
        return self.COLORS[record.levelno] + s + self.reset

    def formatException(self, ei, internal=False):
        if internal:
            s = super().formatException(ei)
            return self.COLORS[logging.ERROR] + s + self.reset
        return ""


def init_logging(level=DEFAULT_LEVEL, log_dir: pathlib.Path = LOG_DIR, log_to_file=False):

    formatter = ColorFormatter()
    root_logger = logging.getLogger()
    console = logging.StreamHandler()
    console.setFormatter(formatter)
    console.setLevel(level)
    root_logger.addHandler(console)
    root_logger.setLevel(level)
    if log_to_file:
        log_dir.mkdir(exist_ok=True)
        log_path = log_dir / "parser.log"
        file_handler = logging.handlers.RotatingFileHandler(
            log_path, maxBytes=LIMIT_1_MB, backupCount=10, mode="a+"
        )
        file_handler.setFormatter(formatter)
        file_handler.setLevel(level)
        root_logger.addHandler(file_handler)

def get_logger(logger_name: str, level=DEFAULT_LEVEL):
    global INITIALIZED
    if not INITIALIZED:
        init_logging()
        INITIALIZED = True
    logger = logging.getLogger(logger_name.lower())
    logger.setLevel(level)
    return logger
