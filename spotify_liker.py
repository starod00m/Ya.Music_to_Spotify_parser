from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
import time
import argparse

parser = argparse.ArgumentParser(description='Spotify liker')

parser.add_argument('login', action="store", help='login')
parser.add_argument('password', action="store", help='password')
parser.add_argument('-p', '--path', dest='path', default='chromedriver.exe', help='Path to chromedriver.exe')
parser.add_argument('-f', '--file', dest='file', default='result.txt', help='Path to result.txt')

args = parser.parse_args()

def get_tracks() -> list:
    tracks = []
    with open(args.file, 'r', encoding='utf-8') as f:
        for line in f:
            tracks.append(' '.join(line.split()))
    return tracks

tracks = get_tracks()
options = webdriver.ChromeOptions()
options.add_experimental_option("excludeSwitches", ["enable-logging"])
browser = webdriver.Chrome(options=options, executable_path=args.path)
browser.get('https://accounts.spotify.com/en/login?continue=https:%2F%2Fopen.spotify.com%2F')
time.sleep(1)
browser.find_element_by_id('login-username').send_keys(args.login)
browser.find_element_by_id('login-password').send_keys(args.password)
browser.find_element_by_id('login-button').click()
time.sleep(1)
browser.get('https://open.spotify.com/search')
time.sleep(1)
for i, track in enumerate(tracks):
    if i + 1 % 10 == 0:
        time.sleep(10)
    try:
        browser.find_element_by_css_selector('input[data-testid]').clear()
        time.sleep(1)
        browser.find_element_by_css_selector('input[data-testid]').send_keys(track)
        time.sleep(1)
        browser.find_element_by_css_selector('div[data-testid="tracklist-row"]').click()
        time.sleep(1)
        try:
            browser.find_element_by_css_selector('div[aria-rowindex="1"] button[aria-checked="false"]').click()
        except NoSuchElementException:
            msg = f'Track {track} already liked'
            print(msg)
            with open('already_liked.txt', 'a', encoding='utf-8') as f:
                f.write(msg + '\n')
            continue
        time.sleep(1)
    except NoSuchElementException:
        msg = f'Can\'t like {track}'
        print(msg)
        with open('cant like.txt', 'a', encoding='utf-8') as f:
            f.write(msg + '\n')
        continue

browser.close()