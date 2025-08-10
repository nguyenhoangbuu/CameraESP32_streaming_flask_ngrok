#Camera streaming
Truyền video giám sát từ camera ESP32 lên websize thông qua flask API và nền tảng Ngrok để có thể xem từ xa.
##Model
##Output example
##Sử dụng#Camera streaming
Truyền video giám sát từ camera ESP32 lên websize thông qua flask API và nền tảng Ngrok để có thể xem từ xa.
##Model
Xây dựng mô hình phát hiện người từ hình ảnh thu được của camera và gửi hình ảnh người đó về bot Telegram. <br>
APi Flask được sử dụng để ứng dụng video từ camera lên websize và truyền phát trực tiếp qua nền tảng Ngrok. <br>
Sử dụng các thư viện như: flask, opencv-python, ultralytics, python-telegram-bot, asyncio, nest_asyncio
##Output example
![screenshot](https://github.com/nguyenhoangbuu/CameraESP32_streaming_flask_ngrok/blob/master/ESP32_image1.png)
![screenshot](https://github.com/nguyenhoangbuu/CameraESP32_streaming_flask_ngrok/blob/master/ESP32_image2.png)
##Sử dụng
Sở hữu và lắp đặt camera ESP32 tại vị trí thích hợp. <br>
Truyền hình ảnh thu được từ ESP32 về máy tính thông qua wifi với Arduino IDE. <br>
Xây dựng ứng dụng web với Flask API. <br>
Đăng ký tài khoản trên nền tảng Ngrok và truyền phát trực tiếp video từ camera. <br>
Ví dụ code chạy ứng dụng:
`python app.py` <br>
`ngrok http 5000`
