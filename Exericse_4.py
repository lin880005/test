
num=eval(input("請輸入一個正整數:"))

sum=0

for i in range(1,num+1):
    
    if i %7 == 0:
        sum+=i
    
print(f"從1到{num}的總和是:{sum}")

    
    

