from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import pyfiglet
#logo
print(pyfiglet.figlet_format('whatsRobot',font='standard'))
print('created by mostafa mayahiyan')
#firefox driver
driver = webdriver.Firefox()
#search whatsapp web 
driver.get('https://web.whatsapp.com')
#take the name of contact from user 
name = input('which name do you want to send:')
#take massage
msg = input('insert your massage :')
#for sending massage 
count = int(input('how many time do you want to send:'))
#before start user should press some keys 
input('press any the buttom to Continue...')
user = driver.find_element(By.XPATH , '//span[@title = "{}"]'.format(name))
user.click()
massage_box = driver.find_element(By.XPATH , '/html/body/div[1]/div/div/div[4]/div/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[2]')
for i in range(count):
    massage_box.send_keys(msg)
    send = driver.find_element(By.XPATH , '/html/body/div[1]/div/div/div[4]/div/footer/div[1]/div/span[2]/div/div[2]/div[2]')
    send.click()
