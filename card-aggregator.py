import csv
import os
from pathlib import Path
from collections import defaultdict

#"Card","Card","Token Id","Parallel","Rarity","Class","Owned","Wallet","Cached","Vault","Payload"
nameToCountDict = defaultdict(lambda: {
                            "Card": "",
                            "Token Id": "",
                            "Parallel": "",
                            "Rarity": "",
                            "Class": "",
                            "Owned": 0,
                            "Wallet": 0,
                            "Cached": 0,
                            "Payload": 0,
                            "Vault": 0
                        })

cardListDir = 'CardLists'
pathlist = Path(cardListDir).rglob('*.csv')

def main():
    # For each csv file to aggregate
    for path in pathlist:
        # Open the file and read in the card contents
        with open(str(path), newline='', encoding='utf-8') as cardfile:
            reader = csv.DictReader(cardfile)

            for row in reader:
                # Card Metadata
                nameToCountDict[row['Card']]['Card'] = row['Card']
                nameToCountDict[row['Card']]['Token Id'] = row['Token Id']
                nameToCountDict[row['Card']]['Parallel'] = row['Parallel']
                nameToCountDict[row['Card']]['Rarity'] = row['Rarity']
                nameToCountDict[row['Card']]['Class'] = row['Class']

                # Card Counts
                nameToCountDict[row['Card']]['Owned'] += int(row['Owned'])
                nameToCountDict[row['Card']]['Wallet'] += int(row['Wallet'])
                nameToCountDict[row['Card']]['Cached'] += int(row['Cached'])
                nameToCountDict[row['Card']]['Payload'] += int(row['Payload'])
                nameToCountDict[row['Card']]['Vault'] += int(row['Vault'])
    
    # Write aggregate card counts to file
    with open('AggregateCards.csv', 'w+', newline='', encoding='utf-8') as cardfile:
        fieldnames = list(nameToCountDict[list(nameToCountDict.keys())[0]].keys())
        print(fieldnames)
        writer = csv.DictWriter(cardfile, fieldnames=fieldnames)

        writer.writeheader()
        for card in nameToCountDict.values():
            writer.writerow(card)

main()
