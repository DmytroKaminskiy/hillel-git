











a = 1
b = a

print(id(a) == id(b))

# lst = [1, 2]
# lst2 = [1, 2]
# lst2 = lst
# lst2.append(3)
# print(lst)

# print(lst[0] == lst2[0])
# print(lst[0] is lst2[0])


t = (1, 2, [3, 4])

t[-1].append(5)
t[-1] = [3, 4, 5]
print(t)
