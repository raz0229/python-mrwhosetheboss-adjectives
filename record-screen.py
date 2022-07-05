from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.webdriver import FirefoxProfile
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from threading import Thread
from time import sleep
import subprocess

def recordmydesktop(name):
    subprocess.run(f'recordmydesktop -o downloads/{name}.ogv --on-the-fly-encoding --fps=25 > /dev/null 2>&1', shell=True)

options = Options()
options.headless = False

profile = FirefoxProfile("/home/raz0229/.mozilla/firefox/58m1hr3k.dev-edition-default")

# Configuration
PATH = "/home/raz0229/Downloads/geckodriver"  # path to your downloaded webdriver
DELAY = 12 # seconds (depending on your internet connection speed)

driver = webdriver.Firefox(profile, executable_path=PATH, options=options)

if __name__ == '__main__':
    try:
        with open('url_list.txt', 'r') as f:
            for line in f:
                file = line.split()
                url = file[1]
                filename = file[0]
                driver.get(url)
                fullScreenButton = WebDriverWait(driver, DELAY).until(EC.presence_of_element_located((By.CSS_SELECTOR, '.ytp-fullscreen-button.ytp-button')))
                fullScreenButton.click()
                sleep(2)
                # playButton = WebDriverWait(driver, DELAY).until(EC.presence_of_element_located((By.CSS_SELECTOR, '.ytp-play-button.ytp-button')))
                # playButton.click()
                thread = Thread(target=recordmydesktop, args=(f"{filename}",))
                thread.start()
                sleep(DELAY)
                subprocess.run('kill -9 recordmydesktop', shell=True)
                print('\n Saved Recording: \'' + filename + '.ogv\' in {PWD}/downloads ')  # prints title of the webpage
            driver.close()

    except Exception as e:
        print(e)
        print('\n[ERROR] File: \'url_list.txt\' not found. Please run \'main.py\' first')
