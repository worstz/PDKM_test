
import string
def rocks_count(rocks):
    chr = string.ascii_uppercase
    if not all(s in chr for s in rocks):
        return print("ข้อมูลที่ป้อนเข้ามาไม่ถูกต้อง")
    count = {}
    for d in rocks:
        if not d in count:
            count[d] = 1
        else:
            count[d] += 1
    index = [d for d in count]
    index.sort()
    for i in index:
        print("{rocks} {count}".format(rocks=i, count=count[i]))
        

rocks = input("กรุณาป้อนตัวอักษรภาษาอังกฤษ A-Z: ")
rocks_count(rocks)

        