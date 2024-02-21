list1 = ["a", "b", "c"]
list2 = [1, 2, 3]
dic = {}
for i in range(len(list1)):
    dic[list1[i]] = list2[i]
print(dic)