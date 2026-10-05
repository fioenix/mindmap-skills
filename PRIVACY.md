# Chính sách bảo mật & Quyền riêng tư (Privacy Policy)

`mindmap-skills` được thiết kế theo kiến trúc phi tập trung, ưu tiên bảo mật và tôn trọng tuyệt đối quyền riêng tư của người dùng:

## 1. Không thu thập & Không gửi dữ liệu ngoài

- **Zero-Backend**: Skill và plugin không sở hữu bất kỳ máy chủ backend, API endpoint thu thập dữ liệu hay cơ chế telemetry/analytics nào.
- **Local & In-Agent Execution**: Quá trình phân tích, trích xuất cấu trúc mindmap và tạo file `.mindmap.md` diễn ra hoàn toàn nội bộ trong ngữ cảnh của mô hình ngôn ngữ trên host (Claude, Codex, Antigravity).
- **Zero-Dependency Rendering**: File HTML độc lập sử dụng mẫu template tĩnh nhúng sẵn hoặc tải CDN công khai mã nguồn mở (Markmap / D3 qua jsDelivr) hoặc render 100% offline bằng `scripts/render.sh` không kết nối mạng.

## 2. Kiểm soát dữ liệu đầu vào

- Quy trình chỉ xử lý văn bản, tài liệu, ghi chú hoặc mã nguồn do người dùng chủ động cung cấp trong phiên làm việc.
- **Khuyến nghị an toàn**: Người dùng không nên cung cấp dữ liệu thẻ tín dụng (PCI DSS), thông tin định danh chính phủ, mật khẩu, private key, session token hoặc dữ liệu cá nhân nhạy cảm vào prompt. Nếu phát hiện các thông tin nhạy cảm này, quy trình khuyến cáo agent dừng phân tích và yêu cầu phiên bản đã được ẩn danh (anonymized).

## 3. Dữ liệu trên nền tảng máy chủ AI Host

- Mọi tương tác prompt và file tạo ra được quản lý theo chính sách quyền riêng tư và điều khoản sử dụng của nền tảng mà bạn đang chạy (Anthropic Claude, OpenAI Codex, Google Antigravity).
- Repository và maintainer không có quyền truy cập, can thiệp hay kiểm soát dữ liệu trên tài khoản người dùng của các nền tảng trên.

## 4. Đóng góp & Báo cáo lỗi

Khi đóng góp ca lỗi (bug report) hoặc mở issue trên GitHub, người dùng chỉ gửi các văn bản, mã nguồn mẫu hoặc sơ đồ đã được ẩn danh hoàn toàn, không chứa thông tin bí mật kinh doanh hay dữ liệu thực tế của doanh nghiệp.

Liên hệ về các vấn đề quyền riêng tư thông qua [GitHub Issues](https://github.com/fioenix/mindmap-skills/issues).
