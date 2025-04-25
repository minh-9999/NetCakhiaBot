import smtplib
from config import EMAIL_RECEIVER


def send_complaint_email(download, upload):
    subject = "Internet speed below promised rate"
    body = f"""
    Dear ISP Support,

    I'm currently subscribed to a package that promises 500Mbps download and 500Mbps upload.
    However, my recent speed test shows:
    - Download: {download:.2f} Mbps
    - Upload: {upload:.2f} Mbps

    Please investigate this issue and respond as soon as possible.

    Best regards — but also seriously,
    A customer who is truly dissatisfied
    """

    print(f"[Email] Complaint sent to {EMAIL_RECEIVER}")
