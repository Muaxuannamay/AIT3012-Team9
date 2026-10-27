"""
Script tải dữ liệu EEG mẫu từ OpenNeuro (ds004621).
Tải 80 giây đầu tiên từ bản ghi Oddball Task của sub-01 (127 kênh, ~39 MB).

Cách chạy:
    python download_real_sample.py
"""

import requests
from requests.adapters import HTTPAdapter
from urllib3.util import Retry
import concurrent.futures
import time
import os
import re

# === CẤU HÌNH ===
url = 'https://s3.amazonaws.com/openneuro.org/ds004621/sub-01/eeg/sub-01_task-oddball_eeg.eeg'
N_CHANS = 127
TOTAL_PTS = 1371320
CROP_PTS = 80000  # 80 giây tại 1000 Hz
bytes_per_ch = CROP_PTS * 4
orig_ch_stride = TOTAL_PTS * 4

# Đường dẫn tương đối (hoạt động trên mọi máy)
script_dir = os.path.dirname(os.path.abspath(__file__))
output_dir = os.path.join(script_dir, 'data', 'sub-01', 'eeg')
output_eeg = os.path.join(output_dir, 'sub-01_task-oddball_eeg.eeg')
vhdr_path = os.path.join(output_dir, 'sub-01_task-oddball_eeg.vhdr')

# Tạo thư mục nếu chưa có
os.makedirs(output_dir, exist_ok=True)

print(f"Đang tải 80 giây dữ liệu EEG thực nghiệm ({N_CHANS} kênh, {N_CHANS * bytes_per_ch / (1024*1024):.1f} MB)...")
print(f"Nguồn: OpenNeuro ds004621 / sub-01 / Oddball Task")

def make_session():
    s = requests.Session()
    retries = Retry(total=5, backoff_factor=0.5, status_forcelist=[500, 502, 503, 504])
    s.mount('https://', HTTPAdapter(max_retries=retries, pool_connections=8, pool_maxsize=8))
    return s

def fetch_channel(ch_idx, session):
    start = ch_idx * orig_ch_stride
    end = start + bytes_per_ch - 1
    headers = {'Range': f'bytes={start}-{end}'}
    resp = session.get(url, headers=headers, timeout=20)
    if resp.status_code != 206:
        raise RuntimeError(f"Kênh {ch_idx} trả về mã lỗi {resp.status_code}")
    return ch_idx, resp.content

t0 = time.time()
session = make_session()
data = [None] * N_CHANS

# Tải song song 4 kênh cùng lúc
with concurrent.futures.ThreadPoolExecutor(max_workers=4) as ex:
    futures = [ex.submit(fetch_channel, i, session) for i in range(N_CHANS)]
    done_count = 0
    for f in concurrent.futures.as_completed(futures):
        idx, chunk = f.result()
        data[idx] = chunk
        done_count += 1
        if done_count % 20 == 0 or done_count == N_CHANS:
            print(f"  Tiến trình: {done_count}/{N_CHANS} kênh đã tải xong")

# Ghi file EEG
with open(output_eeg, 'wb') as f:
    for chunk in data:
        f.write(chunk)

# Cập nhật DataPoints trong file .vhdr
if os.path.exists(vhdr_path):
    with open(vhdr_path, 'r', encoding='utf-8') as f:
        vhdr_content = f.read()
    vhdr_content = re.sub(r'DataPoints=\d+', f'DataPoints={CROP_PTS}', vhdr_content)
    with open(vhdr_path, 'w', encoding='utf-8') as f:
        f.write(vhdr_content)

dt = time.time() - t0
file_size = os.path.getsize(output_eeg) / (1024 * 1024)
print(f"\n✅ Tải thành công! {file_size:.1f} MB trong {dt:.1f} giây")
print(f"📁 File lưu tại: {output_eeg}")
