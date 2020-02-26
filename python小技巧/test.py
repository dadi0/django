list1 = [4, -3, 1, 3, -9, 23, 34, 0, -2]
list1.sort(key=lambda x: (x < 0, abs(x)))
print(list1)
print(2 < 3)