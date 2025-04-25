import sys


def supports_unicode():
    # Kiểm tra xem hệ thống có hỗ trợ Unicode (và emoji) không
    return sys.stdout.encoding.lower() in ["utf-8", "utf-16"]


def post_to_facebook(download, upload):
    # Kiểm tra nếu hệ thống hỗ trợ Unicode (emoji)
    if supports_unicode():
        status = f"""
        My internet is dropping harder than my mood at the end of the month 😤
        Download: {download:.2f} Mbps (Promised: 500 Mbps)
        Upload: {upload:.2f} Mbps (Promised: 500 Mbps)
        Can someone tag the ISP's technician for me? I'm too tired for this 😩
        """
    else:
        status = f"""
        My internet is dropping harder than my mood at the end of the month [MOOD]
        Download: {download:.2f} Mbps (Promised: 500 Mbps)
        Upload: {upload:.2f} Mbps (Promised: 500 Mbps)
        Can someone tag the ISP's technician for me? I'm too tired for this [SAD_FACE]
        """

    # Use Selenium or FB Graph API to post the status
    print("[FB] Publicly roasted the ISP.")
