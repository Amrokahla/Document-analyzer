# backend/core/logging_config.py
import logging
import os
from logging.handlers import RotatingFileHandler

def configure_logging(level: str = None):
    root = logging.getLogger()
    if root.handlers:
        return  # already configured

    log_level = (level or os.getenv("LOG_LEVEL", "INFO")).upper()
    root.setLevel(getattr(logging, log_level, logging.INFO))

    ROOT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
    LOG_DIR = os.path.join(ROOT_DIR, "logs")
    os.makedirs(LOG_DIR, exist_ok=True)
    log_file = os.path.join(LOG_DIR, "app.log")

    fmt = "%(asctime)s %(levelname)s %(name)s %(message)s"
    formatter = logging.Formatter(fmt)

    sh = logging.StreamHandler()
    sh.setFormatter(formatter)
    sh.setLevel(getattr(logging, log_level, logging.INFO))

    fh = RotatingFileHandler(log_file, maxBytes=5 * 1024 * 1024, backupCount=5)
    fh.setFormatter(formatter)
    fh.setLevel(getattr(logging, log_level, logging.INFO))

    root.addHandler(sh)
    root.addHandler(fh)
