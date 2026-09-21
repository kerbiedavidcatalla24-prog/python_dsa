def linearSearch(dataSets, userInput):
    found = False
    index = 0
    operationCount = 0
    for i in range(len(dataSets)):
        operationCount += 1
        if userInput == dataSets[i]:
            index = i
            found = True
            break
    return found, operationCount, index

def main():

    arr = [3, 1, 4, 2, 5, 6, 7, 9]
    userInput = int(input("Enter number: "))
    found, operationCount, index = linearSearch(arr, userInput)
    if found:
        print(f"Number found\nIndex: {index}")
        print(f"Number of iterations (steps): {operationCount}")
    else:
        print("Outcome: None")
        print(f"Number of iterations (steps): {operationCount}")
    
if __name__ == "__main__":
    main()