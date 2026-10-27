# 🧠 AIT3012 - Tiền xử lý Tín Hiệu 

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

Dự án HIỆN TẠI bao gồm **4 notebook** Jupyter, mỗi notebook minh họa một loại bộ lọc số phổ biến trong xử lý tín hiệu EEG:

| Notebook | Bộ Lọc |
|----------|--------|
| `Low-pass.ipynb` | Lọc thông thấp (Low-pass) |
| `High-pass.ipynb` | Lọc thông cao (High-pass) |
| `Band-pass.ipynb` | Lọc thông dải (Band-pass) |
| `Notch-filter.ipynb` | Lọc chắn dải (Notch filter) |

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

### Cách 1: Dùng Jupyter Notebook

```bash
jupyter notebook
```

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

Chi tiết các bộ lọc số được thiết kế và thực nghiệm trong từng notebook, đối chiếu trực tiếp với các tiêu chuẩn xử lý tín hiệu EEG/ERP:

### 1. `Low-pass.ipynb` — Bộ Lọc Thông Thấp (Low-pass / Anti-aliasing Filter)

* **Nguyên lý & Cơ chế**: Cho phép các thành phần tần số **thấp hơn tần số cắt** đi qua và suy giảm mạnh các tần số cao hơn. Chống hiện tượng chồng phổ (*aliasing*) trước khi số hóa và loại bỏ các nhiễu tần số cao, đặc biệt là nhiễu co cơ (EMG) vốn tập trung mạnh từ 30 Hz trở lên.
* **Tần số cắt điển hình**:
  * `30 Hz`, `5 – 40 Hz`, `50 – 100 Hz` (cho phân tích tín hiệu EEG).
  * `70 – 250 Hz` (cho điện não bề mặt vỏ não - ECoG).
  * `5 – 10 kHz` (cho gai điện thế hoạt động của nơ-ron / Spike sorting).
* **Ghi chú thực hành & Lưu ý chuyên môn**:
  * **Mức 30 – 40 Hz**: Mức cắt phổ biến nhất cho nghiên cứu ERP và phân tích nhịp não cơ bản. Giúp loại bỏ triệt để nhiễu cơ (EMG từ 30 Hz trở lên). *Lưu ý*: Lọc ở mức này có thể làm giảm nhẹ biên độ các đỉnh nhọn sớm (như P1, N1).
  * **Mức 50 – 100 Hz**: Khuyến nghị khi cần phân tích dải tần cao Gamma hoặc khi tín hiệu thu được có độ sạch cao.
  * **Quy chuẩn kỹ thuật**: Bắt buộc phải sử dụng bộ lọc Anti-aliasing phần cứng trước khi số hóa tín hiệu (tuân thủ định lý lấy mẫu Nyquist). Trong xử lý phần mềm, nên dùng bộ lọc pha bằng không (*zero-phase filter*) để tránh làm sai lệch mốc thời gian của tín hiệu.
* **Thực nghiệm trong Notebook**:
  * Áp dụng bộ lọc FIR hai chiều không trễ pha với 2 tần số cắt: **30 Hz** (chuẩn ERP khử nhiễu cơ) và **100 Hz** (giữ dải Gamma).
  * Khảo sát dạng sóng trên kênh trán `Fp1` ở miền thời gian và phổ mật độ công suất (PSD).
  * Đánh giá tỷ lệ phần trăm năng lượng và biên độ bị suy giảm trên toàn bộ 127 kênh.

---

### 2. `High-pass.ipynb` — Bộ Lọc Thông Cao (High-pass Filter)

* **Nguyên lý & Cơ chế**: Cho phép các thành phần tần số **cao hơn tần số cắt** đi qua và loại bỏ các thành phần tần số rất thấp. Mục đích chính là loại bỏ thành phần một chiều (DC offset), hiện tượng trôi tín hiệu tần số thấp do bộ khuếch đại điện cực (*baseline drift*), nhiễu chuyển động cơ học và nhiễu chớp mắt/EOG (xấp xỉ ~1 Hz).
* **Tần số cắt điển hình**:
  * `0.1 Hz`, `0.1 – 0.5 Hz` (cho phân tích ERP / P300).
  * `0.5 Hz` (cho phân tích EEG chung, resting-state).
  * Dưới `10 Hz` (cho điện thế trường cục bộ - LFP).
* **Ghi chú thực hành & Lưu ý chuyên môn**:
  * **Dùng 0.1 Hz**: Tiêu chuẩn hiện đại cho dữ liệu điện thế liên quan sự kiện (ERP như P300, N400...). Giúp bảo toàn tối đa biên độ và hình thái sóng, hạn chế tối đa hiện tượng dao động giả (*filter ringing / distortion*) do bộ lọc gây ra.
  * **Dùng 0.5 Hz**: Phù hợp cho phân tích phổ EEG liên tục (resting-state) hoặc các hệ thống có bộ lọc phần cứng cài đặt sẵn. Tần số này triệt tiêu hiệu quả sự trôi đường nền và nhiễu mắt, nhưng có thể làm giảm nhẹ biên độ các thành phần tần số rất thấp của não bộ.
