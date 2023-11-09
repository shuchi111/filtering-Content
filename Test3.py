from selenium import webdriver
from selenium.webdriver.common.by import By
import requests

browser = webdriver.Firefox()
browser.get('https://chegg.com/homework-help/questions-and-answers/3110-another-version-predator-prey-model-begin-aligned-p-t-1-p-t-e-r-left-1-p-t-k-right-s--q102272907')

image_element = browser.find_element(By.CSS_SELECTOR, "#chegg-main-content > div:nth-child(1) > section > div > div > p > img:nth-child(1)")

image_url = image_element.get_attribute("src")
response = requests.get(image_url)

# Specify the path where you want to save the image
image_path = "images/image2.png"

with open(image_path, "wb") as file:
    file.write(response.content)

print("Image downloaded successfully!")


#chegg-main-content > div:nth-child(1) > section > div > div > p > img
#mobile-question-style > div:nth-child(1) > img
#chegg-main-content > div:nth-child(1) > section > div > p > img
#mobile-question-style > div:nth-child(1) > img