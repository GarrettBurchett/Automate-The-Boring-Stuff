# Automate the Boring Stuff - Chapter 5

def displayInventory(inventory:dict):
    print('Inventory:')
    item_total = 0
    for k, v in inventory.items():
        item_total += v
        print(f"{v} {k}")
    print("Total number of items: " + str(item_total))

def addtoInventory(inventory:dict, addedItems:list) -> dict:
    for item in addedItems:
        inventory[item] = inventory.get(item, 0) + 1

    return inventory

stuff = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}
displayInventory(stuff)
dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']
addtoInventory(stuff, dragonLoot)
displayInventory(stuff)