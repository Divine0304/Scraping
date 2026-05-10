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
           # -----------------------------
        # BOUCLE PRODUITS
        # -----------------------------

        for p in produits:

            try:

                # NOM PRODUIT
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

                # CATÉGORIE
                categorie = "Cosmétique et Beauté"

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

# -----------------------------
# FIN
# -----------------------------

driver.quit()

print("Scraping terminé !")
print("Fichier créé : dior_amazon.csv")