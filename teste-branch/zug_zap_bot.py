# -*- coding: utf-8 -*-
from selenium import webdriver
import time

class whatsapp_bot:
    def __init__(self):
        self.message = ["Bom dia, seu fudido", "sera q e Isaias falando com vc? >:3"]
        self.grupe_people = ["Victor", "Emili", "Oi '-'"]
        options = webdriver.ChromeOptions()
        options.add_argument('lang=pt-br')
        self.driver = webdriver.Chrome(executable_path=r'./chromedriver.exe')

    def send_messages(self):
    	#<span dir="auto" title="Victor" class="_19RFN _1ovWX _F7Vk">Victor</span>
    	#<div tabindex="-1" class="_13mgZ">
    	#<span data-icon="send" class="">
    	x = 'Oi'
    	self.driver.get('https://web.whatsapp.com/')
    	time.sleep(15)
    	for j in range(1,20):
    		receiver = self.driver.find_element_by_xpath("//span[@title='Oi']")
    		time.sleep(2)
    		receiver.click()
    		if(j%2 == 0):
    			chat_box = self.driver.find_element_by_class_name('_13mgZ')
    			time.sleep(1)
    			chat_box.click()
    			chat_box.send_keys(self.message[0])
    			send_button = self.driver.find_element_by_xpath("//span[@data-icon='send']")
    			time.sleep(1)
    			send_button.click()
    		else:
    			chat_box = self.driver.find_element_by_class_name('_13mgZ')
    			time.sleep(1)
    			chat_box.click()
    			chat_box.send_keys(self.message[1])
    			send_button = self.driver.find_element_by_xpath("//span[@data-icon='send']")
    			time.sleep(1)
    			send_button.click()
    		time.sleep(3)

bot = whatsapp_bot()
bot.send_messages()
