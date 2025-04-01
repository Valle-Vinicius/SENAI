import tkinter as tk
from PIL import Image, ImageTk
import time
contador12 = 0

doencas = ["Gripe", "Covid-19", "Diabetes", "Hipertensão", "Câncer", "Asma", "Pneumonia", "AVC", "Alzheimer", "Hepatite", "Tuberculose", "Doença de Parkinson", "Artrite", "Insuficiência renal", "Doença celíaca", "Pressão Alta", "Pressão Baixa", "Ansiedade"]

def mostrar_doenca():
    global contador12
    doenca_selecionada = doenca_var.get()
    print(f"Você escolheu: {doenca_selecionada}")
    contador.config(text="é complicado", font=("Arial", 40))
    contador12 += 1 
        

interface = tk.Tk()
interface.geometry("500x500")
interface.title("USU (Único Sistema Umano) ")

imagem = Image.open("logo.png")  
imagem = imagem.resize((300, 300))  
imagem_tk = ImageTk.PhotoImage(imagem)

label_imagem = tk.Label(interface, image=imagem_tk)
label_imagem.place(relx=0.5, rely=0.2, anchor='center')

botao = tk.Button(interface, text="Escolher", command=mostrar_doenca, font=("Arial", 20), width=20, height=1)
botao.place(relx=0.5, rely=0.9, anchor='center')

doenca_var = tk.StringVar()
doenca_var.set(doencas[0])

contador = tk.Label(interface, text=f"Bem vindo! \n Escolha qual doença você tem no momento\n E eu farei o relatório para você ", font=("Arial", 15))
contador.place(relx=0.5, rely=0.5, anchor='center')
    
doenca_menu = tk.OptionMenu(interface, doenca_var, *doencas)
doenca_menu.config(font=("Arial", 18), width=20, height=1)
doenca_menu.place(relx=0.5, rely=0.7, anchor='center')

interface.mainloop()
