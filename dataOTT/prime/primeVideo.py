from selenium import webdriver

options = webdriver.ChromeOptions()
#options.add_argument('headless')
options.add_argument('--log-level=1') #low level logging (clean terminal)
#general bypass
options.add_argument("--user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36")
options.add_experimental_option ('excludeSwitches', ['enable-logging'])
options.add_experimental_option("excludeSwitches", ["enable-automation"])
#cloudflare bypass
options.add_experimental_option('useAutomationExtension', False) 
options.add_argument("--disable-blink-features=AutomationControlled")
w = webdriver.Chrome(options=options)

w.get('https://www.primevideo.com/')