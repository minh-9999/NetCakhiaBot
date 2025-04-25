import speedtest
import sys
from config import *
from fb_post import post_to_facebook
from email_utils import send_complaint_email
from voice_call import call_isp
from log_utils import log_info, log_warning


def supports_unicode():
    # Kiểm tra xem hệ thống có hỗ trợ Unicode (và emoji) không
    return sys.stdout.encoding.lower() in ["utf-8", "utf-16"]


def check_internet_speed():  # sourcery skip: extract-method
    magnifier = "🔍" if supports_unicode() else "[CHECK]"
    gear = "⚙️" if supports_unicode() else "[RESULT]"
    stop = "🛑" if supports_unicode() else "[WARNING]"
    check = "✅" if supports_unicode() else "[OK]"
    warn = "⚠️" if supports_unicode() else "[ERROR]"

    log_info(f"{magnifier} Checking internet speed...")

    try:
        st = speedtest.Speedtest()
        st.get_best_server()
        download = st.download() / 1_000_000  # Convert to Mbps
        upload = st.upload() / 1_000_000

        log_info(
            f"{gear} Result: Download {download:.2f} Mbps, Upload {upload:.2f} Mbps"
        )

        if (
            download < COMMITED_DOWNLOAD_MBPS * 0.8
            or upload < COMMITED_UPLOAD_MBPS * 0.8
        ):
            log_warning(
                f"{stop} Internet speed is below the committed rate! Triggering roast protocol."
            )
            post_to_facebook(download, upload)
            send_complaint_email(download, upload)
            call_isp(download, upload)
        else:
            log_info(f"{check} Connection is stable. No action needed.")

    except Exception as e:
        log_warning(f"{warn} Error while testing internet speed: {e}")
