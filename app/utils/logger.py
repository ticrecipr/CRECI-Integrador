from pathlib import Path
from datetime import datetime
import logging


class Logger:

    def __init__(self):

        root = Path(__file__).resolve().parents[2]

        log_dir = root / "logs"

        log_dir.mkdir(exist_ok=True)

        log_file = log_dir / f"{datetime.now():%Y-%m-%d}.log"

        self.logger = logging.getLogger("CRECI")

        self.logger.setLevel(logging.INFO)

        if not self.logger.handlers:

            formatter = logging.Formatter(
                "%(asctime)s | %(levelname)s | %(message)s"
            )

            file_handler = logging.FileHandler(
                log_file,
                encoding="utf-8"
            )

            file_handler.setFormatter(formatter)

            console_handler = logging.StreamHandler()

            console_handler.setFormatter(formatter)

            self.logger.addHandler(file_handler)

            self.logger.addHandler(console_handler)

    def info(self, mensagem: str):
        self.logger.info(mensagem)

    def warning(self, mensagem: str):
        self.logger.warning(mensagem)

    def error(self, mensagem: str):
        self.logger.error(mensagem)