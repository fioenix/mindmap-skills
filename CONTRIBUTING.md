# Đóng góp cho mindmap-skills (Contributing Guide)

Cảm ơn bạn đã quan tâm đóng góp cho `mindmap-skills`! Mọi đóng góp nhằm cải thiện chất lượng cấu trúc sơ đồ tư duy, cú pháp Markmap, độ tin cậy hiển thị hoặc tính bảo mật đều được hoan nghênh.

## 1. Nguyên tắc cốt lõi

1. **Cognitive First**: Mọi thay đổi trong quy tắc cấu trúc (`SKILL.md`) phải bảo toàn nguyên tắc nhận thức của con người (Miller's Law: 4–7 nhánh chính, độ sâu tối đa 3–4 tầng, mỗi nút ≤ 8 từ).
2. **Zero-Daemon & Zero-Token-Tax**: Không đưa vào các server nền cồng kềnh (như daemon Playwright/Chromium) hay các middleware làm phát sinh token tax không cần thiết trong các turn hội thoại.
3. **Multi-Agent Parity**: Bảo đảm tính tương thích đồng thời trên cả ba nền tảng: Claude Code, OpenAI Codex và Google Antigravity.
4. **An toàn bảo mật**: Mẫu template HTML phải duy trì Content Security Policy (CSP) nghiêm ngặt và thoát chuỗi an toàn chống XSS/DOM injection.

## 2. Kiểm thử cục bộ (Offline Validation)

Trước khi gửi pull request hoặc tạo commit, hãy chạy toàn bộ bộ kiểm chứng:

```bash
# Chạy bộ test suite toàn diện
npm test
# hoặc
bash tests/validate.sh

# Kiểm tra strict Claude Code manifest nếu máy có cài claude CLI
claude plugin validate --strict .
```

Bộ kiểm tra sẽ tự động rà soát:
- Cú pháp và schema của tất cả các manifest JSON (`package.json`, `plugin.json`, `.claude-plugin/`, `.codex-plugin/`, `.agents/`).
- Giới hạn độ dài chuỗi theo tiêu chuẩn OpenAI Marketplace (`displayName` ≤ 30, `shortDescription` ≤ 30, `defaultPrompt` ≤ 128 ký tự).
- Tính hợp lệ của định dạng ảnh và SVG (`assets/icon.svg`, `assets/icon-dark.svg`, `assets/icon.png`, `logo.svg`).
- Tính toàn vẹn của mã render shell script và CSP header trong template HTML.
- Rà soát các file vô tình bị track (`git ls-files -ci --exclude-standard`).

## 3. Quy định về phân loại file trong Git

- **File catalog phân phối**: `.agents/plugins/marketplace.json` và `.claude-plugin/marketplace.json` là tài nguyên catalog phân phối công khai, **bắt buộc phải được track**.
- **File tooling cục bộ**: Thư mục cài đặt cục bộ như `.agents/skills/`, cache, file tạm `*.tmp`, hay artifact kiểm thử cục bộ `*.mindmap.html` **phải được ignore**.
- Tuyệt đối không commit file chứa credentials, secrets, token cá nhân hoặc file `.env`.

## 4. Quy trình Pull Request

1. Fork repository và tạo nhánh tính năng (`feature/...` hoặc `fix/...`).
2. Thực hiện thay đổi tập trung, tối giản và đúng mục đích (surgical changes).
3. Đảm bảo toàn bộ kiểm tra trong `tests/validate.sh` đều vượt qua (`PASS`).
4. Viết commit message rõ ràng bắt đầu bằng động từ chuẩn (Add, Fix, Update, Refactor, Docs).
5. Mở Pull Request trên GitHub và mô tả rõ lý do, bằng chứng kiểm thử và phạm vi ảnh hưởng.
