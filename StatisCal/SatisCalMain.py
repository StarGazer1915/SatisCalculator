import json

# -------------------- FUNCTIONS -------------------- #
def loadRecipes():
    """
    Loads the .json file containing the items of Satisfactory.
    @return: dict
    """
    with open("DataFiles/Resources.json") as file:
        return json.load(file)


def getItemsRequired(data, givenItem):
    """
    Takes the required items to craft the given item from the data and returns them.
    @param data: dict
    @param category: string
    @param givenItem: string
    @return: list
    """
    list = []
    for category in data:
        for item in data[f"{category}"]:
            if item["name"].lower() == givenItem.lower():
                found = True
                for resource in item["crafting"]:
                    list.append([resource, item["crafting"][f"{resource}"], item["machine"]])

    if found == True:
        return list
    else:
        return False


def displayHandCraftingItems(givenItem, list):
    print(f"\n|----------------========----------------|"
          f"\nREQUESTED ITEM: '{givenItem}'\n"
          f"\nRequired for crafting:")

    for item in list:
        print(f"- {item[0]}")
    print("|----------------------------------------|")


def StartCalculator(recipeData):
    print("\n|| Welcome to the Satisfactory Crafting Companion [SCC] ||")

    item = ""
    while item.lower() != "stop":
        item = str(input("\nEnter desired item: "))
        try:
            craftitems = getItemsRequired(recipeData, item.lower())
        except:
            print("Item could not be found in FICSIT Databank.\nPlease try again.")
            continue

        if craftitems != False:
            displayHandCraftingItems(item, craftitems)


# -------------------- EXECUTION -------------------- #
data = loadRecipes()
StartCalculator(data)