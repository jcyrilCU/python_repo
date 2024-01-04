class RestaurantMenu:
    def __init__(self, x, y):
        self.itemName = x
        self.itemPrice = y

class MenuList:
    Menu = []
    def addItem(self,x):
        self.Menu.append(x)
   
    def displayMenu(self):
        count = 0
        print("Restaurant Menu:")
        for item in self.Menu:
            count += 1
            print(count,".",item.itemName,":", item.itemPrice)            

appendItem = MenuList()
while(True):
    itemName = input("Enter the name of the item: ")
    itemPrice = input("Enter the price of the item: ")
    item = RestaurantMenu(itemName, itemPrice)
    appendItem.addItem(item)
    repeatVal = input("Add another item?[y/n]").lower()
    if repeatVal != 'y':
        appendItem.displayMenu()
        break

