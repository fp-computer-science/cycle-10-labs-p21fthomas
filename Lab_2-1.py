def sum_to(value):
    total = 0 
    for x in range(int(value) + 1):
        total += x 
    return total 


num = input("Enter an Integer: ")
print(sum_to(num))

