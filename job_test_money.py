

def withdraw(money):
    if not str(money).isdigit():
        return "ข้อมูลที่ป้อนเข้ามาไม่ถูกต้อง"
    money = int(money)
    money_list = [1, 5, 10, 20, 100]
    money_list.sort()
    money_list.reverse()
    count = 0
    for d in money_list:
        amount = int(money/d)
        if money == 0:
            break
        elif amount >= 1:
            money = money - (amount*d)
            count += amount
    return "จำนวนธนบัตรที่จะได้รับ : {count}".format(count=count)




money = input("กรุณาป้อนจำนวนเงิน : ")
print(withdraw(money))


