from selenium import webdriver
from selenium.webdriver.common.by import By
import requests
from PIL import Image
import requests
import pytesseract
from io import BytesIO

browser = webdriver.Firefox()
browser.get('https://www.chegg.com/homework-help/questions-and-answers/1-quasi-linear-utility-individual-utility-function-u-x-y-u-x-y-function-u-x-also-obeys-typ-q102370433')

image_element = browser.find_element(By.CSS_SELECTOR, "#chegg-main-content > div:nth-child(1) > section > div > p > img")

image_url = image_element.get_attribute("src")
response = requests.get(image_url)

# Specify the path where you want to save the image
image_path = "images/image4.png"

with open(image_path, "wb") as file:
    file.write(response.content)

print("Image downloaded successfully!")

response = requests.get(image_url)
image = Image.open(BytesIO(response.content))

ocr_text=pytesseract.image_to_string(image)
print(ocr_text)

#chegg-main-content > div:nth-child(1) > section > div > div > p > img
#mobile-question-style > div:nth-child(1) > img
#chegg-main-content > div:nth-child(1) > section > div > p > img
#mobile-question-style > div:nth-child(1) > img