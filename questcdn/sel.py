from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import NoSuchElementException
import xlsxwriter

# DRIVER_PATH = "C:\DEVELOPMENT\chromedriver.exe"

conn = webdriver.Chrome()

conn.get("https://www.questcdn.com/")
time.sleep(5)
login = conn.find_element_by_xpath('//*[@id="topBar"]/div[2]/ul[2]/li/a')
login.click()
time.sleep(2)
username = conn.find_element_by_css_selector("#id_username")
username.send_keys(f"{input('put your userid')}")

password = conn.find_element_by_css_selector("#id_password")
password.send_keys(f"{input('put your userid password')}")

log = conn.find_element_by_xpath('//*[@id="contact-us-form"]/div/div[3]/form/div[2]/div/button')
log.click()

time.sleep(5)
industry_directory = conn.find_element_by_css_selector('#topMain > li:nth-child(4) > a')
industry_directory.click()
time.sleep(20)
element_list = []
for i in range(1100,2000):
    url = 'https://www.questcdn.com/quest/idir/view/'+ str(i)+'/?path=349'
    conn.get(url)
    time.sleep(2)
    name = conn.find_element_by_css_selector('.mb-10')
    bussiness_profile = conn.find_element_by_css_selector('#wrapper > div.pt-100 > div.visible-print > div > div.row > div.col-md-10 > div > div.toggle.active > div > table > tbody > tr:nth-child(1) > td:nth-child(2)')
    bussiness_cert = conn.find_element_by_css_selector('#wrapper > div.pt-100 > div.visible-print > div > div.row > div.col-md-10 > div > div.toggle.active > div > table > tbody > tr:nth-child(2) > td:nth-child(2)')
    bussiness_desgnation = conn.find_element_by_css_selector('.list-inline+ .toggle-transparent-body tr:nth-child(3) td+ td')
    buss_type = conn.find_element_by_css_selector('.list-inline+ .toggle-transparent-body tr~ tr+ tr td+ td')

    contact = conn.find_element_by_css_selector('.list-inline+ .toggle-transparent-body .toggle-transparent-body tr:nth-child(1) td+ td')
    ph_no = conn.find_element_by_css_selector('.list-inline+ .toggle-transparent-body tr:nth-child(2) td')
    email = conn.find_element_by_css_selector('.list-inline+ .toggle-transparent-body .toggle-transparent-body tr~ tr+ tr td+ td')
    streetAddress = conn.find_element_by_css_selector('.toggle-transparent-body .toggle-transparent-body tr:nth-child(1) td+ td')
    city = conn.find_element_by_css_selector('.toggle-transparent-body .toggle-transparent-body .toggle-transparent-body tr:nth-child(2) td+ td')
    state = conn.find_element_by_css_selector('.toggle-transparent-body .toggle-transparent-body .toggle-transparent-body tr~ tr+ tr td+ td')
    element_list.append([str(i),name.text,bussiness_profile.text,bussiness_cert.text,bussiness_desgnation.text,buss_type.text,contact.text,ph_no.text,email.text,streetAddress.text,city.text,state.text])

    time.sleep(1)
    





with xlsxwriter.Workbook('industry_dir(1100-2000).xlsx') as workbook:
    worksheet = workbook.add_worksheet()
  
    for row_num, data in enumerate(element_list):
        worksheet.write_row(row_num, 0, data)


conn.close()

