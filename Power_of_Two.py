def is_power_of_two(n):
    if n <= 0:
        return False
    return (n & (n - 1)) == 0

num = int(input("Enter an integer: "))
print(is_power_of_two(num))
