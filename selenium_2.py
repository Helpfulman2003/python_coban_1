from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd

BASE = "https://thuvienphapluat.vn/ma-so-thue/tra-cuu-ma-so-thue-doanh-nghiep"
driver = webdriver.Chrome()

data = {}

for pg in range(1, 6):
    url = f"{BASE}?page={pg}&pageSize=50"
    print(f"Lấy trang {pg}: {url}")
    driver.get(url)

    # Chờ cho bảng load
    try:
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "table tr"))
        )
    except:
        print(f"Trang {pg} không tải được dữ liệu")
        continue

    rows = driver.find_elements(By.CSS_SELECTOR, "table tr")[1:] 
    arr = []
    for r in rows:
        cols = r.find_elements(By.TAG_NAME, "td")
        if len(cols) >= 4:
            arr.append({
                "MST": cols[1].text,
                "Tên DN": cols[2].text,
                "Ngày cấp": cols[3].text
            })
    data[f"Trang_{pg}"] = pd.DataFrame(arr)

driver.quit()

# Ghi Excel
with pd.ExcelWriter("thuvienphapluat.xlsx") as w:
    for sheet, df in data.items():
        df.to_excel(w, sheet_name=sheet, index=False)

print("Hoàn thành: thuvienphapluat.xlsx")