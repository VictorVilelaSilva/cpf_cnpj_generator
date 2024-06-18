import tkinter as tk
import pyperclip
import random
import uuid
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
        self.result_label.config(text='CPF gerado: ' + string_cpf)
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
        self.result_label.config(text='CNPJ gerado: ' + string_cnpj)
        pyperclip.copy(string_cnpj)

    def calcula_digito_verificador(self, rg):
        pesos = [2, 3, 4, 5, 6, 7, 8, 9]
        soma = sum(int(rg[i]) * pesos[i] for i in range(8))
        resto = soma % 11
        if resto == 0:
            return '0'
        elif resto == 1:
            return 'X'
        else:
            return str(11 - resto)

    def generate_rg(self):
        rg = ''.join(str(random.randint(0, 9)) for _ in range(8))
        digito_verificador = self.calcula_digito_verificador(rg)
        rg_com_dv = rg + digito_verificador
        if self.mascara:
            rg_com_dv = rg_com_dv[:2] + '.' + rg_com_dv[2:5] + '.' + rg_com_dv[5:8] + '-' + rg_com_dv[8:]
        self.result_label.config(text='RG gerado: ' + rg_com_dv)
        pyperclip.copy(rg_com_dv)

    def generate_uuid(self):
        uuid_generated = str(uuid.uuid4())
        self.result_label.config(text='UUID gerado: ' + uuid_generated)
        pyperclip.copy(uuid_generated)

    def toggle_mascara(self):
        self.mascara = not self.mascara

    def __init__(self):
        self.mascara = False

        self.root = tk.Tk()
        self.root.title("Gerador de CPF/CNPJ")
        self.root.geometry("400x200")

        self.result_label = tk.Label(self.root, text="")
        self.result_label.pack()

        cpf_button = tk.Button(self.root, text="Gerar CPF", command=self.generate_cpf)
        cpf_button.pack()

        cnpj_button = tk.Button(self.root, text="Gerar CNPJ", command=self.generate_cnpj)
        cnpj_button.pack()

        rg_button = tk.Button(self.root, text="Gerar RG", command=self.generate_rg)
        rg_button.pack()

        uuid_button = tk.Button(self.root, text="Gerar UUID", command=self.generate_uuid)
        uuid_button.pack()

        mascara_button = tk.Button(self.root, text="Toggle Máscara", command=self.toggle_mascara)
        mascara_button.pack()

        self.root.mainloop()


gerador = GeradorCpfCnpj()

