A = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
B = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

X = [f"{month}.{day}" for month, day in zip(A, B)]
print(X)