import numpy as np
##Q1
##list1=input("Enter a List")
list1=[[1,'a',['cat'],2],[[[3]],'dog'],4,5]
list1=np.array(list1)
x=np.ndarray.flatten(list1)
print(x)



##Q2
##list2=input("Enter a List")
list2=[[1, 2], [3, 4], [5, 6, 7]]

list2.reverse()
for i in list2:
    if type(i) == list:
        i=i.reverse()

print(list2)
