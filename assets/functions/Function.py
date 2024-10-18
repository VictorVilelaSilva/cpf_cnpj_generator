import random
from random import randint

def generate_cpf(mask: bool) -> str:
    while True:
        cpf = [randint(0, 9) for i in range(9)]
        if cpf != cpf[::-1]:
            break

    for i in range(9, 11):
        value = sum((cpf[num] * ((i + 1) - num) for num in range(0, i)))
        digit = ((value * 10) % 11) % 10
        cpf.append(digit)

    string_cpf = "".join(map(str, cpf))
    if mask:
        string_cpf = (
            string_cpf[:3]
            + "."
            + string_cpf[3:6]
            + "."
            + string_cpf[6:9]
            + "-"
            + string_cpf[9:]
        )
    return string_cpf


def generate_cnpj(mask):
    cnpj = [random.randrange(10) for _ in range(8)] + [0, 0, 0, 1]
    for _ in range(2):
        value = sum(v * (i % 8 + 2) for i, v in enumerate(reversed(cnpj)))
        digit = 11 - value % 11
        cnpj.append(digit if digit < 10 else 0)
    string_cnpj = "".join(str(x) for x in cnpj)
    if mask:
        string_cnpj = (
            string_cnpj[:2]
            + "."
            + string_cnpj[2:5]
            + "."
            + string_cnpj[5:8]
            + "/"
            + string_cnpj[8:12]
            + "-"
            + string_cnpj[12:]
        )
    return string_cnpj


def digit_verifier_calculator(rg):
    weights = [2, 3, 4, 5, 6, 7, 8, 9]
    total = sum(int(rg[i]) * weights[i] for i in range(8))
    remainder = total % 11
    if remainder == 0:
        return "0"
    elif remainder == 1:
        return "X"
    else:
        return str(11 - remainder)


def generate_rg(mask: bool) -> str:
    rg = "".join(str(random.randint(0, 9)) for _ in range(8))
    check_digit = digit_verifier_calculator(rg)
    rg_with_check_digit = rg + check_digit
    if mask:
        rg_with_check_digit = (
            rg_with_check_digit[:2]
            + "."
            + rg_with_check_digit[2:5]
            + "."
            + rg_with_check_digit[5:8]
            + "-"
            + rg_with_check_digit[8:]
        )
    return rg_with_check_digit
