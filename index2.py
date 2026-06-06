def getSecondLargest(arr):

    n=len(arr)

    largest=-1
    SecondLargest=-1

    for i in range(n):

        if  arr[i]>largest:

            SecondLargest= largest
            largest= arr[i]

        
        elif arr[i]<largest and arr[i]>SecondLargest:

            SecondLargest=arr[i]
    return SecondLargest

if __name__=="__main__":

    arr=[12, 35, 1, 10, 34, 1]
    print(getSecondLargest(arr))



###Time Complexity: O(n)=>O(1) because travarsing this array at only Once and This method is very efficient.