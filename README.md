# 🧠 AIT3012 - Xử Lý Tín Hiệu EEG Bằng Các Bộ Lọc Số (Digital Filters)

> **Đồ án nhóm 9** - Môn AIT3012: Xử lý tín hiệu sinh học  
> Thực hành thiết kế và so sánh các bộ lọc số cho tín hiệu điện não (EEG) trên dữ liệu thực nghiệm.

---

## 📋 Mục Lục

- [Giới Thiệu](#-giới-thiệu)
- [Cấu Trúc Thư Mục](#-cấu-trúc-thư-mục)
- [Yêu Cầu Hệ Thống](#-yêu-cầu-hệ-thống)
- [Hướng Dẫn Cài Đặt](#-hướng-dẫn-cài-đặt)
- [Hướng Dẫn Tải Dữ Liệu](#-hướng-dẫn-tải-dữ-liệu)
- [Hướng Dẫn Chạy](#-hướng-dẫn-chạy)
- [Mô Tả Từng Notebook](#-mô-tả-từng-notebook)
- [Dữ Liệu Sử Dụng](#-dữ-liệu-sử-dụng)
- [Thành Viên Nhóm](#-thành-viên-nhóm)

---

## 🎯 Giới Thiệu

Dự án bao gồm **4 notebook** Jupyter, mỗi notebook minh họa một loại bộ lọc số phổ biến trong xử lý tín hiệu EEG:

| Notebook | Bộ Lọc | Mục Đích |
|----------|--------|----------|
| `Low-pass.ipynb` | Lọc thông thấp (Low-pass) | Loại bỏ nhiễu tần số cao, giữ lại thành phần tần số thấp |
| `High-pass.ipynb` | Lọc thông cao (High-pass) | Loại bỏ trôi đường nền (DC drift), giữ tín hiệu tần số cao |
| `Band-pass.ipynb` | Lọc thông dải (Band-pass) | Chỉ giữ lại dải tần số quan tâm (ví dụ: Alpha 8-13 Hz) |
| `Notch-filter.ipynb` | Lọc chắn dải (Notch filter) | Loại bỏ nhiễu điện lưới 50/60 Hz |

Tất cả notebook đều sử dụng **dữ liệu EEG thực nghiệm** từ bộ dữ liệu [Nencki-Symfonia EEG/ERP (ds004621)](https://openneuro.org/datasets/ds004621) trên OpenNeuro.

---

## 📁 Cấu Trúc Thư Mục

```
AIT3012-Team9/
├── README.md                    # File hướng dẫn này
├── requirements.txt             # Danh sách thư viện Python cần cài
├── download_real_sample.py      # Script tải dữ liệu EEG mẫu
│
├── Band-pass.ipynb              # Notebook lọc thông dải
├── High-pass.ipynb              # Notebook lọc thông cao
├── Low-pass.ipynb               # Notebook lọc thông thấp
├── Notch-filter.ipynb           # Notebook lọc chắn dải
│
└── data/                            # Thư mục dữ liệu
    └── sub-01/
        └── eeg/
            ├── sub-01_task-oddball_eeg.eeg    # Dữ liệu EEG binary (tải bằng script)
            ├── sub-01_task-oddball_eeg.vhdr   # Header file (có sẵn)
            ├── sub-01_task-oddball_eeg.vmrk   # Marker file (có sẵn)
            ├── sub-01_task-oddball_channels.tsv # Thông tin kênh (có sẵn)
            └── sub-01_task-oddball_events.tsv  # Sự kiện (có sẵn)
```

---

## 💻 Yêu Cầu Hệ Thống

- **Python**: >= 3.9
- **Hệ điều hành**: Windows / macOS / Linux
- **RAM**: >= 4 GB (khuyến nghị 8 GB)
- **Kết nối Internet**: Cần để tải dữ liệu EEG mẫu (~39 MB)

---

## 🔧 Hướng Dẫn Cài Đặt

### Bước 1: Clone Repository

```bash
git clone https://github.com/Muaxuannamay/AIT3012-Team9.git
cd AIT3012-Team9
```

### Bước 2: Tạo Môi Trường Ảo (Khuyến Nghị)

**Dùng `venv`:**
```bash
python -m venv venv

# Windows (PowerShell)
.\venv\Scripts\Activate.ps1

# Windows (CMD)
.\venv\Scripts\activate.bat

# macOS / Linux
source venv/bin/activate
```

**Hoặc dùng `conda`:**
```bash
conda create -n eeg-filters python=3.12 -y
conda activate eeg-filters
```

### Bước 3: Cài Đặt Thư Viện

```bash
pip install -r requirements.txt
```

---

## 📥 Hướng Dẫn Tải Dữ Liệu

Dữ liệu EEG quá lớn để lưu trực tiếp trên GitHub. Chạy script sau để tải **80 giây dữ liệu EEG thực nghiệm** (127 kênh, ~39 MB) từ OpenNeuro:

```bash
python download_real_sample.py
```

Script sẽ:
1. Tải dữ liệu EEG nhị phân từ OpenNeuro S3 (song song, nhanh hơn)
2. Lưu vào `data/sub-01/eeg/sub-01_task-oddball_eeg.eeg`
3. Cập nhật file header `.vhdr` cho đúng số điểm dữ liệu

> ⏱️ Thời gian tải: khoảng **1-3 phút** tùy tốc độ mạng.

---

## 🚀 Hướng Dẫn Chạy

### Cách 1: Dùng Jupyter Notebook (Giao Diện Web)

```bash
jupyter notebook
```
Trình duyệt sẽ mở tự động. Chọn notebook cần chạy (ví dụ: `Band-pass.ipynb`) và nhấn **Run All** (hoặc `Ctrl + Shift + Enter`).

### Cách 2: Dùng JupyterLab

```bash
jupyter lab
```

### Cách 3: Dùng VS Code

1. Mở thư mục dự án trong VS Code
2. Cài extension **Jupyter** (nếu chưa có)
3. Mở file `.ipynb` và chạy từng cell

### Thứ Tự Chạy Khuyến Nghị

Các notebook **độc lập** với nhau, bạn có thể chạy theo bất kỳ thứ tự nào. Tuy nhiên, thứ tự sau sẽ giúp hiểu dần từ đơn giản đến phức tạp:

1. 🟢 `Low-pass.ipynb` — Bắt đầu với bộ lọc đơn giản nhất
2. 🔵 `High-pass.ipynb` — Khám phá loại bỏ trôi đường nền
3. 🟡 `Band-pass.ipynb` — Kết hợp cả hai loại lọc trên
4. 🔴 `Notch-filter.ipynb` — Xử lý nhiễu điện lưới

---

## 📓 Mô Tả Từng Notebook

### 1. `Low-pass.ipynb` — Bộ Lọc Thông Thấp

- **Nguyên lý**: Cho phép các thành phần tần số **thấp hơn tần số cắt** đi qua, loại bỏ tần số cao.
- **Ứng dụng**: Khử nhiễu cơ (EMG), nhiễu điện từ tần số cao.
- **Thí nghiệm**: So sánh tín hiệu EEG trước và sau khi lọc thông thấp 40 Hz.

### 2. `High-pass.ipynb` — Bộ Lọc Thông Cao

- **Nguyên lý**: Cho phép các thành phần tần số **cao hơn tần số cắt** đi qua, loại bỏ tần số thấp (DC drift).
- **Ứng dụng**: Loại bỏ trôi đường nền, chuẩn bị dữ liệu cho phân tích ERP.
- **Thí nghiệm**: So sánh bộ lọc 0.1 Hz (chuẩn ERP) và 0.5 Hz (chuẩn EEG liên tục), phân tích sóng P300.

### 3. `Band-pass.ipynb` — Bộ Lọc Thông Dải

- **Nguyên lý**: Chỉ giữ lại dải tần số trong khoảng `[f_low, f_high]`, loại bỏ cả tần số thấp và cao ngoài dải.
- **Ứng dụng**: Trích xuất nhịp Alpha (8-13 Hz), Beta (13-30 Hz), hoặc dải tần cụ thể.
- **Thí nghiệm**: Tách và phân tích các băng tần não bộ quan trọng.

### 4. `Notch-filter.ipynb` — Bộ Lọc Chắn Dải (Notch)

- **Nguyên lý**: Loại bỏ **một tần số cụ thể** (và các hài bậc cao), giữ nguyên phần còn lại.
- **Ứng dụng**: Triệt tiêu nhiễu điện lưới 50 Hz (châu Á/châu Âu) hoặc 60 Hz (Bắc Mỹ).
- **Thí nghiệm**: So sánh phổ PSD trước và sau khi áp dụng notch filter 50 Hz.

---

## 📊 Dữ Liệu Sử Dụng

| Thuộc tính | Giá trị |
|-----------|---------|
| **Bộ dữ liệu** | [Nencki-Symfonia EEG/ERP dataset (ds004621)](https://openneuro.org/datasets/ds004621) |
| **Đối tượng** | `sub-01` |
| **Tác vụ** | 3-Stimuli Oddball Task |
| **Số kênh** | 127 kênh EEG |
| **Tần số lấy mẫu** | 1000 Hz |
| **Thời lượng** | 80 giây (đã crop từ bản ghi gốc ~22 phút) |
| **Định dạng** | BrainVision (`.vhdr` + `.eeg` + `.vmrk`) |



## 📄 Giấy Phép

Dự án này sử dụng dữ liệu công khai từ OpenNeuro theo giấy phép CC0 (Public Domain). Mã nguồn được phát hành phục vụ mục đích học tập.

---

> **Lưu ý**: Nếu gặp lỗi khi chạy, hãy đảm bảo đã tải dữ liệu bằng `python download_real_sample.py` và cài đầy đủ thư viện bằng `pip install -r requirements.txt`.
