A = [23, 25, 34, 45, 56, 67, 78, 89, 90, 12]

largest = A[0]
second = A[0]

for i in range(1, len(A)):
    if A[i] > largest:
        second = largest
        largest = A[i]
    elif A[i] > second and A[i] < largest:
        second = A[i]

print("Largest:", largest)
print("Second Largest:", second)
