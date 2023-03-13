def binary_search(list,element):
    start=0
    mid=0
    end=len(list)
    steps=0


    while (start<=end):
        print("steps",steps, ":" ,str(list[start:end +1]))

        steps=steps+1
        mid = (start + end) // 2
        if element == list[mid]:
            return mid
        if element<list[mid]:
            end=mid-1
        else:
            start = mid +1

    return -1
if __name__=='__main__' :
    my_list=[1,2,3,4,5,6,7,8,9]
    binary_search(my_list,2 )

"""
Linear search
for i in list:
   if i ==12
   print("found")
"""



