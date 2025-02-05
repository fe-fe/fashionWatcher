from selenium.common.exceptions import NoSuchElementException
from selenium import webdriver
import time
from selenium.webdriver.common.by import By


def enjoei(link: str, browser: webdriver.Chrome, new: bool) -> str:
    browser.get(link)
    price = False

    while not price:
        try: 
            price = browser.find_element(By.CSS_SELECTOR, 'span[data-test="label-preco-desconto"]').text
        except NoSuchElementException:
            try:
                price = browser.find_element(By.CSS_SELECTOR, 'span[data-test="div-preco-produto"]').text
            except NoSuchElementException:
                time.sleep(0.5)

    img = ""
    if new:
        while img == "":
            try:
                img = browser.find_element(By.CSS_SELECTOR, 'img[fetchpriority="high"]').get_attribute("src")
            except NoSuchElementException:
                time.sleep(0.5)

    return price[3:], img