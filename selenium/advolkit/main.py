import os.path

from selenium import webdriver

project_directory = os.path.dirname(__file__)
PATH = (os.path.join(project_directory, "../cookie/./chromedriver"))

driver = webdriver.Chrome(PATH)
driver.get("https://www.twitch.tv/advolkit")
text_box = driver.find_element_by_xpath(
    """//*[@id="d6ba35aa81570f259da5f37122314b77"]/div/div[1]/div/div/div/div/div/section/div/div[4]/div[2]/div[1]/div/div[2]/div/div/textarea""")
text_box.send_keys("!vox from script")
