from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
import os

driver = webdriver.Chrome()
driver.get("https://10fastfingers.com/typing-test/french")
os.system('pause')
WebDriverWait(driver, 60).until(EC.presence_of_element_located((By.ID, 'words')))
WebDriverWait(driver, 60).until(EC.presence_of_element_located((By.ID, 'row1')))
div_word_list = driver.find_element_by_id("row1")
spans_word_list = div_word_list.find_elements_by_xpath("./span")
len_spans_word_list = len(spans_word_list)
while len_spans_word_list == 0:
    sleep(0.5)
    div_word_list = driver.find_element_by_id("row1")
    spans_word_list = div_word_list.find_elements_by_xpath("./span")
    len_spans_word_list = len(spans_word_list)
word_list = []
for element in spans_word_list:
    word_list.append(element.get_attribute('innerText'))
input_field = driver.find_element_by_id('inputfield')
for word in word_list :
    input_field.send_keys(str(word))
    input_field.send_keys(Keys.SPACE)
    sleep(0.27)

