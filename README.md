<p align="center">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="assets/icon-dark.svg">
    <img src="assets/icon.svg" width="96" height="96" alt="mindmap-skills icon">
  </picture>
</p>

<h1 align="center">mindmap-skills</h1>

<p align="center">
  <b>Sơ đồ tư duy Markmap cho AI Agents (Claude Code, OpenAI Codex, Google Antigravity).</b><br>
  Chuẩn nhận thức Miller's Law & MECE · 0 daemon · 0 token tax · Render HTML độc lập.
</p>

<p align="center">
  <a href="https://github.com/fioenix/mindmap-skills/actions/workflows/ci.yml"><img src="https://github.com/fioenix/mindmap-skills/actions/workflows/ci.yml/badge.svg" alt="CI Status" /></a>
  <a href="https://github.com/fioenix/mindmap-skills"><img src="https://img.shields.io/badge/Marketplace-Ready-7FE2CE?logo=anthropic&logoColor=0B0B17" alt="Marketplace Ready" /></a>
  <a href="https://github.com/fioenix/mindmap-skills"><img src="https://img.shields.io/badge/Runtime-Zero--Daemon-9750C4" alt="Zero Daemon" /></a>
  <a href="https://github.com/fioenix/mindmap-skills"><img src="https://img.shields.io/badge/Agents-Claude%20%7C%20Codex%20%7C%20Antigravity-18181b" alt="Agent Support" /></a>
  <a href="LICENSE"><img src="https://img.shields.io/badge/License-MIT-blue.svg" alt="License: MIT" /></a>
  <a href="CONTRIBUTING.md"><img src="https://img.shields.io/badge/PRs-welcome-brightgreen.svg" alt="PRs Welcome" /></a>
</p>

---

## ⚡ Bản chất giải pháp

Phần lớn giải pháp mindmap cho AI hiện nay mắc phải hai điểm nghẽn lớn:
1. **Server MCP cồng kềnh & Token Tax**: Chạy tiến trình nền ngầm, kéo theo trình duyệt Playwright/Chromium 300MB chỉ để chụp màn hình, đồng thời đốt hơn 1.000 tokens định nghĩa schema trong mỗi lượt hội thoại dù không dùng tới.
2. **Tràn ngập nhận thức (Cognitive Sprawl)**: Đổ nguyên đoạn văn xuôi dài dòng vào các nút con, tạo thành những "bức tường chữ" phá vỡ hoàn toàn công năng trực quan của sơ đồ tư duy.

### Bảng đối chiếu giải pháp

| Tiêu chí | Server MCP cồng kềnh / Headless | LLM xuất văn bản thô | **mindmap-skills** |
|---|---|---|---|
| **Tiến trình nền (Daemon)** | Chrome 300MB chạy ngầm liên tục | 0 MB | **0 MB (Không daemon ngầm)** |
| **Token Tax mỗi lượt chat** | Tốn 1.000+ tokens định nghĩa tool | 0 token | **0 token overhead khi ở trạng thái nghỉ** |
| **Cấu trúc nhận thức** | Không lọc (dump toàn bộ chữ) | Hỗn độn, thiếu trật tự | **Miller's Law (4–7 nhánh, depth 3–4, ≤ 8 từ/nút)** |
| **Artifact đầu ra** | Ảnh chụp tĩnh (PNG không tương tác) | Đoạn text thuần | **File `.mindmap.md` + file `.html` tương tác độc lập** |
| **Hỗ trợ đa nền tảng** | Cục bộ theo từng client | Tự do, không chuẩn hóa | **Claude Code · OpenAI Codex · Google Antigravity** |
| **Mức độ an toàn (Security)** | Nguy cơ thực thi subprocess | An toàn | **Mẫu HTML có CSP nghiêm ngặt, chống parser breakout** |

---

## 🔍 Đối chiếu thực tế: Trước và Sau khi áp dụng

