import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
URL = 'https://humanbenchmark.com/tests/reactiontime'
PATH = '/Users/homepro/Development/CEG/chromedriver'

driver = webdriver.Chrome(PATH)

blue = "rgb(43, 135, 209)"
green = "rgb(75, 219, 106)"
red = "rgb(206, 38, 54)"
driver.get(URL)
box_to_click = driver.find_element_by_css_selector(
    'div.css-saet2v.view-splash')
# First Click
box_to_click.click()
print(box_to_click.value_of_css_property("background"))
try:
    wait = True
    while wait:
        if green in box_to_click.value_of_css_property("background"):
            wait = False
        print("red")
finally:
    box_to_click.click()
