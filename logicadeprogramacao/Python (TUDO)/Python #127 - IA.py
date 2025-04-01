import tkinter as tk
import google.generativeai as genai

genai.configure(api_key="AIzaSyDc_MrvKFjDCximm2Q_ih_ECBCPug3b_-k")

def send_message():
    msg = entry.get()
    entry.delete(0, tk.END)
    chat_history.insert(tk.END, f"Você: {msg}\n")
    
    response = genai.GenerativeModel("models/gemini-1.5-pro-001").start_chat().send_message(msg)
    cleaned_response = response.text.replace('*', '').replace('[', '').replace(']', '')

    chat_history.insert(tk.END, f"IA: {cleaned_response}\n")
    chat_history.yview(tk.END)

root = tk.Tk()
root.title("Chat com IA")

chat_history = tk.Text(root, height=30, width=100)
chat_history.pack(pady=10)

entry = tk.Entry(root, width=30, font="comic-sans")
entry.pack()

tk.Button(root, text="Enviar", command=send_message).pack()

root.mainloop()