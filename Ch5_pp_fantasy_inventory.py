import pprint
# Part 1 - Count Inventory
fullInventory = {'arrow': 12, 'gold coin': 42, 'rope': 1,'torch': 6, 'dagger':1}

# Part 2 - Dragon's loot
inv = {'gold coin': 42, 'rope': 1}
dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']

def displayInventory(inventory):
	print("Inventory:")
	item_total = 0
	for k,v in inventory.items():  # k - key, v - values
		print(str(v) + '\t' + k)
		item_total = item_total + v
	print("Total number of items: " + str(item_total))
	
def addToInventory(inventory, addedItems):
	for i in range(len(addedItems)):
		inventory.setdefault(addedItems[i],0)		# if "added items" aren't in "inventory" - add and set count to 0
		inventory[addedItems[i]] = inventory[addedItems[i]] + 1		# add added items to dictionary
	print("addToInventory Output: ")
	pprint.pprint(inventory)
	return inventory
'''

# For Part 1	
# displayInventory(fullInventory)
'''
# For Part 2
displayInventory(addToInventory(inv, dragonLoot))
