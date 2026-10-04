def sortArr(arr):
    for i in range(len(arr)):
        for j in range(len(arr) - 1 - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

def main():

    arr = [4, 5, 1, 6, 7, 9, 8, 10]
    sortArr(arr)
    print(arr)

if __name__=="__main__":
    main()

