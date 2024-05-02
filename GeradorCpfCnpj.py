import keyboard
import pyperclip
import random
from random import randint


class GeradorCpfCnpj:
    mascara = False
    def generate_cpf(self):
        while True:
            cpf = [randint(0, 9) for i in range(9)]
            if cpf != cpf[::-1]:
                break

        for i in range(9, 11):
            value = sum((cpf[num] * ((i + 1) - num) for num in range(0, i)))
            digit = ((value * 10) % 11) % 10
            cpf.append(digit)

        string_cpf = ''.join(map(str, cpf))
        if self.mascara:
            string_cpf = string_cpf[:3] + '.' + string_cpf[3:6] + '.' + string_cpf[6:9] + '-' + string_cpf[9:]
        print(string_cpf)
        pyperclip.copy(string_cpf)

    def generate_cnpj(self):
        cnpj = [random.randrange(10) for _ in range(8)] + [0, 0, 0, 1]

        for _ in range(2):
            value = sum(v * (i % 8 + 2) for i, v in enumerate(reversed(cnpj)))
            digit = 11 - value % 11
            cnpj.append(digit if digit < 10 else 0)

        string_cnpj = "".join(str(x) for x in cnpj)
        if self.mascara:
            string_cnpj = string_cnpj[:2] + '.' + string_cnpj[2:5] + '.' + string_cnpj[5:8] + '/' + string_cnpj[8:12] + '-' + string_cnpj[12:]
        print(string_cnpj)
        pyperclip.copy(string_cnpj)
    
    def toggle_mascara(self):
        self.mascara = not self.mascara
    
    def __init__(self):
        self.mascara = False

gerador = GeradorCpfCnpj()

keyboard.add_hotkey('ctrl+1', gerador.generate_cpf)
keyboard.add_hotkey('ctrl+2', gerador.generate_cnpj)
keyboard.add_hotkey('ctrl+*', gerador.toggle_mascara)
keyboard.wait('esc')


