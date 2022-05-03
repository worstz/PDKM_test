

def reverse_binary(number):
    if not str(number).isdigit():
        return "ข้อมูลที่ป้อนเข้ามาไม่ถูกต้อง"
    reverse_number = ''
    number = bin(int(number))
    for d in str(number[2:]):
        if d == '0':
            reverse_number += '1'
        else:
            reverse_number += '0'
    reverse_number = int(reverse_number, 2)
    return reverse_number


number = input("กรุณาป้อนตัวเลขฐานสิบ: ")
print(reverse_binary(number))
        