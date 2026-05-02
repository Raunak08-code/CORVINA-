import logging
import os

def get_logger():
    logger = logging.getLogger("corvina")

    if not logger.handlers:
        logger.setLevel(logging.INFO)

        os.makedirs("logs", exist_ok=True)

        file_handler = logging.FileHandler("logs/app.log")
        formatter = logging.Formatter(
            "%(asctime)s | %(levelname)s | %(message)s"
        )
        file_handler.setFormatter(formatter)

        logger.addHandler(file_handler)

    return logger