import csv
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
# -----------------------------
# CONFIGURATION
# -----------------------------

BASE_URL = "https://www.amazon.fr/s?k=dior+beaute&page={}"
NB_PAGES = 3

# -----------------------------
# SELENIUM
# -----------------------------
options = Options()
options.add_argument("--start-maximized")
options.add_argument("--disable-blink-features=AutomationControlled")

driver = webdriver.Chrome(options=options)

# -----------------------------
# CRÉATION CSV
# -----------------------------