def binarySearch(dataSets, userInput):
    
    found = False
    index = 0
    operationCount = 0
    low = 0
    high = len(dataSets) - 1
    while low <= high:
        operationCount += 1
        middle = (low + high) // 2

        if userInput == dataSets[middle]:
            index = middle
            found = True
            break
        elif userInput < dataSets[middle]:
            high = middle - 1
        else:
            low = middle + 1
    return found, operationCount, index

def main():

    arr = [3, 1, 4, 2, 5, 6, 7, 9]
    arr.sort()
    userInput = int(input("Enter number: "))
    found, operationCount, index = binarySearch(arr, userInput)

    if found:
        print(f"Number found\nIndex: {index}")
        print(f"Number of iterations (steps): {operationCount}")
    else:
        print("Outcome: None")
        print(f"Number of iterations (steps): {operationCount}")

if __name__ == "__main__":
    main()