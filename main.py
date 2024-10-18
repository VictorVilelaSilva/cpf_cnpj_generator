from assets.functions.Function import generate_cnpj, generate_cpf, generate_rg
from PIL import ImageGrab
import tkinter as tk
import keyboard
import pyperclip
import uuid
import threading
import pyautogui




class MainWindow:
    mask: bool = False

    def get_cpf(self):
        string_cpf = generate_cpf(self.mask)
        self.result_label.config(text="Gerado CPF: " + string_cpf)
        pyperclip.copy(string_cpf)

    def get_cnpj(self):
        string_cnpj = generate_cnpj(self.mask)
        self.result_label.config(text="Gerado CNPJ: " + string_cnpj)
        pyperclip.copy(string_cnpj)

    def get_rg(self):
        rg = generate_rg(self.mask)
        self.result_label.config(text="Gerado RG: " + rg)
        pyperclip.copy(rg)

    def get_uuid(self):
        uuid_generated = str(uuid.uuid4())
        self.result_label.config(text="Gerado UUID: " + uuid_generated)
        pyperclip.copy(uuid_generated)

    def toggle_mask(self):
        self.mask = not self.mask

    def __init__(self, root):
        self.mask = False
        self.container1 = tk.Frame(root, background="#d4d4d4", border=1, relief='raised' , width=598, height=800)
        self.container2 = tk.Frame(root, background="#d4d4d4", border=1, relief='raised', width=598, height=800)
        self.container1.pack(side="left", expand=True)
        self.container2.pack(side="right", expand=True)
        # self.title = tk.Label(self.fr1, text="Gerador de Documentos", font=("Arial", 20))
        # self.title.pack()

        # self.result_label = tk.Label(self.root, text="TDFD")
        # self.result_label.pack(pady=(10, 10))
        # self.result_label.config(fg="#000", bg="#fff", borderwidth=2.5, relief="groove")
        # cpf_button = tk.Button(self.root, text="Gerar CPF", command=self.get_cpf)
        # cpf_button.pack(pady=(0, 10))

        # cnpj_button = tk.Button(self.root, text="Gerar CNPJ", command=self.get_cnpj)
        # cnpj_button.pack(pady=(0, 10))

        # rg_button = tk.Button(self.root, text="Gerar RG", command=self.get_rg)
        # rg_button.pack(pady=(0, 10))

        # uuid_button = tk.Button(self.root, text="Gerar UUID", command=self.get_uuid)
        # uuid_button.pack(pady=(0, 10))

        # mask_button = tk.Button(self.root, text="Toggle Mask", command=self.toggle_mask)
        # mask_button.pack(pady=(0, 10))
        # keyboard.add_hotkey("ctrl+1", self.get_cpf)
        # keyboard.add_hotkey("ctrl+2", self.get_cnpj)
        # keyboard.add_hotkey("ctrl+3", self.get_rg)
        # keyboard.add_hotkey("ctrl+4", self.get_uuid)
        # keyboard.add_hotkey("ctrl+*", self.toggle_mask)


root = tk.Tk()
root.title('FDTD')
root.geometry("1200x800")

generator = MainWindow(root)
root.mainloop()
