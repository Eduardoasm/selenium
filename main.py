from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import json

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
    EC.presence_of_element_located(
        (By.XPATH, "//button[contains(@class, 'css-60l9xa em8s8ey3')]/span[text()='LAN']"))
)

buttonLan = driver.find_element(
    By.XPATH, "//button[contains(@class, 'css-60l9xa em8s8ey3')]/span[text() = 'LAN']")
buttonLan.click()

input_element.clear()
input_element.send_keys("shir4k0", Keys.ENTER)

disabledButton = "DISABLE css-1r09es5 e17xj3f90"
enabledButton = "IDLE css-1ki6o6m e17xj3f90"

WebDriverWait(driver, 5).until(
    EC.element_to_be_clickable(
        (By.CSS_SELECTOR, ".IDLE.css-1ki6o6m.e17xj3f90")
    )
)

enabledButton = driver.find_element(
    By.CSS_SELECTOR, ".IDLE.css-1ki6o6m.e17xj3f90")
enabledButton.click()

WebDriverWait(driver, 7).until(
    EC.presence_of_element_located(
        (By.CSS_SELECTOR, ".DISABLE.css-1r09es5.e17xj3f90"))
)

WebDriverWait(driver, 3).until(
    EC.presence_of_element_located(
        (By.CLASS_NAME, "tier"))
)

tier = driver.find_element(By.CLASS_NAME, "tier").text
lp = driver.find_element(By.CLASS_NAME, "lp").text

data = {
    "tier": tier,
    "lp": lp,
}

with open("data.json", "w") as file:
    json.dump(data, file, indent=4)


time.sleep(30)

driver.quit()
