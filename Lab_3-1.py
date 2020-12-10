
def sum_to(n):
    total = 0
    iteration = 1 
    while iteration < n+1:
        total += iteration 
        iteration += 1
    return total


num = input("Please input an intager: ")

result = sum_to(int(num))
print(result)


