import logging
from datetime import datetime
import os

# Đảm bảo thư mục logs tồn tại
LOG_DIR = "logs"
os.makedirs(LOG_DIR, exist_ok=True)

# Tạo tên file log theo ngày
log_filename = os.path.join(LOG_DIR, f"log_{datetime.now().strftime('%Y-%m-%d')}.log")

# Cấu hình logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    handlers=[
        logging.FileHandler(log_filename, encoding="utf-8"),
        logging.StreamHandler(),  # In ra console
    ],
)


def log_info(message):
    logging.info(message)


def log_warning(message):
    logging.warning(message)


def log_error(message):
    logging.error(message)
