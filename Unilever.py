import csv
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

BASE_URL = "https://www.amazon.fr/s?k=unilever&page={}"
NB_PAGES = 3



options = Options()
options.add_argument("--start-maximized")
options.add_argument("--disable-blink-features=AutomationControlled")

driver = webdriver.Chrome(options=options)

with open("unilever_amazon.csv", "w", newline="", encoding="utf-8") as fichier:

    writer = csv.writer(fichier)

    writer.writerow([
        "nom_produit",
        "prix",
        "categorie",
        "note"
    ])

    for page in range(1, NB_PAGES + 1):

        url = BASE_URL.format(page)

        print(f"Scraping Unilever - Page {page}...")

        driver.get(url)

        time.sleep(5)

        produits = driver.find_elements(
            By.CSS_SELECTOR,
            "div.s-result-item[data-component-type='s-search-result']"
        )

        for p in produits:

            try:

                try:
                    nom = p.find_element(By.CSS_SELECTOR, "h2 span").text
                except:
                    nom = "N/A"

                # PRIX
                try:
                    entier = p.find_element(By.CSS_SELECTOR, ".a-price-whole").text
                    centimes = p.find_element(By.CSS_SELECTOR, ".a-price-fraction").text

                    prix = f"{entier},{centimes}€"

                except:
                    prix = "N/A"

                categorie = "Consommation Courante"

                # NOTE
                try:
                    note_brute = p.find_element(
                        By.CSS_SELECTOR,
                        ".a-icon-alt"
                    ).get_attribute("innerHTML")
                    note = note_brute.split(" ")[0]

                except:
                    note = "N/A"

                # ÉCRITURE CSV
                writer.writerow([
                    nom,
                    prix,
                    categorie,
                    note
                ])

            except:
                continue

        time.sleep(2)

driver.quit()

print("Scraping terminé !")
print("Fichier créé : unilever_amazon.csv")