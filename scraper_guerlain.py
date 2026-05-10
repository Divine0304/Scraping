import csv
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
BASE_URL = "https://www.amazon.fr/s?k=guerlain&page={}"

NB_PAGES = 3
options = Options()

options.add_argument("--start-maximized")

options.add_argument("--disable-blink-features=AutomationControlled")

options.add_argument(
    "user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0 Safari/537.36"
)

driver = webdriver.Chrome(options=options)
with open("guerlain_amazon.csv", "w", newline="", encoding="utf-8") as fichier:

    writer = csv.writer(fichier)

    writer.writerow([
        "nom_produit",
        "prix",
        "categorie",
        "note"
    ])
    for page in range(1, NB_PAGES + 1):

        url = BASE_URL.format(page)

        print(f"Scraping page {page}...")

        driver.get(url)

        time.sleep(5)

        print(driver.title)