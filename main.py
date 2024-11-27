from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
import time

service = Service(executable_path="chromedriver.exe")
driver = webdriver.Chrome(service=service)

driver.get("https://google.com")

WebDriverWait(driver, 5).until(
    EC.presence_of_element_located((By.ID, "APjFqb"))
)

input_element = driver.find_element(By.ID, "APjFqb")
input_element.clear()
input_element.send_keys("op gg", Keys.ENTER)

WebDriverWait(driver, 5).until(
    EC.presence_of_element_located((By.PARTIAL_LINK_TEXT, "OP.GG"))
)

link = driver.find_element(By.PARTIAL_LINK_TEXT, "OP.GG")
link.click()

WebDriverWait(driver, 5).until(
    EC.presence_of_element_located((By.ID, "searchHome"))
)

input_element = driver.find_element(By.ID, "searchHome")
region = driver.find_element(By.CLASS_NAME, "css-r2ch24.em8s8ey1")
region.click()

WebDriverWait(driver, 5).until(
    EC.presence_of_element_located((By.LINK_TEXT, "LAN"))
)

buttonLan = driver.find_element(By.LINK_TEXT, "LAN")
buttonLan.click()

input_element.clear()
input_element.send_keys("lalalxd", Keys.ENTER)

time.sleep(30)

driver.quit()
