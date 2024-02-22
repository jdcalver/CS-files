"""
Jackson Calvert
CS1210 C
2/21/24
"""

ELEMENTS = (None, "Hydrogen", "Helium", "Lithium", "Beryllium", "Boron",
            "Carbon", "Nitrogen", "Oxygen", "Fluorine", "Neon", "Sodium",
            "Magnesium", "Aluminum", "Silicon", "Phosphorus", "Sulfur",
            "Chlorine", "Argon", "Potassium", "Calcium", "Scandium",
            "Titanium", "Vanadium", "Chromium", "Manganese", "Iron", "Cobalt",
            "Nickel", "Copper", "Zinc", "Gallium", "Germanium", "Arsenic",
            "Selenium", "Bromine", "Krypton", "Rubidium", "Strontium",
            "Yttrium", "Zirconium", "Niobium", "Molybdenum", "Technetium",
            "Ruthenium", "Rhodium", "Palladium", "Silver", "Cadmium", "Indium",
            "Tin", "Antimony", "Tellurium", "Iodine", "Xenon", "Cesium",
            "Barium", "Lanthanum", "Cerium", "Praseodymium", "Neodymium",
            "Promethium", "Samarium", "Europium", "Gadolinium", "Terbium",
            "Dysprosium", "Holmium", "Erbium", "Thulium", "Ytterbium",
            "Lutetium", "Hafnium", "Tantalum", "Tungsten", "Rhenium", "Osmium",
            "Iridium", "Platinum", "Gold", "Mercury", "Thallium", "Lead",
            "Bismuth", "Polonium", "Astatine", "Radon", "Francium", "Radium",
            "Actinium", "Thorium", "Protactinium", "Uranium", "Neptunium",
            "Plutonium", "Americium", "Curium", "Berkelium", "Californium",
            "Einsteinium", "Fermium", "Mendelevium", "Nobelium", "Lawrencium",
            "Rutherfordium", "Dubnium", "Seaborgium", "Bohrium", "Hassium",
            "Meitnerium", "Darmstadtium", "Roentgenium", "Copernicium",
            "Nihonium", "Flerovium", "Moscovium", "Livermorium", "Tennessine",
            "Oganesson")

if __name__ == '__main__':
    prompt = input('Do you wish to look up by element name or by atomic number? '
                   'e/n: ')
    if prompt.lower() == 'e':
        name = input('Enter the name of the element: ').capitalize()
        if name in ELEMENTS:
            print(f'The atomic number of {name} is '
                  f'{ELEMENTS.index(name)}.')
        else:
            print(f'Error. Dummy! Did you mispell it? {name.capitalize()} '
                  'doesn\'t exist!')
    elif prompt.lower() == 'n':
        number = int(input('Enter the atomic number of the element: '))
        if 0 < number <= len(ELEMENTS)-1:
            print(f'The element with atomic number {number} is '
                  f'{ELEMENTS[number]}')
        else:
            print('Invalid atomic number, try again... dummy')
    else:
        print('Invalid input... dummy')
    