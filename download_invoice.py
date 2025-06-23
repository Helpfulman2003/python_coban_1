from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import time

# 1. Hàm mở trình duyệt: cấu hình download file selenium


def mo_trinh_duyet():
    options = Options()
    options.add_argument("--start-maximized")
    prefs = {"download.prompt_for_download": False}
    options.add_experimental_option("prefs", prefs)
    return webdriver.Chrome(options=options)

# 2. Hàm nhập mã tra cứu


def doc_ma_tra_cuu(file_path="ma_tra_cuu.txt"):
    with open(file_path, 'r', encoding='utf-8') as f:
        return [line.strip() for line in f if line.strip()]

# 3. Hàm thực hiện tìm kiếm


def thuc_hien_tra_cuu(driver, ma):
    driver.get("https://www.meinvoice.vn/tra-cuu")
    try:
        # Nhập mã tra cứu vào ô input
        input_box = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(
                (By.CSS_SELECTOR, 'input[placeholder="Nhập mã tra cứu hóa đơn"]'))
        )
        input_box.clear()
        input_box.send_keys(ma)

        # Nhấn nút tìm kiếm
        nut_tim = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, "btnSearchInvoice"))
        )
        nut_tim.click()
        return True
    except Exception as e:
        print(f"Lỗi khi nhập mã hoặc nhấn tìm kiếm: {e}")
        return False

# 4. Hàm xử lý kết quả tìm kiếm và tải hóa đơn


def xu_ly_ket_qua(driver, ma):
    try:
        # Chờ nút tải hóa đơn xuất hiện và nhấn vào
        nut_tai_hoa_don = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable(
                (By.CSS_SELECTOR, "span.download-invoice"))
        )
        nut_tai_hoa_don.click()

        # Chọn tải file PDF
        btn_pdf = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(
                (By.CSS_SELECTOR, "div.txt-download-pdf"))
        )
        btn_pdf.click()

        # Có thể chụp màn hình làm minh chứng (nếu cần)
        driver.save_screenshot(f"{ma}.png")

        ghi_log(ma, "Tải thành công")
    except TimeoutException:
        ghi_log(ma, "Không tìm thấy hóa đơn hoặc không hiện popup")
    except Exception as e:
        ghi_log(ma, f"Lỗi khác: {str(e)}")

# 5. Hàm ghi log kết quả


def ghi_log(ma, trang_thai):
    with open("log.txt", "a", encoding="utf-8") as f:
        f.write(f"{ma}: {trang_thai}\n")

# Hàm chính thực hiện các bước theo yêu cầu


def main():
    # 1. Truy cập trang web tra cứu hóa đơn điện tử của meinvoice.vn.
    driver = mo_trinh_duyet()

    # 2. Nhập mã tra cứu hóa đơn vào trong tương ứng.
    danh_sach_ma = doc_ma_tra_cuu()

    for ma in danh_sach_ma:
        print(f"Đang xử lý: {ma}")
        # 3. Thực hiện hành động tìm kiếm.
        if thuc_hien_tra_cuu(driver, ma):
            # 4. Xử lý kết quả tìm kiếm, tải hóa đơn về máy.
            xu_ly_ket_qua(driver, ma)
        else:
            ghi_log(ma, "Không thể nhập mã hoặc nhấn tìm kiếm")
        time.sleep(2)  # Nghỉ 2 giây giữa các lần tra cứu

    driver.quit()
    print("Đã xử lý xong toàn bộ mã tra cứu.")


if __name__ == "__main__":
    main()
