def selectionSort(n):
  
  for i in range(len(n)):

    track = i
    for j in range(i + 1, len(n)):
      if n[track] > n[j]:
        track = j
    n[i], n[track] = n[track], n[i]


def main():

  n = [4, 7, 9, 1, 2, 6]
  print(f"Before: {n}")
  selectionSort(n)
  print(f"After: {n}")

if __name__=="__main__":
  main()

