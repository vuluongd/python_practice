from http.server import BaseHTTPRequestHandler
import os 
class Server(BaseHTTPRequestHandler):
    def do_Get(self):
        if self.path == '/':
            self.path == '/index.html'

        try:
            split_path = os.path.splitext(self.path)
            request_extension = split_path[1]
            if request_extension != ".py":
                f = open(self.path[1:]).read()
                self.send_response(200)
                self.end_headers()
                self.wfile.write(bytes(f, 'utf-8'))
            else:
                f = "File not found"
                self.send_error(404,f)
        except:
            f = "File not found"
            self.send_error(404,f)

"""
BaseHTTPRequestHandler được sử dụng để xử lý các yêu cầu HTTP đến máy chủ.

Ngoài ra BaseHTTPRequestHandler còn hỗ trợ một số thuộc tính và phương thức sau:

do_GET(): Phương thức này xử lý khi có yêu cầu GET gửi lên.
do_POST(): Phương thức này xử lý khi có yêu cầu POST gửi lên.
path: Thuộc tính này trả về path của request.
send_error(): Phương thức này trả về lỗi HTTP cho client.
Đầu tiên định nghĩa một phương thứ do_GET(). Phương thức này chạy khi có một yêu cầu GET gửi lên.

self.path =='/' kiểm tra xem yêu cầu gửi lên có phải trang index hay không và nếu là trang index thì gán đường dẫn cho index self.path == '/index.html`.

Tiếp theo cố gắng đọc các tệp mà người dùng đang cố truy cập ngoại trừ những file python tránh làm lộ source code.

Nếu tập tin yêu cầu được tìm thấy thì server gửi phản hồi 200. 200 là phản hồi mà bất cứ khi nào bạn truy cập thành công một trang web.

Nếu tập tin yêu cầu không được tìm thấy thì server gửi một mã lỗi tập tin yêu cầu không hợp lệ.

Sử dụng phương thức bytes() encode utf-8 để chuyển đổi dạng văn bản sang bytes.
"""


