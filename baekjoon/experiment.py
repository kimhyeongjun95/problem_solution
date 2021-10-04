def dec_to_bin(num):

    result = []
    while True:
        num, remainder = divmod(num, 2) # 몫이랑 나머지가 나옴
        
        if num < 2:
            result.append(remainder)
            result.append(num)
            break
        
        result.append(remainder)

    return result[::-1]

def dec_to_base_x(num, base):

    result = []
    while num: # 몫이 0보다 큰 동안 계속 나누기
        result.append(num % base)
        num = num // base

    return ''.join(map(str, result[::-1]))

num = 19
print(bin(num)) #2
print(oct(num)) #8
print(hex(num)) #16

print(dec_to_bin(num))
print('10진법 => 2진법', dec_to_base_x(num, 2))
print('10진법 => 3진법', dec_to_base_x(num, 3))
print('10진법 => 8진법', dec_to_base_x(num, 8))
print('10진법 => 16진법', dec_to_base_x(num, 16))