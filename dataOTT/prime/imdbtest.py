from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


options = webdriver.ChromeOptions()
# options.add_argument('headless')
options.add_argument("--window-size=1920,1080")
options.add_argument('--log-level=1') #low level logging (clean terminal)
#general bypass
options.add_argument("--user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36")
options.add_experimental_option ('excludeSwitches', ['enable-logging'])
options.add_experimental_option("excludeSwitches", ["enable-automation"])
#cloudflare bypass
options.add_experimental_option('useAutomationExtension', False) 
options.add_argument("--disable-blink-features=AutomationControlled")



w = webdriver.Chrome(options=options)

wait = WebDriverWait(w, 5)

showID = "tt0386676"
season = 9
f = open('test.json', "a")
ferr = open('testerr.txt', "a")
f.write("[\n")
for i in range(0, season):
    # print(f"Season {i+1} : ", end="")
    w.get(f'https://www.imdb.com/title/{showID}/episodes?season={str(i+1)}')
    div = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="episodes_content"]/div[2]/div[2]')))
    eps = list(div.find_elements_by_class_name('list_item'))

    # print(len(eps))
    for j in range(0,len(eps)):

        wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="episodes_content"]/div[2]/div[2]/div['+str(j+1)+']/div[2]/strong/a'))).click()

        try:
            link = wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="__next"]/main/div/section[1]/section/div[3]/section/section/div[4]/div[2]/div[2]/div/a'))).get_attribute('href')
        except:
            print(f"S{i+1}E{j+1}")
            ferr.write(f"S{i+1}E{j+1}\n")
            w.back()
            continue

        link = link.replace('https://www.primevideo.com/detail/amzn1.dv.gti.', '')
        f.write(f'"{link}",\n')
        w.back()

f.write("]")
f.close()
ferr.close()