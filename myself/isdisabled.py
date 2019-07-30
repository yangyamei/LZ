from selenium import webdriver
import time as t
brower=webdriver.Chrome()
brower.get('http://www.baidu.com')
# locator=brower.find_element_by_xpath('//*[@id="cp"]')
# print(locator.is_displayed())
locator=brower.find_element_by_link_text('新闻')
print(locator.is_enabled())