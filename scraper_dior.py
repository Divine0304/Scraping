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
with open("dior_amazon.csv", "w", newline="", encoding="utf-8") as fichier:

    writer = csv.writer(fichier)

    # Colonnes CSV
    writer.writerow([
        "nom_produit",
        "prix",
        "categorie",
        "note"
    ])
     # -----------------------------
    # BOUCLE PAGES
    # -----------------------------

    for page in range(1, NB_PAGES + 1):

        url = BASE_URL.format(page)

        print(f"Scraping Dior - Page {page}...")

        driver.get(url)

        time.sleep(5)

        # Tous les produits Amazon
        produits = driver.find_elements(
            By.CSS_SELECTOR,
            "div.s-result-item[data-component-type='s-search-result']"
        )