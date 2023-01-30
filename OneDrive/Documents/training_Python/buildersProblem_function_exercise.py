#Implement a function that solves the following problem: 
# A construction company takes n days to build a dam with k workers. 
# Applying a rule of three, find how many days it takes for a company to build the damn with t workers

def builders(n,k,m):    # n=days project1  ;  k=workers project1  ; m=days project2  ;  t=workers project2
    t=(k-1)*(m/2)/n
    return t
print(builders(60,3,90))