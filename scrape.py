import os
import shutil
import time
import json

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# specifies the path to the chromedriver.exe
driver = webdriver.Chrome('path to chromdriver')

# driver.get method() will navigate to a page given by the URL address
driver.get('https://www.linkedin.com/login?fromSignIn=true&trk=guest_homepage-basic_nav-header-signin')

# locate email form by_class_name
username = driver.find_element_by_id('username')

# send_keys() to simulate key strokes
username.send_keys('username')

# locate password form by_class_name
password = driver.find_element_by_id('password')

# send_keys() to simulate key strokes
password.send_keys('****')

# locate submit button by_class_id
log_in_button = driver.find_element_by_class_name('login__form_action_container ')

# .click() to mimic button click
log_in_button.click()

try:
    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "ember12"))
    )
finally:
    driver.get('https://www.linkedin.com/jobs/search/?geoId=92000000&keywords=machine%20learning%20researcher&location=Worldwide')

start_item = 0
data = []

# to resume after Error 429 - linkedin servers block requests after too many requests...
if os.path.exists('job_texts.json'):
    with open('job_texts.json', 'r') as f:
        data = json.load(f)
    start_item = len(data)
    #backup
    if start_item > 0:
        shutil.copy('job_texts.json', '_job_texts.json')

while start_item < 1400:
    base_url = f"https://www.linkedin.com/jobs/search/?geoId=92000000&keywords=machine%20learning%20researcher&location=Worldwide&start={start_item}"
    driver.get(base_url)

    try:
        element = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "ul.jobs-search-results__list.artdeco-list"))
        )
    finally:
        time.sleep(3)

        lis = driver.find_elements_by_css_selector('li.occludable-update.artdeco-list__item--offset-2.artdeco-list__item.p0.ember-view')

        for i in range(10):
            lis[6].find_elements_by_tag_name('a')[0].send_keys(Keys.PAGE_DOWN)
            time.sleep(2)

        lis[6].find_elements_by_tag_name('a')[0].click()
        time.sleep(2)
        lis = driver.find_elements_by_css_selector(
            'li.occludable-update.artdeco-list__item--offset-2.artdeco-list__item.p0.ember-view')

        for l in lis:
            try:
                print(l.find_elements_by_tag_name('a')[0].get_attribute('href'))
                l.find_elements_by_tag_name('a')[0].click()
                job_text = driver.find_element_by_css_selector('div.jobs-box__html-content.jobs-description-content__text.t-14.t-normal').text
                data.append(job_text)
            except Exception as ex:
                print(ex)
            time.sleep(1)

    print("save")
    with open('job_texts.json', 'w') as f:
        json.dump(data, f)

    time.sleep(5)
    start_item+=25



    

