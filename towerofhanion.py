def TowerOfHanoi(n,source,destination,auxiliary):
    if n==1:
        print("move disk 1 form source",source,"to destination",destination)
        return
    TowerOfHanoi(n-1,source,auxiliary,destination)
    print("move disk",n,"from source",source,"to destination",destination)
    TowerOfHanoi(n-1,auxiliary,destination,source)
n = 4
TowerOfHanoi(n,'A','B','C')

##list
print("\nList")
list=[12,23,86,98,77,45,84]
print(sum(list))