| Tình huống | Trước khi áp dụng (LLM mặc định) | Sau khi cấu trúc qua `mindmap-skills` |
|---|---|---|
| **Kiến trúc Gateway** | `- Hệ thống sử dụng một API Gateway chạy trên nền tảng Cloudflare Workers để xử lý xác thực các yêu cầu của người dùng thông qua mã JWT được ký bằng thuật toán mã hóa RSA...` (32 từ, lan man) | `- **Auth**: JWT với chữ ký RSA`<br>`- **Rate Limit**: Token bucket tại Edge`<br>`- ~~Kong Gateway: Chi phí hạ tầng cao~~` (Ngắn gọn, từ khóa đầu dòng, có lý do loại bỏ) |
| **Cấu trúc nhánh** | Đổ phẳng 14 gạch đầu dòng ngang hàng nhau, gây quá tải bộ nhớ làm việc. | Gom tụ thành 4 nhánh MECE (Edge, Compute, Data, Telemetry); các nhánh sâu tự động thu gọn bằng `<!-- markmap: fold -->`. |
| **Theo dõi quyết định** | Chỉ nêu dữ kiện tĩnh, không biết tính năng nào đã chốt, tính năng nào còn bỏ ngỏ. | `- [x] Đồng bộ state snapshot`<br>`- [ ] Cơ chế retry backoff cho WebSocket`<br>`+ Tốc độ cao / - Rủi ro stale read` |

---

## 📦 Cài nhanh

### 1. Claude Code

#### Cài từ Marketplace công khai của repo (Khuyến nghị):
Trong phiên dòng lệnh của Claude Code:
```text
/plugin marketplace add fioenix/mindmap-skills
/plugin install mindmap-skills@fioenix-plugins
```
Gọi skill trực tiếp trong cuộc hội thoại:
```text
/mindmap-skills:markmap Tạo sơ đồ tư duy cho kiến trúc microservices này
```

#### Trên Claude Desktop hoặc Claude Web UI:
1. Mở **Customize** → **Plugins** → **Add** → **Add marketplace** → **Add from a repository**.
2. Nhập repository: `fioenix/mindmap-skills`.
3. Trong mục **Discover**, tìm **mindmap-skills** và nhấn **Add**.
4. Sử dụng bằng cách gõ `/markmap` hoặc chọn biểu tượng `+` trong ô chat.

#### Cài đặt cục bộ khi phát triển (Local Link):
```bash
claude plugin add ~/Projects/mindmap-skills
```

---

### 2. OpenAI Codex & Agents SDK

#### Cài nhanh qua Skills CLI:
```bash
npx --yes skills@1.5.20 add fioenix/mindmap-skills --global
```

#### Quản lý qua Catalog Workspace hoặc Thư mục Agent:
```bash
# Trong một dự án cụ thể
mkdir -p .agents/skills
cp -r ~/Projects/mindmap-skills/skills/markmap .agents/skills/

# Hoặc cài global cho máy
mkdir -p ~/.codex/skills
ln -s ~/Projects/mindmap-skills/skills/markmap ~/.codex/skills/markmap
```

---

### 3. Google Antigravity

#### Cài đặt toàn cục (Machine-Global):
```bash
mkdir -p ~/.gemini/config/skills
ln -s ~/Projects/mindmap-skills/skills/markmap ~/.gemini/config/skills/markmap
```

#### Cài đặt theo từng Workspace dự án:
```bash
mkdir -p .agents/skills
cp -r ~/Projects/mindmap-skills/skills/markmap .agents/skills/
```

---

## 📋 Bộ quy tắc cấu trúc nhận thức (Cognitive Invariants)

Mọi mindmap do skill tạo ra đều tuân thủ chặt chẽ các nguyên tắc cấu trúc thông tin:

* **Miller's Law (4–7 nhánh chính `##`)**: Giới hạn số lượng nhánh cấp 1 theo dung lượng bộ nhớ làm việc của não bộ. Luôn gom nhóm các thành phần liên quan vào các cụm chủ đề thay vì liệt kê dàn trải.
* **Phân loại MECE (Không trùng lặp, Không bỏ sót)**: Các nhánh con ở cùng một tầng phải phân chia theo một trục logic duy nhất (ví dụ: tầng kiến trúc, vòng đời dữ liệu, hoặc nhóm tác nhân), không để lẫn lộn thuộc tính phi chức năng với thành phần hệ thống.
* **Cân bằng mật độ nhánh (Branch Equilibrium)**: Khi một nhánh có trên 7 nút con, bắt buộc gom nhóm trung gian (`###`) để giữ bố cục sơ đồ cân đối, tránh lệch trọng tâm thị giác.
* **Khai mở tăng tiến (`<!-- markmap: fold -->`)**: Tầng 1 và 2 luôn mở sẵn để người đọc nắm bắt toàn cảnh trong 5 giây. Các nhánh sâu từ tầng 3 trở đi hoặc danh sách thông số kỹ thuật chi tiết phải tự động gấp lại (`<!-- markmap: fold -->`), cho phép người dùng click mở khi cần đào sâu.
* **Mã hóa quyết định kiến trúc**:
  - `- [x]` Đã thống nhất / Hoàn thành
  - `- [ ]` Câu hỏi mở / Đang chờ chốt
  - `~~Phương án loại trừ~~`: Ghi nhận lý do phương án bị từ chối
  - `==Điểm nghẽn / Trọng tâm rủi ro==`: Đánh dấu thành phần nhạy cảm
  - `+ Lợi thế / - Chi phí đánh đổi`: Chỉ rõ ai là bên trả giá cho quyết định kiến trúc

