import pandas as pd
import glob
import os

fichiers_csv = glob.glob("*_amazon.csv")

print(f"Fichiers trouvés : {fichiers_csv}")

liste_df = []
for fichier in fichiers_csv:
    df = pd.read_csv(fichier)

    df['source_file'] = fichier 
    
    liste_df.append(df)

df_final = pd.concat(liste_df, ignore_index=True)

df_final.to_csv("tous_concurrents_amazon.csv", index=False, encoding='utf-8-sig')

print("Félicitations ! Le fichier 'tous_concurrents_amazon.csv' a été créé.")