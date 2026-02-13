# exercise2.py
def print_factor(x):
    for i in range(1, x + 1):
        if x % i == 0:
            print(f"{x}的因子：{i}")

print_factor(52633)  # 输出52633的所有因子（含1和自身）
