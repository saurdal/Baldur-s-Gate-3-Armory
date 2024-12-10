import sqlite3

conn = sqlite3.connect("BG3_Armory.db")
cursor = conn.cursor()

#armor pieces
armor_pieces = [("Armour of Persistence",), ("Dark Justiciar Half-Plate",), ("Armour of Moonbasking",)]

cursor.executemany("INSERT INTO Armor (armor_title) VALUES (?)", armor_pieces)

#dyes
dyes = [("Standard", "_stan",), ("Cobalt Dye", "_cobalt",), ("Black and Azure Dye", "_blackAzure",), ("Black and Summer Green Dye", "_blackSummer",), ("Jet and Pink Rose Dye", "_jetPink",),
("Black and Furnace Red Dye", "_blackFurnace",), ("Black and Jade Green Dye", "_blackJade",), ("Light Blue Dye", "_lightBlue",), ("Sea Green Dye", "_sea",),
("Lavender Dye", "_lavender",), ("Blue Dye", "_blue",), ("Baby Blue and Gold Dye", "_babyBlue",), ("Yellow Dye", "_yellow",), ("Green Dye", "_green",),
("Faewild Green and Dun Dye", "_faewild",), ("Swamp Green Dye", "_swamp",), ("Sage Green Dye", "_sage",),
("Pink and Leaf Green Dye", "_pinkLeaf",), ("Custard and Pink Rose Dye", "_custard",), ("Peach and Apricot Dye", "_peach",), ("Mellow Fruit Dye", "_mellow",),
("Lime, Lemon, and Lichen Dye", "_lime",), ("Gorgeous Maroon Dye", "_maroon",), ("Ocean Dye", "_ocean",), ("Orange Dye", "_orange",), ("Pale Orange Dye", "_paleOrange",),
("Pale Pink Dye", "_palePink",), ("Dark Amethyst Dye", "_darkA",), ("Purple Dye", "_purple",), ("Indigo Dye", "_indigo",), ("Deep Lilac Dye", "_lilac",),
("Bloody Plum Dye", "_plum",), ("Red Dye", "_red",), ("Muddy Red Dye", "_muddy",), ("White and Scarlet Dye", "_whiteScar",), ("Lush Burgandy", "_burgandy",),
("Boreal Blue Dye", "_boreal",), ("Pale Green Dye", "_paleGreen",), ("Harlequin Black and White Dye", "_BW",), ("Brown Alabaster Dye", "_brown",),
("Sinful Red and Bone White", "_sinful",), ("Drake General Dye", "_drake",),]

cursor.executemany("INSERT INTO Dyes (dye_name, dye_ref) VALUES (?)", dyes)

conn.commit()
conn.close()