def pushZerosToEnd(array):

    n=len(array)
    

    temp=[0]*n

    
    j=0 #temparature এর Array এর মধ্যে Index এর সূচক ধরে রাখতে


    for i in range(n):
        if array[i] !=0:

            temp[j]=array[i]
            j+=1
    
    #temparature array থাকা বাকি স্থানগুলো ০ দিয়ে ভরাট করার জন্য।
    while  j < n : 
           temp[j]=0
           j +=1
    #temp[] এর সকল উপাদান array[] তে কপি করে বসাতে হবে।
    for i in range(n):
        array[i]=temp[i]

if __name__=="__main__":
    array=[1,2,0,4,3,0,5,0]
    pushZerosToEnd(array)
    
     
    for num in array:

      print(num,end="  ")



     
     
     
        
    