```markdown
---
title: Kiến trúc Finolabs Gateway
markmap:
  colorFreezeLevel: 2
---

## Ingress Gateway (MECE: Cổng biên)
- **Runtime**: Cloudflare Workers
- **Security**: JWT với chữ ký RSA
- ~~Kong Gateway: Chi phí hạ tầng cao~~

## Storage Tier (MECE: Lưu trữ)
- **Metadata**: Cloudflare D1
  - `+ Truy vấn SQLite độ trễ cực thấp`
  - `- Giới hạn ghi đơn luồng`
- **Blobs**: Cloudflare R2
- ~~AWS S3: Phí egress dữ liệu cao~~

## Telemetry (MECE: Quan sát) <!-- markmap: fold -->
- **Traces**: OpenTelemetry collector
- **Metrics**: Cloudflare Analytics Engine
- **Nhiệm vụ còn mở**:
  - - [ ] Đánh giá tần suất sampling 5%
  - - [x] Bật tail-based sampling
```

---

## 🔄 Hướng dẫn phối hợp kỹ năng (Multi-Skill Synergy)

`mindmap-skills` được thiết kế theo nguyên tắc **Zero-Coercion & Zero-Hard-Dependency**: hoạt động độc lập 100% không đòi hỏi bất kỳ công cụ ngoài nào. Tuy nhiên, khi agent harness có sẵn các skills bổ trợ, nó sẽ đóng vai trò là **Bộ gom tụ trực quan (Visual Converger)**:

| Skill có trong Harness | Vai trò của Skill đó | Cách `markmap` tiếp nhận & phối hợp |
|---|---|---|
| **`grilling`** | Phản biện giả định ngầm, bóc tách rủi ro, chốt các đánh đổi kiến trúc. | **Bản đồ quyết định (Decision Tree)**: Đóng gói lại các phương án đã chọn, phương án bị loại (`~~...~~`), invariants bảo vệ và các đầu việc cần làm (`- [ ]`). |
| **`brainstorming`** | Phóng tác ý tưởng tự do, mở rộng các phương án tiềm năng. | **Bộ gom cụm nhận thức (Affinity Map)**: Gom hàng chục ý tưởng tản mạn thành 4–7 cụm MECE, phân cấp thứ tự ưu tiên và gấp các nhánh chi tiết. |
| **Spec Kit (`.specify/`)** | Xây dựng đặc tả yêu cầu chức năng hệ thống (`spec.md`). | **Phân rã chức năng (Functional Decomposition)**: Trực quan hóa User Stories, quan hệ thực thể dữ liệu và Acceptance Criteria. |

### Các kịch bản sử dụng thực tế:

#### Kịch bản 1: Phối hợp cùng `grilling`
> **User Prompt:** *"Hãy dùng grilling để phản biện và chốt kiến trúc này, sau đó dùng markmap để vẽ lại toàn bộ quyết định thành sơ đồ tư duy."*
> 
> **Hành động của Agent:**
> 1. Chạy quy trình `grilling` để phỏng vấn, bóc tách rủi ro và xác nhận các ràng buộc kỹ thuật.
> 2. Chốt các quyết định cốt lõi.
> 3. Tự động chuyển giao sang `markmap` để tạo ra file `.mindmap.md` tổng kết kiến trúc: đánh dấu các phương án được duyệt, gạch bỏ các phương án loại trừ (`~~...~~`) và gắn các task pending (`- [ ]`).

#### Kịch bản 2: Phối hợp cùng `brainstorming`
> **User Prompt:** *"Brainstorm 10 hướng phát triển tính năng cho app, sau đó dùng markmap gom nhóm trực quan."*
> 
> **Hành động của Agent:**
> 1. Chạy quy trình `brainstorming` để sinh ra các ý tưởng đột phá.
> 2. Sử dụng `markmap` để phân loại 10 ý tưởng đó vào 4 nhánh MECE (ví dụ: Growth, Retention, Monetization, Infra).
> 3. Thêm cờ `<!-- markmap: fold -->` cho các ý tưởng nhánh phụ và xuất ra file HTML artifact để người dùng xem ngay.

