def reverse_integer(num):
    is_negative = False
    if num < 0:
        is_negative = True
        num = abs(num)
    
    reversed_num = 0
    while num > 0:
        remainder = num % 10
        reversed_num = (reversed_num * 10) + remainder
        num //= 10
    
    if is_negative:
        reversed_num = -reversed_num
    
    return reversed_num

input_num = int(input("Enter an integer: "))
result = reverse_integer(input_num)
print("Reversed integer:", result)

