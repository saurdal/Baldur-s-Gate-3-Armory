let dye_dictionary = {
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
};

let image_names = {
  "Armour of Persistence": "armour_of_persistence",
  "Dark Justiciar Mail": "dark_justiciar_mail",
  "Elven Chain": "elven_chain"
};

let armor_name = document.body.getAttribute("data-armor_name");
let armor_path = image_names[armor_name];
let dye_dropdown = document.getElementById("dye_dropdown");
let armor_image_f = document.getElementById("armor_image_f");
let armor_image_m = document.getElementById("armor_image_m");

Object.keys(dye_dictionary).forEach(dye => {
  let option = document.createElement("option");
  option.value = dye_dictionary[dye];
  option.textContent = dye;
  dye_dropdown.appendChild(option);
});

function choose_dye() {
  let chosen_dye = dye_dropdown.value;
  let f_image = `images/${armor_path}/female/${armor_path}_F${chosen_dye}.png`;
  let m_image = `images/${armor_path}/male/${armor_path}_M${chosen_dye}.png`;
  armor_image_f.src = f_image;
  armor_image_m.src = m_image;
};

dye_dropdown.addEventListener("change", choose_dye);
