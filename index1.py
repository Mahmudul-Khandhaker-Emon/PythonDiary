def getSecondlargest(arr):
     
    n=len(arr)

    largest=-1
    Secondlargest=-1

    for i in range(n):

        if arr[i]>largest:
            largest=arr[i]

    for i in range(n):

        if arr[i] >Secondlargest and arr[i] != largest:

            Secondlargest=arr[i]
    return Secondlargest


if __name__ == "__main__":
    arr = [12, 35, 1, 10, 34, 1]
    print(getSecondlargest(arr))