import os.path

from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains

project_directory = os.path.dirname(__file__)
PATH = (os.path.join(project_directory, "./chromedriver"))

driver = webdriver.Chrome(PATH)
driver.get("http://orteil.dashnet.org/cookieclicker/")

driver.implicitly_wait(5)

# Cookie that have to be click
cookie = driver.find_element_by_id("bigCookie")
cookie_count = driver.find_element_by_id("cookies")
# Range(1, -1, -1) mean start from 1 and go to 0
items = [driver.find_element_by_id("productPrice" + str(i)) for i in
         range(1, -1, -1)]

actions = ActionChains(driver)
actions.click(cookie)

for i in range(5000):
    actions.perform()
    # Get the value of cookie_count by splitting
    count = int(cookie_count.text.split(" ")[0])
    for item in items:
        # Get the price of the items
        value = int(item.text)
        if value <= count:
            upgrade_actions = ActionChains(driver)
            upgrade_actions.move_to_element(item)
            upgrade_actions.click()
            upgrade_actions.perform()
