A = [1, 2, 2, 1, 3, 4, 3]

for i in range(len(A)):
    for j in range(i, len(A)):
        if A[i] == A[j]:
            A.remove(A[i])
            A.remove(A[i])
    else:
        print(A[i])