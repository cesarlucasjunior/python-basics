# we have to use parentheses in a multi line conditional statement:

n,m = 1,2

if ((n > 2 and 
     n != m) or n==m):
    n+=1

# notice that we use the logic operators: (and | &&) (or | ||)