import csv
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

# --- CONFIGURATION ---
BASE_URL = "https://www.amazon.fr/s?k=loreal&page={}"
NB_PAGES = 3

options = Options()

options.add_argument("--start-maximized")
options.add_argument("--disable-blink-features=AutomationControlled")

options.add_argument(
    "user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0 Safari/537.36"
)

# Driver Chrome
driver = webdriver.Chrome(options=options)

# --- FICHIER CSV ---
with open("loreal_amazon.csv", "w", newline="", encoding="utf-8") as fichier:

    writer = csv.writer(fichier)

    # Colonnes identiques aux autres CSV
    writer.writerow([
        "nom_produit",
        "prix",
        "categorie",
        "note"
    ])

    # Boucle pages Amazon
    for page in range(1, NB_PAGES + 1):

        url = BASE_URL.format(page)

        print(f"Scraping L'Oréal - Page {page}...")

        driver.get(url)

        time.sleep(5)

        print(driver.title)

        produits = driver.find_elements(
            By.CSS_SELECTOR,
            "div.s-result-item[data-component-type='s-search-result']"
        )

        print(f"Produits trouvés : {len(produits)}")

        # Boucle produits
        for p in produits:

            try:

                # Nom produit
                nom = p.find_element(
                    By.CSS_SELECTOR,
                    "h2 span"
                ).text

                print(nom)

                # Prix
                try:

                    entier = p.find_element(
                        By.CSS_SELECTOR,
                        ".a-price-whole"
                    ).text

                    centimes = p.find_element(
                        By.CSS_SELECTOR,
                        ".a-price-fraction"
                    ).text

                    prix = f"{entier},{centimes}€"

                except:
                    prix = "N/A"

                print(prix)

                # Catégorie
                categorie = "Cosmétique et Beauté"

                print(categorie)

                # Note
                try:

                    note_brute = p.find_element(
                        By.CSS_SELECTOR,
                        ".a-icon-alt"
                    ).get_attribute("innerHTML")

                    note = note_brute.split(" ")[0]

                except:
                    note = "N/A"

                print(note)

                # Écriture CSV
                writer.writerow([
                    nom,
                    prix,
                    categorie,
                    note
                ])

            except:
                continue

# Fermeture navigateur
driver.quit()

print("Scraping L'Oréal terminé !")