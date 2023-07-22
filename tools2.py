from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.support.expected_conditions import alert_is_present
from selenium.webdriver.common.by import By

#WebDriver
browser = webdriver.Chrome()

browser.get("http://techstepacademy.com/training-ground")

#alert = Alert(browser)

#print("I have arrived")
#WebDriverWait(browser, 20).until(alert_is_present())
#print("An alert appeared")


sel = browser.find_element(By.ID, 'sel1')
my_select = Select(sel)
[elem.text for elem in my_select.options]
print(elem.text)

my_select.select_by_visible_text('Battlestar Galactica')
my_select.select_by_index(0)
my_select.deselect_by_value('second')
