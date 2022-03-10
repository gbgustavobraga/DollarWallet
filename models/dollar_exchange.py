from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import pandas as pd


def dollar_exchange():
    nav = webdriver.Chrome()
    nav.get("https://www.google.com.br/")

    nav.find_element(By.XPATH,
                     '/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input').send_keys("Cotação Dólar")
    nav.find_element(By.XPATH,
                     '/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input').send_keys(Keys.ENTER)

    price_doll = nav.find_element(
        By.XPATH, '//*[@id="knowledge-currency__updatable-data-column"]/div[1]/div[2]/span[1]').get_attribute('data-value')

    nav.quit()
    return float(price_doll)


