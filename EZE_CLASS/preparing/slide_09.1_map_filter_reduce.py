# Filter takes a step further than maps and performs a general operation on members then also filters 
# The final values that meet a particular criteria
# Write a program that filters out the even numbers greater than 10.
def even(x):
    if x > 10:
        if x % 2 == 0:
            return x
nums = [7,8,9,10,11,12,13,14,15,16,17,18,19,20,7,77,65]

answer = list(filter(even,nums))
print(answer)