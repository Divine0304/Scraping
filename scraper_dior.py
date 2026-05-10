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