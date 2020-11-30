from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
import time
import argparse

parser = argparse.ArgumentParser(description='Ya.Music parser')

parser.add_argument('url', action="store", help='Ya.Music url to parse')
parser.add_argument('-p', '--path', dest='path', default='chromedriver.exe', help='Path to chromedriver.exe')

args = parser.parse_args()

options = webdriver.ChromeOptions()
options.add_experimental_option("excludeSwitches", ["enable-logging"])
browser = webdriver.Chrome(options=options, executable_path=args.path)

browser.get(args.url)
time.sleep(1)

# Пытаемся закрыть рекламу
try:
    browser.find_element_by_css_selector('div.payment-plus__header-close span.d-icon_cross-big').click()
except NoSuchElementException:
    pass
time.sleep(10)
tracks = []
is_end = False
while True:
    try:
        if not is_end:
            is_end = True
            time.sleep(0.5)
            elements = browser.find_elements_by_css_selector('div.typo-track div.d-track__overflowable-wrapper')
            for element in elements:
                track = ' '.join(element.text.split('\n'))
                if track not in tracks:
                    tracks.append(track)
                    is_end = False
            time.sleep(0.5)
            browser.find_element_by_tag_name('body').send_keys(Keys.PAGE_DOWN)
            browser.find_element_by_tag_name('body').send_keys(Keys.PAGE_DOWN)
        else:
            break
    except NoSuchElementException:
        continue
with open('result.txt', 'w', encoding='utf-8') as f:
    for track in tracks:
        f.write(track + '\n')
browser.close()