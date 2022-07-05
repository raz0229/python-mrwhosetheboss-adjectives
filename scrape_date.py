from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.webdriver import FirefoxProfile
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
import os

options = Options()
options.headless = False

profile = FirefoxProfile("/home/raz0229/.mozilla/firefox/58m1hr3k.dev-edition-default")

# Configuration
PATH = "/home/raz0229/Downloads/geckodriver"  # path to your downloaded webdriver

driver = webdriver.Firefox(profile, executable_path=PATH, options=options)

if __name__ == '__main__':
    try:
        w=open('url_list_copy.txt', 'a')
        with open('url_list.txt', 'r') as f:
            for line in f:
                file = line.split()
                url = file[1]
                driver.get(url)
                date = WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "#info-strings yt-formatted-string")))
                w.write(f'{line} {date.text}\n')
                # Force the OS to store the file buffer to disc
                w.flush()
                os.fsync(w.fileno())
            driver.close()

    except Exception as e:
        print(e)
        print('\n[ERROR] File: \'url_list.txt\' not found. Please run \'main.py\' first')
