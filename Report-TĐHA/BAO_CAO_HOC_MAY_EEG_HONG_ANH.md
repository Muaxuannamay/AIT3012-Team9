# BÁO CÁO PHÂN LOẠI TÍN HIỆU EEG ODDBALL BẰNG MÔ HÌNH HỌC MÁY

* **Môn học**: Xử lý tín hiệu não (AIT3012) — **Nhóm**: 9
* **Sinh viên :** Tống Đức Hồng Anh
* **Nhiệm vụ :** Trích xuất đặc trưng Miền tần số / Phi tuyến & Huấn luyện mô hình Logistic Regression vs Random Forest

---

## 1. Bài toán và dữ liệu thực nghiệm

Thí nghiệm Oddball kích thích thị giác gồm hai loại sự kiện: kích thích thường (Standard, chiếm ~80%) và kích thích đích (Target, chiếm ~15%). Khi người tham gia nhận diện Target, điện thế gợi mở P300 xuất hiện ở vùng vỏ não đỉnh-trung tâm sau 300 - 500 ms. Mục tiêu là phân loại nhị phân giữa Standard (nhãn 0) và Target (nhãn 1).

Nghiên cứu sử dụng tập dữ liệu Nencki-Symfonia (ds004621, 42 người, 127 kênh, 1000 Hz). Mỗi epoch kéo dài từ -0.2 s đến 0.8 s (1001 điểm lấy mẫu), hiệu chỉnh baseline [-0.2, 0] s. Dữ liệu được chia độc lập theo đối tượng (Subject-Independent):
- **Tập Train (Người 01 - 28)**: 16.235 epoch dùng để huấn luyện.
- **Tập Validation (Người 29 - 34)**: 3.474 epoch dùng để tinh chỉnh tham số.
- **Tập Test (Người 35 - 42)**: 4.731 epoch của 8 người hoàn toàn mới dùng để đánh giá.

---

## 2. Phương pháp trích xuất đặc trưng

Để tránh quá tải số chiều (127 kênh × 1001 điểm = 127.127 giá trị/epoch), tín hiệu được rút gọn thành 9 đặc trưng trên mỗi kênh:

### 2.1. Đặc trưng miền tần số (Welch PSD)
- Năng lượng 5 dải sóng não: Delta (1 - 4 Hz), Theta (4 - 8 Hz), Alpha (8 - 12 Hz), Beta (12 - 30 Hz), Gamma (30 - 40 Hz). Kích thích Target tập trung năng lượng cao ở dải Delta và Theta.
- Tỉ số công suất chú ý Theta / Beta (TBR):
  $$\text{TBR} = \frac{P_{\theta} + \epsilon}{P_{\beta} + \epsilon}$$

### 2.2. Đặc trưng miền phi tuyến
- Độ hỗn loạn phổ (Spectral Entropy - $H_s$): Phản ánh mức độ đồng bộ hóa nơ-ron (giảm khi gặp Target):
  $$H_s = -\sum_{i} p_i \log_2(p_i + \epsilon) \quad \text{với} \quad p_i = \frac{\text{PSD}_i}{\sum_j \text{PSD}_j}$$
- Tham số hình thái Hjorth:
  $$\text{Mobility}(x) = \sqrt{\frac{\text{Var}(x')}{\text{Var}(x)}} \qquad \text{Complexity}(x) = \frac{\text{Mobility}(x')}{\text{Mobility}(x)}$$

Tổng số chiều đặc trưng mỗi epoch: 127 kênh × 9 = **1.143 chiều**. Dữ liệu được chuẩn hóa bằng `StandardScaler` (chỉ fit trên tập Train để chống rò rỉ dữ liệu).

---

## 3. Huấn luyện và so sánh 2 mô hình học máy

Do dữ liệu mất cân bằng (Standard nhiều gấp ~8 lần Target), cả hai mô hình đều được áp dụng trọng số lớp nghịch đảo: $w_j = \frac{N}{2 \cdot N_j}$.
1. **Logistic Regression (Tuyến tính)**: Điều chuẩn $L_2$, $C = 0.05$, tối ưu L-BFGS.
2. **Random Forest (Phi tuyến / Cây)**: 100 cây quyết định, độ sâu tối đa 10 tầng.

### Bảng kết quả trên tập kiểm thử độc lập (Người 35 - 42: 4.731 mẫu)

| Chỉ số đánh giá | Logistic Regression | Random Forest | Ý nghĩa |
| :--- | :---: | :---: | :--- |
| **ROC-AUC** | **0.643** | 0.628 | Khả năng xếp hạng phân biệt giữa 2 lớp |
| **Balanced Accuracy** | **61.8%** | 59.5% | Trung bình Recall của 2 lớp (chỉ số chuẩn khi lệch lớp) |
| **Recall (Target - 1)** | **66.7%** (442/663) | 58.2% (386/663) | Khả năng bắt trúng kích thích đích |
| **Precision (Target - 1)** | 20.4% | 21.5% | Tỉ lệ đoán đúng trong số các ca báo Target |
| **F1-Score (Macro)** | 0.510 | 0.514 | Trung bình điều hòa giữa Precision và Recall |
| **Accuracy tổng thể** | 58.7% | 60.8% | Bị kéo theo lớp đa số Standard |

### Chi tiết ma trận nhầm lẫn
- **Logistic Regression**: TN = 2.335, FP = 1.733, FN = 221, TP = 442 (phát hiện được 442/663 mẫu Target).
- **Random Forest**: TN = 2.490, FP = 1.578, FN = 277, TP = 386.

---

## 4. Nhận xét và kết luận

- **Về độ nhạy phát hiện Target**: Logistic Regression thể hiện ưu thế rõ rệt khi đạt Recall 66.7% trên lớp Target (phát hiện được 442/663 mẫu ở người mới). Diện tích dưới đường cong ROC đạt 0.643, cao hơn Random Forest (0.628) và vượt xa mức ngẫu nhiên 0.500.
- **So sánh hai hướng tiếp cận**: Sau khi chuẩn hóa, các đặc trưng năng lượng phổ có mối quan hệ tương đối tuyến tính với nhãn bài toán, giúp Logistic Regression hoạt động ổn định khi chuyển vùng sang đối tượng mới. Ngược lại, Random Forest có xu hướng thận trọng ở các nhánh lá, đạt Accuracy tổng thể cao hơn (60.8%) nhưng bỏ sót nhiều mẫu Target hơn (Recall đạt 58.2%).
- **Đóng góp**: Đã xây dựng hoàn chỉnh pipeline xử lý dữ liệu và trích xuất đặc trưng cho 42 đối tượng, lưu đệm nén `.npz` sẵn sàng để kết hợp với phần nghiên cứu đặc trưng thời gian của bạn Hòa trong báo cáo chung của Nhóm 9.
