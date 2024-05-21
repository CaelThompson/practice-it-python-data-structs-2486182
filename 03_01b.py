from collections import namedtuple
def order(driver, numPack):
    return driver.Car_capacity >= numPack
def main():
    #add code here
    #create a driver with a name, car type, and car capacity
    #an example you can use to practice: "Iris", "Toyota Prius", 7
    #check if they can take a certain order, given their car's capacity.
    driver = namedtuple("driver", ["name", "car", "Car_capacity"])
    Iris = driver("Iris", "Prius", 4)
    Mick = driver("Mick", "Camery", 4)
    Sam = driver("Sam", "F-150", 7)
    print(order(Sam,5))
    return

if __name__ == "__main__":
    main()