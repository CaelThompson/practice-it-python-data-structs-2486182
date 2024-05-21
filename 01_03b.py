from collections import Counter
def main():
    
    inventory = Counter(STA001=10, SAL002=20, ENT004=13)
    sales = Counter(STA001 = 5, SAL002 = 3, ENT004 = 3)
    inventory = inventory-sales
    #sell 5 starters, 3 salads, and 3 entrees
    #make 9 more starters and 1 more entree
    Shipment = {"STA001": 9, "ENT004":1}
    inventory.update(Shipment)
    print(inventory)

if __name__ == "__main__":
    main()