import os

directory = "/Users/saraha/Desktop/BG3_Armory/website/images/elven_chain/male" #edited before each run
images = sorted(os.listdir(directory))
armor_piece = "elven_chain_M" #edited before each run

dye_dictionary = {
    "Standard": "_stan",
    "Baby Blue and Gold Dye": "_babyBlue",
    "Black and Azure Dye": "_blackAzure",
    "Black and Furnace Red Dye": "_blackFurnace",
    "Black and Jade Green Dye": "_blackJade",
    "Black and Summer Green Dye": "_blackSummer",
    "Bloody Plum Dye": "_plum",
    "Blue Dye": "_blue",
    "Boreal Blue Dye": "_boreal",
    "Brown Alabaster Dye": "_brown",
    "Cobalt Dye": "_cobalt",
    "Custard and Pink Rose Dye": "_custard",
    "Dark Amethyst Dye": "_darkA",
    "Deep Lilac Dye": "_lilac",
    "Drake General Dye": "_drake",
    "Faewild Green and Dun Dye": "_faewild",
    "Gorgeous Maroon Dye": "_maroon",
    "Green Dye": "_green",
    "Harlequin Black and White Dye": "_BW",
    "Indigo Dye": "_indigo",
    "Jet and Pink Rose Dye": "_jetPink",
    "Lavender Dye": "_lavender",
    "Light Blue Dye": "_lightBlue",
    "Lime, Lemon, and Lichen Dye": "_lime",
    "Lush Burgandy": "_burgandy",
    "Mellow Fruit Dye": "_mellow",
    "Muddy Red Dye": "_muddy",
    "Ocean Dye": "_ocean",
    "Orange Dye": "_orange",
    "Pale Green Dye": "_paleGreen",
    "Pale Orange Dye": "_paleOrange",
    "Pale Pink Dye": "_palePink",
    "Peach and Apricot Dye": "_peach",
    "Pink and Leaf Green Dye": "_pinkLeaf",
    "Purple Dye": "_purple",
    "Red Dye": "_red",
    "Sage Green Dye": "_sage",
    "Sea Green Dye": "_sea",
    "Sinful Red and Bone White": "_sinful",
    "Swamp Green Dye": "_swamp",
    "White and Scarlet Dye": "_whiteScar",
    "Yellow Dye": "_yellow",
}

dye_refs = list(dye_dictionary.values())

def new_names():
    if len(images) == len(dye_refs):
        for image, dye_ref in zip(images, dye_refs):
            orig_path = os.path.join(directory, image)
            extension = os.path.splitext(image)[1]
            new_name = f"{armor_piece}{dye_ref}{extension}"
            update_path = os.path.join(directory, new_name)
            os.rename(orig_path, update_path)
                    
    else:
        print("wrong number of pictures")