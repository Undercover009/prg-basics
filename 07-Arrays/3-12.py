arr1=[4,36,12,28,9,44,5]
arr2=[5,1,36]

for item in arr1:
    if not (item in arr2):
        print(item, end=', ')