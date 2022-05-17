import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

website = 'https://mdcoxe.github.io/panorama-to-cubemap/'
os.environ['PATH'] += ':/home/michaelc/AES/pano-selenium/selenium-driver'
filename = 'GSAA5586.jpg'


options = webdriver.ChromeOptions()
prefs = {"download.default_directory": "/home/michaelc/Downloads", "safebrowsing.enabled": "false"}
options.add_experimental_option('prefs', prefs)
options.add_argument('--no-sandbox')
options.add_argument("--headless")
options.add_argument("--no-startup-window")
options.add_argument("--disable-gpu")

driver = webdriver.Chrome( options=options)
driver.get(website)

choose_file = driver.find_element(By.XPATH, '//input[@id="imageInput"]')
choose_file.send_keys('/home/michaelc/Downloads/' + filename)

time.sleep(5)
py_img = driver.find_element(By.XPATH, '//a[@title="py"]')
driver.execute_script("arguments[0].click();", py_img)
# py_img.click()
time.sleep(5)
nx_img = driver.find_element(By.XPATH, '//a[@title="nx"]')
driver.execute_script("arguments[0].click();", nx_img)
# nx_img.click()
time.sleep(5)
pz_img = driver.find_element(By.XPATH, '//a[@title="pz"]')
driver.execute_script("arguments[0].click();", pz_img)
# pz_img.click()
time.sleep(5)
px_img = driver.find_element(By.XPATH, '//a[@title="px"]')
driver.execute_script("arguments[0].click();", px_img)
# px_img.click()
time.sleep(5)
nz_img = driver.find_element(By.XPATH, '//a[@title="nz"]')
driver.execute_script("arguments[0].click();", nz_img)
# nz_img.click()
time.sleep(5)
ny_img = driver.find_element(By.XPATH, '//a[@title="ny"]')
driver.execute_script("arguments[0].click();", ny_img)

# ny_img.click()
print('Complete')