* **Thực nghiệm trong Notebook**:
  * So sánh đối đầu giữa bộ lọc **0.1 Hz** (chuẩn ERP hiện đại) và **0.5 Hz** (chuẩn EEG liên tục) so với dữ liệu gốc `raw_orig`.
  * Trực quan hóa 30 giây đầu tiên trên kênh trán `Fp1` để quan sát sự ổn định của đường nền (baseline stability).
  * Đo lường năng lượng và biên độ tiêu hao trên toàn bộ 127 kênh đo.

---

### 3. `Band-pass.ipynb` — Bộ Lọc Thông Dải (Band-pass Filter)

* **Nguyên lý & Cơ chế**: Chỉ cho phép dải tần số trong khoảng `[f_low, f_high]` đi qua. Bộ lọc giúp cô lập vùng tần số chứa hoạt động não liên quan trực tiếp đến tác vụ, đồng thời loại bỏ đồng thời cả nhiễu ở tần số rất thấp (trôi nền, EOG) lẫn tần số rất cao (nhiễu cơ, nhiễu tần số cao).
* **Dải tần điển hình**:
  * `0.5 – 40 Hz`, `1 – 50 Hz` (tiền xử lý EEG tổng quát).
  * `8 – 12 Hz` (cô lập nhịp Mu vận động).
  * `8 – 30 Hz` (bao gồm cả nhịp Mu và nhịp Beta cảm giác - vận động).
* **Ghi chú thực hành & Lưu ý chuyên môn**:
  * **Dải rộng (1 – 50 Hz)**: Tiêu chuẩn vàng cho tiền xử lý EEG tổng quát. Dải này bảo toàn hầu hết các nhịp não sinh lý (từ Delta đến Gamma thấp) trong khi loại bỏ trôi nền (< 1 Hz) và nhiễu điện lưới (50 Hz).
  * **Dải hẹp (8 – 12 Hz; 8 – 30 Hz)**: Dùng để cô lập các nhịp vận động (Mu, Beta). Rất hiệu quả cho các bài toán Giao diện Não - Máy tính (BCI - phân loại cử động / motor imagery) và phân tích biến thiên công suất phổ (ERD/ERS).
  * **Lưu ý quan trọng**: Việc sử dụng bộ lọc thông dải hẹp (đặc biệt khi có bậc lọc cao) sẽ gây ra hiện tượng dao động giả ở các cạnh tín hiệu (*ringing artifacts*). Do đó, **không khuyến nghị** dùng bộ lọc hẹp để đánh giá hình thái các thành phần sóng ERP.
* **Thực nghiệm trong Notebook**:
  * Thực hành áp dụng **Dải rộng (1 – 50 Hz)** và **Dải hẹp (8 – 30 Hz)** trên dữ liệu Oddball task.
  * So sánh dạng sóng trên miền thời gian (chuyển đổi sang đơn vị µV) và đánh giá lượng thông tin bị loại bỏ qua tỷ lệ % năng lượng và biên độ hiệu dụng (RMS).

---

### 4. `Notch-filter.ipynb` — Bộ Lọc Chắn Dải / Lọc Khía (Band-stop / Notch Filter)

* **Nguyên lý & Cơ chế**: Loại bỏ hoặc suy giảm cực mạnh một tần số mục tiêu cụ thể (hoặc dải hẹp xung quanh nó), giữ nguyên các tần số còn lại. Mục đích là triệt tiêu nhiễu cảm ứng từ đường dây điện nguồn xoay chiều (50/60 Hz *mains hum / line noise*) hoặc giảm nhiễu chuyển động mắt chậm (Slow EOG ở tần số 3 – 4 Hz).
* **Dải tần chắn điển hình**:
  * Chắn dải `48 – 52 Hz` (tại Châu Âu, Châu Á và Việt Nam dùng điện lưới 50 Hz).
  * Chắn dải `59 – 61 Hz` (tại Bắc Mỹ dùng điện lưới 60 Hz).
  * Chắn dải `1 – 4 Hz` (thử nghiệm giảm nhiễu Slow EOG).
* **Ghi chú thực hành & Lưu ý chuyên môn**:
  * **Dùng 48 – 52 Hz / 59 – 61 Hz**: Cần chọn dải chặn rộng khoảng **2 – 4 Hz** để bù đắp sự dao động trôi tần số thực tế của lưới điện. **Tuyệt đối xác định đúng vị trí địa lý nơi ghi dữ liệu** (Bắc Mỹ: 60 Hz; Châu Âu và Châu Á: 50 Hz).
  * **Dùng 1 – 4 Hz**: Mục đích triệt tiêu nhiễu chuyển động mắt chậm (Slow EOG). Tuy nhiên, phương pháp này **rất hạn chế** vì sẽ làm mất đi sóng Delta sinh lý quan trọng. Phương pháp tối ưu hiện đại là sử dụng phân tích thành phần độc lập (**ICA**) để loại bỏ EOG mà vẫn bảo toàn nguyên vẹn tín hiệu não.
  * **Cảnh báo dao động giả & dải Gamma**: Bộ lọc Notch có độ dốc cao rất dễ gây ra hiện tượng dao động giả và có thể vô tình cắt mất tín hiệu não thật (như dải Gamma) nằm trùng tần số với nhiễu.
  * **Bản chất khác biệt**: Sự khác nhau giữa 50 Hz (Á/Âu) và 60 Hz (Mỹ) xuất phát từ **bản chất của hạ tầng hệ thống điện lưới**, không liên quan đến bản chất sinh lý học của não bộ hay tín hiệu sinh học như các bộ lọc khác.
