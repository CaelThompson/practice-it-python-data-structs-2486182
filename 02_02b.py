from collections import deque
def checkPal(word):
    d = deque(word)
    while len(d) > 1:
        if d.pop() != d.popleft():
            return False
    return True
def main():
    word = "choice"
    print(checkPal(word))
    word = "tacocat"
    print(checkPal(word))
    return

if __name__ == "__main__":
    main()