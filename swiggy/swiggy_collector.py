
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time
from bs4 import BeautifulSoup
from selenium.webdriver.common.action_chains import ActionChains
driver = webdriver.Chrome(ChromeDriverManager().install())

driver.get("https://www.swiggy.com/")
time.sleep(3)
driver.find_element_by_xpath('//*[@id="root"]/div[1]/div[1]/div/div[1]/div[1]/div/div[1]/div/a[1]').click()
time.sleep(3)
print("enter phone number")
mobile= input()
time.sleep(6)
loginBox = driver.find_element_by_xpath('//*[@id="mobile"]')
loginBox.send_keys(mobile) 

time.sleep(2)
driver.find_element_by_xpath('//*[@id="overlay-sidebar-root"]/div/div/div[2]/div/div/div/form/div[2]/a').click()

time.sleep(20)

# -----
print("Enter OTP")
otp = input()
time.sleep(2)
driver.find_element_by_xpath('//*[@id="otp"]').send_keys(otp)
time.sleep(2)
otp_btn = driver.find_element_by_xpath('//*[@id="overlay-sidebar-root"]/div/div/div[2]/div/div/div/div[2]/form/div[2]/div[2]/a')

actions = ActionChains(driver)
actions.move_to_element(otp_btn).click().perform()

# ------

time.sleep(7)

driver.find_element_by_xpath('//*[@id="root"]/div[1]/header/div/div/ul/li[2]/div/div/div/a').click()
time.sleep(5)

time.sleep(4)
html = driver.page_source
soup = BeautifulSoup(html,'html.parser')


pl = []
it=[]
ct =[]
dt=[]
r=0
x=12
s=0
for j in range(32):
  time.sleep(2)
  html = driver.page_source
  soup = BeautifulSoup(html,'html.parser')
  time.sleep(2)
  place = soup.find_all( class_ = "_3h4gz" )
  item = soup.find_all( class_ = "nRCg_" )
  cost = soup.find_all( class_ = "_3Hghg" )
  date = soup.find_all( class_ ='_2uT6l')
  r=r+10
  for i in range(s,r):
    
    pl.append(place[i].text)
    it.append(item[i].text)
    ct.append(cost[i].text)
    dt.append(date[i].text)
  time.sleep(4)
  show = driver.find_element_by_xpath(f'//*[@id="root"]/div[1]/div[1]/div[1]/div[3]/div[2]/div/div[2]/div/div/div[{x}]')
  x=x+10
  s=s+10
  actions = ActionChains(driver)
  actions.move_to_element(show)
  actions.click(show)
  actions.perform()
  

#   //*[@id="root"]/div[1]/div[1]/div[1]/div[3]/div[2]/div/div[2]/div/div/div[23]
#   //*[@id="root"]/div[1]/div[1]/div[1]/div[3]/div[2]/div/div[2]/div/div/div[33]
# //*[@id="root"]/div[1]/div[1]/div[1]/div[3]/div[2]/div/div[2]/div/div/div[32]
print(len(dt))
print(len(pl))
print(len(it))
print(len(ct))
import pandas as pd

dict = {'date': dt, 'place':pl,'item':it,'cost':ct}
df = pd.DataFrame(dict)

df.to_csv("swiggy3.csv")
