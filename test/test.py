import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException

chrome_options = Options()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--disable-gpu')
chrome_options.add_argument("--disable-dev-shm-usage")
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument('user-agent="Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36"')

def wait(timeout):
    WebDriverWait(driver, timeout).until(lambda x: driver.execute_script("return jQuery.active == 0"))

driver = webdriver.Chrome(options=chrome_options)
driver.set_window_size(1024, 768)

driver.get('http://www.baidu.com')
wait(30)

driver.save_screenshot('/test/test.png')

