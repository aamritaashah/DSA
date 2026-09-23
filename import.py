# Import array module
import array


# 1. Create an integer array
a = array.array('i', [10, 20, 30, 40, 50])

print("1. Original Array:", a)


# 2. Append
print("\n2. Append")
a.append(60)
print("After append:", a)


# 3. Insert
print("\n3. Insert")
a.insert(2, 25)
print("After insert:", a)


# 4. Remove
print("\n4. Remove")
a.remove(30)
print("After remove:", a)


# 5. Pop
print("\n5. Pop")
a.pop()
print("After pop:", a)


# 6. Count
print("\n6. Count")
a.append(20)
print("Array:", a)
print("Count of 20:", a.count(20))


# 7. Extend
print("\n7. Extend")
b = array.array('i', [70, 80, 90])
a.extend(b)
print("After extend:", a)


# 8. Fromlist
print("\n8. Fromlist")
c = array.array('i', [1, 2, 3])
c.fromlist([4, 5, 6])
print("After fromlist:", c)


# 9. Frombytes
print("\n9. Frombytes")
d = array.array('i')
d.frombytes(bytes([1, 0, 0, 0, 2, 0, 0, 0]))
print("After frombytes:", d)


# 10. Index
print("\n10. Index")
print("Index of 20:", a.index(20))


# 11. Reverse
print("\n11. Reverse")
a.reverse()
print("After reverse:", a)


# 12. ToList
print("\n12. ToList")
my_list = a.tolist()
print("Array:", a)
print("List:", my_list)


# 13. ToString
print("\n13. ToString")
s = str(a.tolist())
print("Array:", a)
print("String:", s)
print("Type:", type(s))
