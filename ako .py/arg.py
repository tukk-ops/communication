#args 任意數量的參數
def add(*args):
    total =0
    for arg in args:
        print(f"arg:{arg}")
        total += arg
    return total
print(add(1,2,2))