* **Thực nghiệm trong Notebook**:
  * Dữ liệu Nencki-Symfonia ghi nhận tại Ba Lan (Châu Âu) nên sử dụng lọc Notch **48 – 52 Hz**, đồng thời so sánh đối chiếu với dải chặn **1 – 4 Hz**.
  * Vẽ đồ thị phổ PSD trước và sau lọc để kiểm chứng đỉnh nhiễu 50 Hz bị triệt tiêu hoàn toàn.

---

### 📋 Bảng Tổng Hợp So Sánh Các Bộ Lọc

| Lọc tần số | Tên bộ lọc | Tần số cắt điển hình | Mục đích & Cơ chế | Ghi chú thực hành & Lưu ý chuyên môn |
|---|---|---|---|---|
| **High-pass** | Bộ lọc thông cao | `0.1 Hz`, `0.1 - 0.5 Hz` (P300), `0.5 Hz` (EEG chung), `< 10 Hz` (LFP) | Loại bỏ thành phần một chiều (DC), hiện tượng trôi tín hiệu tần số thấp do bộ khuếch đại, nhiễu chuyển động và nhiễu chớp mắt/EOG (~1 Hz). | • **Dùng 0.1 Hz**: Tiêu chuẩn hiện đại cho ERP (P300, N400...), bảo toàn tối đa biên độ và hình thái sóng, tránh dao động giả.<br>• **Dùng 0.5 Hz**: Phù hợp cho phổ EEG liên tục, triệt tiêu trôi nền mạnh hơn nhưng có thể giảm nhẹ biên độ tần số rất thấp. |
| **Low-pass** | Bộ lọc thông thấp / Anti-aliasing | `30 Hz`, `5 - 40 Hz`, `50 - 100 Hz` (EEG), `70 - 250 Hz` (ECoG), `5 - 10 kHz` (Spikes) | Chống hiện tượng chồng phổ trước khi số hóa và loại bỏ nhiễu tần số cao (nhiễu cơ EMG tập trung từ 30 Hz trở lên). | • **Dùng 30 - 40 Hz**: Mức phổ biến nhất cho ERP, loại bỏ triệt để nhiễu cơ (EMG ≥ 30 Hz), có thể làm giảm nhẹ biên độ đỉnh nhọn (P1, N1).<br>• **Dùng 50 - 100 Hz**: Khuyến nghị khi cần phân tích dải Gamma.<br>• Bắt buộc dùng Anti-aliasing phần cứng trước số hóa; dùng bộ lọc pha bằng 0 trong phần mềm. |
| **Band-pass** | Bộ lọc thông dải | `0.5 - 40 Hz`, `1 - 50 Hz` (EEG tổng quát), `8 - 12 Hz` (nhịp Mu), `8 - 30 Hz` (Mu & Beta) | Cô lập vùng tần số chứa hoạt động não liên quan đến tác vụ và loại bỏ đồng thời nhiễu ở tần số rất thấp lẫn rất cao. | • **Dải rộng (1 - 50 Hz)**: Tiêu chuẩn tiền xử lý EEG tổng quát, bảo toàn hầu hết nhịp sinh lý và loại trôi nền + nhiễu 50 Hz.<br>• **Dải hẹp (8 - 12 Hz / 8 - 30 Hz)**: Hiệu quả cho BCI phân loại chuyển động và phân tích công suất.<br>• Tránh dùng bộ lọc dải hẹp bậc cao để đánh giá hình thái thành phần ERP do gây dao động giả. |
| **Band-stop / Notch** | Bộ lọc chắn dải / Lọc khía | `48 - 52 Hz` (Châu Á, Châu Âu: 50 Hz), `59 - 61 Hz` (Mỹ: 60 Hz), hoặc `1 - 4 Hz` | Triệt tiêu nhiễu nguồn xoay chiều 50/60 Hz line noise hoặc giảm nhiễu chuyển động mắt EOG ở 3 - 4 Hz. | • **Dùng 48 - 52 Hz / 59 - 61 Hz**: Cần dải chặn rộng 2 - 4 Hz bù trôi tần số; xác định đúng vị trí địa lý ghi dữ liệu.<br>• **Dùng 1 - 4 Hz**: Hạn chế vì làm mất sóng Delta sinh lý (nên dùng ICA thay thế).<br>• Bộ lọc dốc dễ gây dao động giả và cắt mất dải Gamma trùng tần số.<br>• Phụ thuộc bản chất hệ thống điện thay vì bản chất não bộ. |

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
