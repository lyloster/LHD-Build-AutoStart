from selenium import webdriver


browser=webdriver.Chrome()

#first tab
browser.get('https://www.wunderground.com/')

#second tab
browser.execute_script("window.open('about:blank', 'tab2');")
browser.switch_to.window("tab2")
browser.get('http://reddit.com')
rSearch = browser.find_element_by_xpath('//*[@id="header-search-bar"]')
rSearch.send_keys("news")


#third tab
browser.execute_script("window.open('about:blank', 'tab3');")
browser.switch_to.window("tab3")
browser.get('http://outlook.com')

#fourth tab
browser.execute_script("window.open('about:blank', 'tab4');")
browser.switch_to.window("tab4")
browser.get('http://calendar.google.com')
