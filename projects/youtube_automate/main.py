from selenium import webdriver

driver = webdriver.Firefox(executable_path='./geckodriver')
driver.get('https://youtube.com')
search_box = driver.find_element_by_xpath('//input[@id="search"]')
# print(search_box)
search_box.send_keys('Migos')

searchButton = driver.find_element_by_xpath('//*[@id="search-icon-legacy"]')
# print(searchButton)
searchButton.click()
