from selenium import webdriver
from selenium.webdriver.common.by import By

browser = webdriver.Chrome()


search_page = EbaySearchPage(driver=browser).go()
search_page.search.input.text = "fender jazzmaster"
search_page.search_button.click()

results_page - EbayResultsPage(driver=browser)
assert len(results_page.results) > 0

