# Prepare a sua entrevista -- Python
# https://youtube.com/c/AutomationDataScience

# Desafio:
#     Crie uma função cujo argumento é uma string e opere dois números
#     identificados. Não pode usar eval( ) e tem que utilizar métodos dunder.

#     Vídeo-Desafio: https://youtube.com/shorts/rutjLHBFobc

def not_eval(p: str) -> int or float:

    a, operator, b = p.split()
    a, b = float(a), float(b)

    match operator:
        case '+':
            return a.__add__(b)
        case '-':
            return a.__sub__(b)
        case '*':
            return a.__mul__(b)
        case '/':
            return a.__truediv__(b)
        case '//':
            return a.__floordiv__(b)
        case '%':
            return a.__mod__(b)


# -- Testes
rsp = not_eval('3 + 9')
print(rsp)  # 12.0

rsp = not_eval('25 // 2.3')
print(rsp)  # 10.0

rsp = not_eval('203.4 - 158.9')
print(rsp)  # 44.5

rsp = not_eval('2030 % 4')
print(rsp)  # 2.0

rsp = not_eval('3 / 0')
print(rsp)  # ZeroDivisionError: float division by zero

