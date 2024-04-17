import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.common.keys import Keys

URL_FORM = 'https://forms.gle/1mq3co2LvmtDnmAu9'
URL_ZILLOW = 'https://appbrewery.github.io/Zillow-Clone/'

respons = requests.get(URL_ZILLOW).text

soup = BeautifulSoup(respons, 'html.parser')

################################# Create list of prices #########################################
price_list = soup.find_all(name='span', class_='PropertyCardWrapper__StyledPriceLine')
new_list_price = []
for price in price_list:
    new_list_price.append(price.text.split('/')[0].split('+')[0])

print(new_list_price)
################################# Create list of links#########################################
href_list = soup.find_all(name="a", class_='property-card-link')
list_of_links = []
for link in href_list:
    list_of_links.append(link.get("href"))

print(list_of_links)
################################# Create list of adress #########################################
adress_list = soup.find_all(name='address')
list_of_adress = []
for adress in adress_list:
    list_of_adress.append(adress.text.strip())

print(list_of_adress)

print(len(list_of_adress), len(list_of_links), len(new_list_price))

######################################### SELENIUM ##############################################3

chrome_option = webdriver.ChromeOptions()
chrome_option.add_experimental_option('detach', True)





len_time = 0
while len_time < len(list_of_adress):
    driver = webdriver.Chrome(options=chrome_option)
    driver.get(URL_FORM)
    time.sleep(6)
    answer1 = driver.find_element(By.XPATH, value= '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')
    answer1.send_keys(list_of_adress[len_time])

    answer2 = driver.find_element(By.XPATH, value= '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')
    answer2.send_keys(new_list_price[len_time])

    answer3 = driver.find_element(By.XPATH, value= '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input')
    answer3.send_keys(list_of_links[len_time])

    klik_send = driver.find_element(By.XPATH, value='//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div').click()

    driver.close()
    len_time += 1