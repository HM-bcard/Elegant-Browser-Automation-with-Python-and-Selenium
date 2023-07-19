import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait


browser = webdriver.Chrome()

riddle1input = "input[id=r1Input]"
riddle1button = "button[id=r1Btn]"
riddle1answer = "div#passwordBanner > h4"

riddle2input = "input[id=r2Input]"
riddle2button = "button[id=r2Butn]"

riddle3input = "input[id=r3Input]"
riddle3button = "button[id=r3Butn]"

end_message_check = "button[id=checkButn]"
end_message = "div#trialCompleteBanner > h4"


Merchant_Jessica_Wealth = "//p[contains(text(),'3000')]/../span/b"
Merchant_Bernard_Wealth = "//p[contains(text(),'2000')]/../span/b"


browser.get("https://techstepacademy.com/trial-of-the-stones")
element1 = browser.find_element(By.CSS_SELECTOR, riddle1input)
element1.send_keys("rock")

element2 = browser.find_element(By.CSS_SELECTOR, riddle1button)
element2.click()

browser.find_element(By.CSS_SELECTOR, riddle1answer)

element3 = browser.find_element(By.CSS_SELECTOR, riddle1answer)


element4 = browser.find_element(By.CSS_SELECTOR, riddle2input)
element4.send_keys(element3.text)
element5 = browser.find_element(By.CSS_SELECTOR, riddle2button)
element5.click()

element6 = browser.find_element(By.CSS_SELECTOR, riddle3input)
element6.send_keys("Jessica")
element7 = browser.find_element(By.CSS_SELECTOR, riddle3button)
element7.click()

element8 = browser.find_element(By.CSS_SELECTOR, end_message_check)
element9 = browser.find_element(By.CSS_SELECTOR, end_message)
element8.click()

wait = WebDriverWait(browser, 10)
element10 = wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, end_message)))


assert element10.text == 'Trial Complete'
