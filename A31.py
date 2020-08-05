
def binarySearch(arr, l, r, x): 
  
    while l <= r: 
  
        mid = l + (r - l)//2; 
          
        # Check if x is present at mid 
        if int(arr[mid]) == x: 
            return mid 
  
        # If x is greater, ignore left half 
        elif int(arr[mid]) < x: 
            l = mid + 1
  
        # If x is smaller, ignore right half 
        else: 
            r = mid - 1
      
    # If we reach here, then the element was not present 
    return -1
str1=input("Enter the numbers")
list1=list(str1)
list1.sort()
print ("The sorted order list1 of elements is",list1)
searchElement=int(input("Enter the element tosearch from the above list"))
res= binarySearch(list1 , 0 , len(list1)-1 , searchElement)

if res!=-1:
    print("Success")
else:
    print("Unsuccessful search")
