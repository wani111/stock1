from selenium import webdriver

driver = webdriver.Firefox()
# driver = webdriver.Chrome()

driver.get('http://icanhazip.com/')

print(driver.page_source)

driver.quit()

profile = webdriver.FirefoxProfile()
profile.set_preference("network.proxy.type", 1)
profile.set_preference("network.proxy.socks", "127.0.0.1")
profile.set_preference("network.proxy.socks_port", 9050)

profile.update_preferences()

driver = webdriver.Firefox(profile)

driver.get('http://icanhazip.com/')

print(driver.page_source)

driver.quit()
