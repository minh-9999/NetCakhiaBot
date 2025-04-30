# 📶 NetCakhiaBot

NetCakhiaBot là một bot Python được thiết kế để **giám sát tốc độ Internet** và **tự động nhắc nhở nhà mạng** khi tốc độ thực tế thấp hơn mức cam kết trong hợp đồng. Hữu ích cho người dùng cá nhân hoặc doanh nghiệp muốn đòi lại quyền lợi khi mạng "cá khịa".

## 💡 Ý tưởng

Các nhà mạng thường cam kết "tốc độ tối đa lên đến XX Mbps", nhưng thực tế lại... không như mơ. NetCakhiaBot sẽ:

- Đo tốc độ mạng định kỳ.
- So sánh với mức cam kết.
- Gửi email/nhắn tin/ghi log khi phát hiện bất thường.
- Có thể mở rộng để gửi khiếu nại tự động (email, webform...).

## ⚙️ Tính năng

- ⏱️ Đo tốc độ mạng bằng `speedtest-cli`.
- 📊 So sánh tốc độ với mức cam kết tối thiểu.
- 📩 Gửi cảnh báo qua email hoặc Telegram (tuỳ cấu hình).
- 📅 Chạy định kỳ bằng cron hoặc scheduler tích hợp.
- 🧠 Ghi log lịch sử và phân tích thống kê nếu cần.

## 🛠️ Cài đặt

```bash
git clone https://github.com/minh-9999/NetCakhiaBot.git
cd NetCakhiaBot
pip install -r requirements.txt
```

## 📝 Cấu hình

Tạo file .env hoặc config.json với các thông tin sau:  
` .env`  
PROMISED_DOWNLOAD_MBPS=tocdocamketnhamang  
PROMISED_UPLOAD_MBPS=tocdocamketnhamang  
EMAIL_RECEIVER=cs@nhamang.vn  
EMAIL_SENDER=your.email@gmail.com  
EMAIL_PASSWORD=your_app_password  
ALERT_THRESHOLD_PERCENT=80 # Báo khi dưới 80% cam kết

## ▶️ Sử dụng

python main.py

## 📈 Tính năng mở rộng (gợi ý)

Gửi đơn khiếu nại trực tiếp đến nhà mạng qua API hoặc email template.

Giao diện Web hoặc Telegram Bot để xem lịch sử đo tốc độ.

Biểu đồ thống kê bằng Matplotlib hoặc Streamlit.

## 🤖 Yêu cầu hệ thống

Python 3.7+

speedtest-cli

Kết nối Internet (dĩ nhiên)

SMTP nếu muốn gửi email

## 🧠 Ghi chú

NetCakhiaBot không đại diện pháp lý. Đây là công cụ hỗ trợ người dùng bảo vệ quyền lợi. Đừng lạm dụng hoặc spam.

## 📜 Giấy phép

Apache License
