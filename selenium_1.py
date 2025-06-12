from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd
import time

usernames = [
    "standard_user", "locked_out_user", "problem_user", 
    "performance_glitch_user", "error_user", "visual_user"
]
password = "secret_sauce"

driver = webdriver.Chrome()
results = []

for username in usernames:
    driver.get("https://www.saucedemo.com/")
    time.sleep(1)

    driver.find_element(By.ID, "user-name").clear()
    driver.find_element(By.ID, "password").clear()
    driver.find_element(By.ID, "user-name").send_keys(username)
    driver.find_element(By.ID, "password").send_keys(password)
    driver.find_element(By.ID, "login-button").click()
    time.sleep(1)

    # Kiểm tra đăng nhập
    if "inventory" in driver.current_url:
        try:
            items = driver.find_elements(By.CLASS_NAME, "inventory_item")
            if not items:
                results.append({
                    "Username": username,
                    "Status": "Thành công",
                    "Reason": "Không có sản phẩm",
                    "Product": "",
                    "Price": ""
                })
            else:
                for item in items:
                    name = item.find_element(By.CLASS_NAME, "inventory_item_name").text
                    price = item.find_element(By.CLASS_NAME, "inventory_item_price").text
                    results.append({
                        "Username": username,
                        "Status": "Thành công",
                        "Reason": "",
                        "Product": name,
                        "Price": price
                    })
        except:
            results.append({
                "Username": username,
                "Status": "Thành công",
                "Reason": "Lỗi khi lấy sản phẩm",
                "Product": "",
                "Price": ""
            })

        # Logout
        try:
            driver.find_element(By.ID, "react-burger-menu-btn").click()
            time.sleep(0.5)
            driver.find_element(By.ID, "logout_sidebar_link").click()
        except:
            pass
    else:
        # Đăng nhập lỗi
        try:
            error = driver.find_element(By.CLASS_NAME, "error-message-container").text
        except:
            error = "Không rõ lỗi"
        results.append({
            "Username": username,
            "Status": "Thất bại",
            "Reason": error,
            "Product": "",
            "Price": ""
        })

driver.quit()

# Ghi ra file
df = pd.DataFrame(results)
df.to_excel("saucedemo.xlsx", index=False)

print("Xong, dữ liệu lưu ở saucedemo.xlsx")