from selenium.webdriver import Chrome, ChromeOptions
import time

o = ChromeOptions()
o.add_experimental_option('detach', True)
driver = Chrome(options=o)

driver.get('https://www.flipkart.com/')

# driver.back()
# time.sleep(10)
# driver.forward()
# time.sleep(10)
# driver.refresh()
# time.sleep(10)
# driver.maximize_window()
# time.sleep(10)
# driver.minimize_window()
# time.sleep(10)
# driver.fullscreen_window()
# time.sleep(10)
# driver.close()

website_title = driver.title
print(website_title)

website_source_code = driver.page_source
print(website_source_code)

# hw: use other website and do the above