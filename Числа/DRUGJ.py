
for X in range(10000):
    S = sum(I for i in range(1, X) if X % I == 0)
    if S > X and sum(I for I in range(1, S) if S % I == 0) == X:
        print(X, S)
