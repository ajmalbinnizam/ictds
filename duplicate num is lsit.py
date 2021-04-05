# duplicate num in list
num = [4,3,5,2,3]
for i in range(len(num)):
    for j in range(i+1, len(num)):
        if num[i] == num[j]:
            print(str(num[i]) +" is a duplicate num")
            break