list1 = [1,2,3,4,5,6,7,-1]
sliced_list = list1[0:4]
print(sliced_list)
print(list1[6])

threeDList = [[[1,2],[2,3],[4,5]]]
print(threeDList[0][0][1])
# append : adds element at the last position of the list

list1.append(8)
print(list1)
# pops last element from the list
list1.pop()
print(list1)

# extend : adds multiple elemnts at the end of the list

list1.extend([9,10,11])
print(list1)

# insert :adds element at the specific position of the list
list1.insert(2,12)
print(list1)

# editing using slicing

list1[1:4] = [13,14,15]
print(list1)


# removes element from the list

list1.remove(13)
print(list1)
# removing elements via slicing

list1[1:4] = []
print(list1)


for i in list1:
    print(i)

print("The length of list is : " + str(len(list1)))
print(min(list1))
print(max(list1))
print(sorted(list1))
print(sorted(list1,reverse=True))

print(list1.index(11))


