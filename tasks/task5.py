# tasks/task1.py



def solve():   
# Ниже пишите решение задачии(Обязательно поставьте четыре пробела после функции Solve())
    chislo1, chislo2, chislo3 = map(int, input().split())
    a = (chislo1 ** 2)
    b = (chislo2 ** 2)
    c = (chislo3 ** 2)
    print(a,b,c)


# Код ниже не трогать! он нужен для тестов
if __name__ == "__main__":
    solve()