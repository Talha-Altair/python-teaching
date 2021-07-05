my_list = [1,6,19,20,65,180,250,760]

target = 6

def binary_search(array,x):
    
    low = 0
    high = len(array) - 1

    while low <= high:

        mid = (low + high ) // 2
        
        if array[mid] < x:
            low = mid + 1
        elif array[mid] > x:
            high = mid - 1
        else:
            return mid

    return "Element not found"

result = binary_search(my_list,target)

print(result)

