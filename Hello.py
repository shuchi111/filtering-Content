from selenium import webdriver
from selenium.webdriver.common.by import By

browser = webdriver.Firefox()
browser.get('https://www.chegg.com/homework-help/questions-and-answers/consumer-130-monthly-income-spent-two-goods-z-b--price-operatorname-good-z-left-p-z-right--q102370392')

elem_list = browser.find_element(By.CSS_SELECTOR,"#chegg-main-content > div:nth-child(1) > section > div > p > img:nth-child(1)")

print(elem_list)
