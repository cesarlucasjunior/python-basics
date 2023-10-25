# functions

def myFunc(n,m):
    return n*m

print(myFunc(3,3))

# Nested functions have access to outer variables

def outer(a,b):
    c = 'c'

    def inner():
        return a + b + c
    
    return inner()

print(outer('a','b'))

# Can modify objects but not reassign unless usign nonlocal keyword

def double(arr, val): 
    def helper():
        #Modifyung arrays works
        for i, n in enumerate(arr):
            arr[i] *= 2
        
        # will only modify val in the helper scope
        # val *= 2

        # this will modify val outside helper scope
        nonlocal val 
        val *= 2
    helper()
    print(arr, val)

double([1,2], 3)