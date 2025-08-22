from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

username = 'michellechiang'
password = '@@rSC801567'
url = 'http://172.16.2.66/EIP/portal_frame?key=bWVudV9sb2NhbGVrZXk9bXNpLm1lbnUuVDA0NDQ1Jm1pZD0zOCZhY3Rpdml0eV92aWV3PVFVTlVTVlpKVkZsZlNVUTlOemM1TmpFJTNE'

# 記錄開始時間
start_time = time.time()

driver = webdriver.Chrome()
wait = WebDriverWait(driver, 10)
driver.get(url)

# Login 按鈕
login_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='mainnav']/div/form/button[2]")))
login_button.click()

# 切換到 iframe 登入
wait.until(EC.frame_to_be_available_and_switch_to_it((By.ID, "iframe_content")))

login_name = wait.until(EC.presence_of_element_located((By.NAME, 'username')))
login_name.send_keys(username)

login_password = wait.until(EC.presence_of_element_located((By.NAME, 'password')))
login_password.send_keys(password)

submit = wait.until(EC.presence_of_element_located((By.NAME, 'btn_login')))
driver.execute_script("arguments[0].click();", submit)

# 回到主文檔，再進入 iframe
driver.switch_to.default_content()
wait.until(EC.frame_to_be_available_and_switch_to_it((By.ID, "iframe_content")))

# Sign Up 頁面
signUp_page = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "a[href='#signup']")))
driver.execute_script("arguments[0].click();", signUp_page)

# 點擊 Sign Up 按鈕
signUp_button1 = wait.until(EC.presence_of_element_located((By.ID, "btn_signup")))
driver.execute_script("arguments[0].click();", signUp_button1)

signUp_button2 = wait.until(EC.presence_of_element_located((By.ID, "btn_signup")))
driver.execute_script("arguments[0].click();", signUp_button2)

'''
#填寫資料
fullname = 'POOH'
age ='20'

#name
name = wait.until(EC.element_to_be_clickable((By.NAME, 'fullname')))
name.send_keys(fullname)

#gender
gender = wait.until(EC.element_to_be_clickable((By.ID,'sex')))
gender.click()

#age 
Age = wait.until(EC.element_to_be_clickable((By.NAME,'age')))
Age.send_keys(age)
'''

# 儲存
#save_btn = wait.until(EC.presence_of_element_located((By.ID, "btn_save")))
save_btn = wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[4]/div/div/div[3]/button[2]")))
driver.execute_script("arguments[0].click();", save_btn)

# 記錄結束時間
end_time = time.time()

# 計算花費秒數
elapsed_time = end_time - start_time
print(f"程式執行到 click() 花費時間: {elapsed_time:.2f} 秒")

time.sleep(2)
