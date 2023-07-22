from selenium import webdriver

opts = webdriver.ChromeOptions()
# chrome.options - deprecated - but not :|
opts.add_argument('--disable-gpu')
browser1 = webdriver.Chrome(chrome_options=opts)
browser2 = webdriver.Chrome(chrome_options=opts)

browser1.get("http://techstepacademy.com/training-ground")
browser2.get("https://ebay.com")

# browser1.execute_script('window.open("http://techstepacademy.com/training-ground")')
#
#
#
# replace with not deprecated options
