list1 = [1,2,3,4,5,6,7,8,9,10]
list2 = [1,2,3,4,5,6,7,8,9,10]

for value in list1:
    for int in list2:
        print(f"{value} X {int} = {value * int}")
    print("")