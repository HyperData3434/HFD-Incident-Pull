import simpleaudio as sa
import pyaudio as pa
import json
import threading
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# Set up webdriver
chrome_options = Options()
driver = webdriver.Chrome(options=chrome_options)

def listen():
    driver.get("https://www.broadcastify.com/webPlayer/28416")
    play = driver.find_element(By.CLASS_NAME, "playStop-28416")
    play.click
    time.sleep(30)
    