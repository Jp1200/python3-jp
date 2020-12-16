import time

from selenium import webdriver

URL = 'https://humanbenchmark.com/tests/reactiontime'
PATH = '/Users/homepro/Development/CEG/chromedriver'

driver = webdriver.Chrome(PATH)

blue = "rgb(43, 135, 209)"
green = "rgb(75, 219, 106)"
red = "rgb(206, 38, 54)"
driver.get(URL)
box_to_click = driver.find_element_by_css_selector(
    'div.css-saet2v.view-splash')


start = time.time()

for i in range(5):
    box_to_click.click()
    try:
        wait = True
        while wait:
            if green in box_to_click.value_of_css_property("background"):
                wait = False

    finally:
        print("Clicked!")
        box_to_click.click()
end = time.time()
print(f"Average time to complete whole test ~{int(end-start)}")
time.sleep(5)
print("Closing...")
driver.quit()
