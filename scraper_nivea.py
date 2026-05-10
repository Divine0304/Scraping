import csv
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
BASE_URL = "https://www.amazon.fr/s?k=nivea&page={}"
NB_PAGES = 3
options = Options()

options.add_argument("--start-maximized")
options.add_argument("--disable-blink-features=AutomationControlled")
options.add_argument(
    "user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0 Safari/537.36"
)

driver = webdriver.Chrome(options=options)
with open("nivea_amazon.csv", "w", newline="", encoding="utf-8") as fichier:

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
        produits = driver.find_elements(
            By.CSS_SELECTOR,
            "div.s-result-item[data-component-type='s-search-result']"
        )

        print(f"Produits trouvés : {len(produits)}")
        for p in produits:

            try:

                nom = p.find_element(By.CSS_SELECTOR, "h2 span").text

                print(nom)
                try:
                    entier = p.find_element(By.CSS_SELECTOR, ".a-price-whole").text
                    centimes = p.find_element(By.CSS_SELECTOR, ".a-price-fraction").text

                    prix = f"{entier},{centimes}€"

                except:
                    prix = "N/A"

                print(prix)
                categorie = "Cosmétique et Beauté"

                print(categorie)
                try:

                    note_brute = p.find_element(
                        By.CSS_SELECTOR,
                        ".a-icon-alt"
                    ).get_attribute("innerHTML")

                    note = note_brute.split(" ")[0]

                except:
                    note = "N/A"

                print(note)

            except:
                continue