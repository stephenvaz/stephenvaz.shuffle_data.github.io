from gettext import find
from selenium import webdriver
import time

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



w = webdriver.Chrome(executable_path="chromedriver.exe" ,options=options)

showID = "tt0386676"
season = 9

# nSeasons = int(input())
for i in range(0, season):
    # if(season == 1):
    #     w.get("https://www.imdb.com/title/" + showID + "/episodes")
    #     print(w.find_element_by_xpath('/html/body/div[2]/div/div[2]/div[3]/div[1]/div[1]/div[2]/div[2]/h3'))
    
    w.get(f'https://www.imdb.com/title/{showID}/episodes?season={str(i+1)}')
    div = w.find_element_by_xpath('//*[@id="episodes_content"]/div[2]/div[2]')
    eps = list(div.find_elements_by_class_name('list_item'))
    w.execute_script("var scrollingElement = (document.scrollingElement || document.body);scrollingElement.scrollTop = scrollingElement.scrollHeight;")
    time.sleep(3)
    print(len(eps))
    for j in range(0,len(eps)):
        #//*[@id="episodes_content"]/div[2]/div[2]/div[1]/div[2]/div[4]/span/div/a[1]

        #//*[@id="episodes_content"]/div[2]/div[2]/div[1]/div[2]/div[4]/span/div/a[1]

        #//*[@id="episodes_content"]/div[2]/div[2]/div[2]/div[2]/div[4]/span/div/a[1]
        link = w.find_element_by_xpath('//*[@id="episodes_content"]/div[2]/div[2]/div['+str(j+1)+']/div[2]/div[4]/span/div/a[1]').get_attribute('href')
        print(link)