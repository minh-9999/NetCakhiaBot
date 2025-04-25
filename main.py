import schedule
import time
from speed_monitor import check_internet_speed
from log_utils import log_info
import sys


def supports_unicode():
    # Kiểm tra xem hệ thống có hỗ trợ Unicode (và emoji) không
    return sys.stdout.encoding.lower() in ["utf-8", "utf-16"]


def main():
    rocket = "🚀" if supports_unicode() else "[START]"
    log_info(f"{rocket} Starting NetCaKhiaBot...")

    # Kiểm tra mỗi 15 phút
    schedule.every(15).minutes.do(check_internet_speed)

    while True:
        schedule.run_pending()
        time.sleep(1)


if __name__ == "__main__":
    main()
