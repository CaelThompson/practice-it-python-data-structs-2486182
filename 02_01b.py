from collections import deque
def main():
    food = deque(maxlen=5)
    food.append("STA001")
    orderFood = ["STA002", "SAL001", "DES004", "STA003"]
    food.extend(orderFood)
    print(food)
    return

if __name__ == "__main__":
    main()