# ALL SORTING ALGORITHMS IN THE COMPUTER SCIENCE COURSE

def get_arr():
    return [7,1,89,23,24,21,5,0,-1,-55,44]

def is_ordered(array):
    return [-55, -1, 0, 1, 5, 7, 21, 23, 24, 44, 89]  == array

print("- INITIAL VECTOR WITHOUT ORDER ", get_arr(), " - ")    

#  BUBBLE SORT
def bubble_sort(array):
    
    for x in range(0,len(array)):
        
        for y in range(0,len(array)-1):
            
            if array[x]<array[y]:
                aux = array[x]
                array[x] = array[y]
                array[y] = aux
            
    print(f"| Ordered: {is_ordered(array)}|")
    
    return array

print("\n - BUBBLE SORT \n SPECIFICATIONS: \n Average runtime: O(n^2) - \n ",bubble_sort(get_arr()), "\n")

# INSERTION SORT
def insertion_sort(array):
    
    for x in range(0, len(array)):
        
        j = x-1
        KEY = array[x]
        
        while KEY<array[j] and j >= 0:
            aux = KEY
            array[j+1] = array[j]
            array[j] = aux
            j -= 1
            
    print(f"\n | Ordered: {is_ordered(array)}|")
    return array

print("\n - INSERTION SORT \n SPECIFICATIONS: \n Average runtime: O(n^2) - \n ",insertion_sort(get_arr()), "\n")

# SELECTION SORT
def selection_sort(array):
    
    for x in range(0, len(array)):
        
        min_value = 999
        pos = 0
        for y in range(x, len(array)):
            if array[y] < min_value:
                min_value = array[y]
                pos = y

        if array[x] > min_value:
            aux = array[x]
            array[x] = array[pos]
            array[pos] = aux
            
    return array

print("\n - SELECTION SORT \n SPECIFICATIONS: \n Average runtime: O(n^2) - \n ",selection_sort(get_arr()), "\n")

#####################################################
#               DIVIDE AND CONQUEROR                #
#####################################################

# QUICK SORT

def quick_sort(array, low, high):
    if low < high:
        
        PartitionIndex = partition(array, low, high)
        
        quick_sort(array, low, PartitionIndex-1)
        quick_sort(array, PartitionIndex+1, high)

    return array
    
def partition (arr, low, high):
    i = (low-1)
    pivot = arr[high]

    for j in range (low, high):
        if arr[j] < pivot:
            i = i+1
            arr[i], arr[j] = arr[j],arr[i]
            
    arr[i+1], arr[high] = arr[high], arr[i+1]
    return (i+1)

print("\n - QUICK SORT \n SPECIFICATIONS: \n Average runtime: O(n.log(n)) - \n ",quick_sort(get_arr(),0 ,len(get_arr())-1), "\n")

# MERGE SORT
    
def merge_sort(arr):
    # caso base
    if len(arr) > 1:
        # partimos el array en 2
        middle = len(arr)//2
        # creamos lado izquierdo y derecho
        partitionLeft = arr[:middle]
        partitionRight = arr[middle:]
        
        # recursividad, volvemos a hacer hasta que queden los numeros solos
        merge_sort(partitionLeft)
        merge_sort(partitionRight)
        # incializamos contadores en 0 los 3
        i = j = k = 0
        # reocrremos partitionLeft y partitionRight con sus respectivos punteros
        # cuando se cumple la condicion aumentamos el puntero de un lado o de otro
        while i < len(partitionLeft) and j < len(partitionRight):
            if partitionLeft[i] < partitionRight[j]:
                arr[k] = partitionLeft[i]
                i+=1
            else:
                arr[k] = partitionRight[j]
                j+=1    
            # siempre aumentamos k+1 ya que va ir poniendolos en el array general
            k+=1
        
        # para que no quede ningun elemento fuera comprobamos
        # esto no es necesario si se ejecuta bien
        while i < len(partitionLeft):
            arr[k] = partitionLeft[i]
            i+=1
            k+=1
            
        while j < len(partitionRight):
            arr[k] = partitionRight[j]
            j+=1
            k+=1
    return arr    

print("\n - MERGE SORT \n SPECIFICATIONS: \n Average runtime: O(n.log(n)) - \n ",merge_sort(get_arr()), "\n")

    
