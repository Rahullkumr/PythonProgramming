from selenium.webdriver import Chrome, ChromeOptions

x = ChromeOptions()
x.add_experimental_option('detach', True)
driver = Chrome(options=x)
driver.get('https://www.flipkart.com/')
driver.maximize_window()
data=driver.find_element("class name","tLbyDf")
# if there is space in
# print(data)     # give object address
print(data.text)

driver.close()