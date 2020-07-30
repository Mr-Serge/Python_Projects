from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
driver.get('http://bkjx.wust.edu.cn/')
elem_Account = driver.find_element_by_id('userAccount')
elem_Password = driver.find_element_by_id('userPassword')
elem_button = driver.find_element_by_css_selector('button')
elem_Account.send_keys('201803166019')
elem_Password.send_keys('Gxj1114558916')
elem_button.click()

elem_grades = driver.find_element_by_css_selector('[data-code=NEW_XSD_XJCJ]')
elem_grades.click()