# exercise3.py
def print_factor(x):
    print(f"\n数字{x}的所有因子：")
    for i in range(1, x + 1):
        if x % i == 0:
            print(i)
            
# 列表迭代计算
l = [52633, 8137, 1024, 999]
for num in l:
    print_factor(num)
