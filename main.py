import tkinter as tk
from tkinter import ttk

from core.conversor import converter_imagens
from core.pdf import juntar_pdfs


# ----------------------
# Janela Principal
# ----------------------

root = tk.Tk()

root.title("Conversor PDF")
root.geometry("430x200")
root.resizable(False, False)


# ----------------------
# Tema
# ----------------------

style = ttk.Style()
style.theme_use("clam")

style.configure(
    "Botao.TButton",
    font=("Segoe UI", 13, "bold"),
    padding=15
)


# ----------------------
# Botão Converter Imagens
# ----------------------

btn_converter = ttk.Button(
    root,
    text="🖼️ Imagens para PDF",
    style="Botao.TButton",
    command=converter_imagens
)

btn_converter.pack(
    fill="x",
    padx=40,
    pady=(35, 15)
)


# ----------------------
# Botão Juntar PDFs
# ----------------------

btn_juntar = ttk.Button(
    root,
    text="📄 Juntar PDFs",
    style="Botao.TButton",
    command=juntar_pdfs
)

btn_juntar.pack(
    fill="x",
    padx=40,
    pady=0
)


# ----------------------
# Loop
# ----------------------

root.mainloop()