
num=eval(input("請輸入整數:"))

if num %7 == 0 & num %2 ==0:
    print(f"{num}是2及7的倍數")
elif num %2 == 0:
    print(f"{num}是2的倍數")
elif num %7 == 0:
    print(f"{num}是7的倍數")
else:
    print(f"{num}不是2及7的倍數")

print("嗨嗨嗨")

