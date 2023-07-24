from selenium import webdriver

opts = webdriver.ChromeOptions()
# chrome.options - deprecated - but not :|
opts.add_argument('--disable-gpu')
browser1 = webdriver.Chrome(chrome_options=opts)
browser2 = webdriver.Chrome(chrome_options=opts)

browser1.get("http://techstepacademy.com/training-ground")
# browser2.get("https://ebay.com")

browser1.execute_script('window.open("http://techstepacademy.com/training-ground", "_blank")')
browser1.execute_script('window.open("http://techstepacademy.com/training-ground", "_blank")')
browser1.execute_script('window.open("http://techstepacademy.com/training-ground", "_blank")')
browser1.execute_script('window.open("https://ebay.com", "_blank")')
browser1.implicitly_wait(15)


# replace with not deprecated options

browser1.window_handles
len(browser1.window_handles)
handles = browser1.window_handles
browser1.switch_to.window(handles[0])

#window handles(tabs) aren't called in the same order that they are displayed in

