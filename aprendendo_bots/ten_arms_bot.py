# -*- coding: utf-8 -*-
from selenium import webdriver
import time
import random

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

        n = 0
        tempo_video = 100
        self.driver.get('https://www.youtube.com/?gl=US')
        time.sleep(1)
        self.driver.get('https://youtu.be/rfwPPzL05-U')
        time.sleep(3)
        procurar = self.driver.find_element_by_xpath("//html[1]")
        time.sleep(0.5)
        procurar.send_keys("0")
        tempo_espera = tempo_video
        time.sleep(tempo_espera)
        while(n < 3):
            time.sleep(0.5)
            x = random.randint(1,9)
            x = str(x)
            procurar.send_keys(x)
            tempo_espera = tempo_video - 10 * int(x)
            time.sleep(tempo_espera)
            n += 1

        
        # procurar = self.driver.find_element_by_xpath("//a[@id='gb_70']")
        # time.sleep(1)
        # procurar.click()
        # procurar = self.driver.find_element_by_xpath("//input[@id='identifierId']")
        # time.sleep(1)
        # procurar.click()
        # procurar.send_keys("hahahahakkj")
        # time.sleep(1)
        # clique = self.driver.find_element_by_claas_name("RveJvd snByac")
        # time.sleep(0.5)
        # clique.click()
        # procurar = self.driver.find_element_by_claas_name("whsOnd zHQkBf")
        # time.sleep(0.5)
        # clique.send_keys("pqeuamotantoserrei")
        # time.sleep(0.5)
        # clique = self.driver.find_element_by_claas_name("RveJvd snByac")
        # time.sleep(0.5)
        # clique.click()



bot = bot()
bot.malinar()  