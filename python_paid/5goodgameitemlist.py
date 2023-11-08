stuff={'rope':1,'torch':6,'gold coin':42,'dagger':1,'arrow':12}

def displayInventory(inventory):
    print('Inventory:')
    total=0
    for k,v in inventory.items():
        print(str(v)+' '+k)
        total=total+v
    print('Total number of items:'+str(total))
displayInventory(stuff)
print()

def addToInventory(inventory,addedItems):
    print('-背包更新中-')
    c1={}
    for something in addedItems:
        c1.setdefault(something,0)
        c1[something]+=1 
    for v in inventory.keys():
        if v not in c1.keys():
            c1.setdefault(v,0)
            c1[v]+=inventory[v]
    for k in c1.keys():
        if k in inventory:
            c1[k]+=c1[k]+inventory[k]
    return c1

def displayInventory(inv):
    for k,v in inv.items():
        print(str(v)+':'+k)

inv={'gold coin':42,'rope':1}
dragonLoot=['gold coin','dagger','gold coin','ruby']
print('背包物品：')
displayInventory(inv)
print('BOSS掉落物品：')
print(dragonLoot)
inv=addToInventory(inv,dragonLoot)
print('背包物品：')
displayInventory(inv)