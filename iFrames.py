from selenium import webdriver
from selenium.webdriver.common.by import By

browser = webdriver.Chrome()

opts = webdriver.ChromeOptions()
# chrome.options - deprecated - but not :|
opts.add_argument('--disable-gpu')
browser1 = webdriver.Chrome(chrome_options=opts)

browser1.get("https://techstepacademy.com/iframe-training")
# browser2.get("https://ebay.com")

browser1.execute_script('window.open("https://techstepacademy.com/iframe-training", "_blank")')
browser1.execute_script('window.open("http://techstepacademy.com/training-ground", "_blank")')
browser1.execute_script('window.open("http://techstepacademy.com/training-ground", "_blank")')

browser.get('https://techstepacademy.com/iframe-training')
welcome_text = browser.find_element(By.CSS_SELECTOR, )

iframe = browser.find_element(By.CSS_SELECTOR, "iframe")
browser.switch_to.frame(iframe)
welcome_text = browser.find_element(By.CSS_SELECTOR, "div#block-ec928cee802cf918d26c div p")
welcome_text.text

title_text = browser.find_element(By.CSS_SELECTOR,"div#block-5d3de848045889000188d389")
# first you need to swtich out of the iframe:
browser.switch_to.default_content()
