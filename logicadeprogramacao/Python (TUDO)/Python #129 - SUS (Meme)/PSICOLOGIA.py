import tkinter as tk
import random
import time

falas = ["É complicado amigo", "Você tá errado", "Sei não em", "E seu ex?", "Você precisa se tratar", "Eu tenho medo de você", "Nossa Consulta acaba por aqui amigo", "sim", "nao", "Nao sei", "Me diz voce", "Eu acho que sim", "Eu acho que nao"]
escolha = random.choice(falas)

def send_message():
    escolha = random.choice(falas)
    msg = entry.get()

    if msg == "" or msg == " " or msg == "  " or msg == "   " or msg == "     " or msg == "      ":
        chat_history.insert(tk.END, f"Psicólogo: Erro amigo! Você não pode mandar um espaço em branco.\n")
    else:
        entry.delete(0, tk.END)
        chat_history.insert(tk.END, f"Você: {msg}\n")
        chat_history.insert(tk.END, f"Psicólogo: {escolha}\n")

def escolha():
    escolha = random.choice(falas)
    root.after(200, send_message)
    
root = tk.Tk()
root.title("Chat com IA")

chat_history = tk.Text(root, height=30, width=100)
chat_history.pack(pady=10)

entry = tk.Entry(root, width=30, font="Arial")
entry.pack()

tk.Button(root, text="Enviar", command=send_message).pack()

root.mainloop()
