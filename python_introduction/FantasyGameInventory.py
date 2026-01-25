inventory = {
    'rope': 1,
    'torch': 6,
    'gold coin': 42,
    'dagger': 1,
    'arrow': 12
}
def displayInventory(inventory):
    print("Inventory:")
    total_items = 0

    for item, count in inventory.items():
        print(f"{count} {item}")
        total_items += count

    print("Total number of items:", total_items)

displayInventory(inventory)