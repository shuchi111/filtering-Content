from selenium import webdriver
from selenium.webdriver.common.by import By
import requests
from PIL import Image
import requests
import pytesseract
from io import BytesIO
import pandas as pd

df=pd.read_csv('Sample Sheet.csv')

browser = webdriver.Chrome()

for i in range(1,5): #df['Link'].count()+1
    browser.get(df['Link'][i])

    try:
        image_element = browser.find_element(By.CSS_SELECTOR, "#chegg-main-content > div:nth-child(1) > section > div > p > img:nth-child(1)")
    except:
        continue

    image_url = image_element.get_attribute("src")
    response = requests.get(image_url)

    # Specify the path where you want to save the image
    image_path = "images/image[i].png".format(i=i)


    #FOR OCR
    
    """
    with open(image_path, "wb") as file:
        file.write(response.content)

    print("Image[i] downloaded successfully!".format(i=i))

    response = requests.get(image_url)
    image = Image.open(BytesIO(response.content))

    ocr_text=pytesseract.image_to_string(image)
    print(ocr_text)
    """

#chegg-main-content > div:nth-child(1) > section > div > div > p > img
#mobile-question-style > div:nth-child(1) > img
#chegg-main-content > div:nth-child(1) > section > div > p > img
#mobile-question-style > div:nth-child(1) > img