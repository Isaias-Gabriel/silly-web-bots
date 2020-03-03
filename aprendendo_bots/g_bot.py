# -*- coding: utf-8 -*-
from selenium import webdriver
import time

class bot:
    def __init__(self):
        options = webdriver.ChromeOptions()
        options.add_argument('lang=pt-br')
        self.driver = webdriver.Chrome(executable_path=r'./chromedriver.exe')
        self.procurar = "DUDA BEAT Bixinho"

    def malinar(self):
        #<div id="container" class="style-scope ytd-searchbox">
        #<button id="search-icon-legacy" class="style-scope ytd-searchbox" aria-label="Pesquisar">
        #<yt-formatted-string class="style-scope ytd-video-renderer" aria-label="DUDA BEAT - Bixinho (Lux &amp; Tróia Remix) [Clipe Oficial] Duda Beat há 11 meses 3 minutos e 33 segundos 7.505.164 visualizações">
        #<img id="img" class="style-scope yt-img-shadow" alt="" width="246" src="https://i.ytimg.com/vi/UFj_yrzzenc/hqdefault.jpg?sqp=-oaymwEZCNACELwBSFXyq4qpAwsIARUAAIhCGAFwAQ==&amp;rs=AOn4CLBtW9yEkwaMHsdnguIX3bgGRziu-Q">
        
        # self.driver.get('https://www.youtube.com')
        # time.sleep(5)
        # procurar = self.driver.find_element_by_xpath("//input[@id='search']")
        # time.sleep(1)
        # procurar.click()
        # procurar.send_keys(self.procurar)
        # time.sleep(2)
        # clicar = self.driver.find_element_by_xpath("//button[@id='search-icon-legacy']")
        # time.sleep(0.5)
        # clicar.click()
        # clicar = self.driver.find_element_by_xpath('//a[@href="/watch?v=UFj_yrzzenc"]')
        # time.sleep(2)
        # clicar.click()

        self.driver.get('https://www.google.com/')
        time.sleep(5)
        procurar = self.driver.find_element_by_xpath("//input[@name='q']")
        time.sleep(1)
        procurar.click()
        procurar.send_keys('isaac')
        time.sleep(1)
        clicar = self.driver.find_element_by_xpath("//input[@value='Pesquisa Google']")
        time.sleep(1)
        clicar.click()
        clicar = self.driver.find_element_by_xpath("//h3[1]")
        time.sleep(2)
        clicar.click()



bot = bot()
bot.malinar()