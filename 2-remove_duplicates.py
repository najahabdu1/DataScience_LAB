list1 = []
n = int(input("Enter number of elements : "))
print("Enter the numbers")
for i in range(0, n):
    element = int(input())
    list1.append(element)
print(list1)
print (set(list1))