#### Kịch bản 3: Chạy độc lập (Standalone)
> Khi môi trường của người dùng không cài đặt `grilling` hay `brainstorming`, skill thực thi trực tiếp từ văn bản hoặc tài liệu của người dùng, **tuyệt đối không yêu cầu người dùng cài đặt thêm công cụ nào khác**.

---

## 🛠️ Cấu trúc Repository

```text
mindmap-skills/
├── .github/
│   ├── workflows/
│   │   └── ci.yml              # Quy trình kiểm thử tự động trên GitHub Actions
│   ├── ISSUE_TEMPLATE/         # Biểu mẫu báo lỗi và đề xuất tính năng
│   └── PULL_REQUEST_TEMPLATE.md# Checklist kiểm tra trước khi merge PR
├── .claude-plugin/
│   ├── marketplace.json        # Định nghĩa catalog marketplace cho Claude Code
│   └── plugin.json             # Manifest plugin Claude Code (URLs, icons, tags)
├── .codex-plugin/
│   └── plugin.json             # Manifest plugin OpenAI Codex (interface, translations)
├── .codex/
│   └── plugin.json             # Manifest tương thích Codex phiên bản cũ
├── .agents/
│   └── plugins/
│       └── marketplace.json    # Catalog phân phối cho hệ sinh thái AI Agents
├── agents/
│   └── openai.yaml             # Đặc tả giao diện agent
├── plugin.json                 # Manifest chuẩn Antigravity / Universal
├── package.json                # Package descriptor cho npm / skills.sh
├── assets/
│   ├── icon.svg                # Icon vector squircle giao diện sáng (FINOLABS tokens)
│   ├── icon-dark.svg           # Icon vector giao diện tối (Dark mode)
│   └── icon.png                # Icon bitmap vuông 512x512
├── logo.svg                    # Vector logo gốc
├── LICENSE                     # Giấy phép mã nguồn mở MIT
├── README.md                   # Tài liệu hướng dẫn sử dụng chính
├── CONTRIBUTING.md             # Hướng dẫn đóng góp & kiểm thử offline
├── PRIVACY.md                  # Chính sách bảo mật & dữ liệu
├── TERMS.md                    # Điều kiện sử dụng
├── skills/
│   └── markmap/
│       ├── SKILL.md            # Chỉ dẫn hành vi và ràng buộc kỹ thuật của skill
│       └── assets/
│           └── template.html   # Template HTML độc lập (được bảo vệ bằng CSP)
├── scripts/
│   ├── build_icon.py           # Script build icon vector tự động
│   └── render.sh               # Script wrapper dòng lệnh (markmap-cli)
└── tests/
    └── validate.sh             # Bộ kiểm chứng tự động 8 gates trước khi phát hành
```

---

## 🔒 An toàn & Bảo mật thông tin

* **Không vận hành backend & Không telemetry**: Toàn bộ quá trình tạo mindmap diễn ra nội bộ trong phiên làm việc của agent. Không có bất kỳ dữ liệu nào bị gửi tới máy chủ của maintainer.
* **Bảo vệ chống XSS & Parser Breakout**: Template HTML nhúng sẵn tiêu đề Content Security Policy (CSP) chặt chẽ và tự động thoát chuỗi `</script` thành `<\/script` trong nội dung Markdown để ngăn chặn tiêm mã độc.
* **Ngăn chặn CLI Option Injection**: Kịch bản `scripts/render.sh` kết thúc cờ dòng lệnh bằng `--` trước khi truyền tham số tệp để ngăn chặn tệp độc hại kích hoạt cờ trái phép.
* **Chính sách dữ liệu**: Xem chi tiết tại [PRIVACY.md](PRIVACY.md) và [TERMS.md](TERMS.md).

---

## 📄 Bản quyền & Đóng góp

* **Giấy phép**: [MIT License](LICENSE) © [Fioenix](https://github.com/fioenix)
* **Đóng góp**: Đọc kỹ [CONTRIBUTING.md](CONTRIBUTING.md) trước khi tạo pull request.
* **Báo lỗi & Thảo luận**: [GitHub Issues](https://github.com/fioenix/mindmap-skills/issues)
